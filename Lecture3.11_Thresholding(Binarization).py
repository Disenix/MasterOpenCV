# Пороговая обработка

# Пороговое преобразование, бинаризация и адаптивное пороговое преобразование
# При пороговом преобразовании мы преобразуем изображение в оттенках серого в его двоичную форму
import cv2
import numpy as np

# Load our image as grayscale
image = cv2.imread('gradient.jpg')
cv2.imshow('Original', image)

# Values below 127 goes to 0 (black, everything above goes to 255(white))
ret, thresh1 = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)
cv2.imshow('1 Threshold Binary', thresh1)

# Values below 127 go to 255 and values above 127 go to 0 (reverse of above)
ret, thresh2= cv2.threshold(image, 127, 255, cv2.THRESH_BINARY_INV)
cv2.imshow('2 Threshold Binary Inverse', thresh2)

# Values above 127 are truncated (held) at 127 (the 255 argument is unused)
ret, thresh3 = cv2.threshold(image, 127, 255, cv2.THRESH_TRUNC)
cv2.imshow('3 THRESH TRUNC', thresh3)

# Values below 127 of to 0, above 127 are unchanged
ret, thresh4 = cv2.threshold(image, 127, 255, cv2.THRESH_TOZERO)
cv2.imshow('4 THRESH TOZERO', thresh4)

# Reseveer of above, below 127 is unchanged, above 127 goes to 0
ret, thresh5 = cv2.threshold(image, 127, 255, cv2.THRESH_TOZERO_INV)
cv2.imshow('5 THRESH TOZERO INV', thresh5)
cv2.waitKey(0)

cv2.destroyAllWindows()


# Adaptive thresholding
import cv2
import numpy as np

image = cv2.imread('Origin_of_Species.jpg', 0)

cv2.imshow('Original', image)
cv2.waitKey(0)

# Values below 127 goes to 0(black, everything abovw goes to 255 (white))
ret, thresh1 = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)
cv2.imshow('Threshold Binary', thresh1)
cv2.waitKey(0)

# It's good practice to blur images as it removes noice
image = cv2.GaussianBlur(image, (3, 3), 0)

# Using adaptiveThreshold
thresh = cv2.adaptiveThreshold(image, 255, cv2.ADAPTIVE_THRESH_MEAN_C, 
                               cv2.THRESH_BINARY, 3, 5) 
cv2.imshow("Adaptive Mean Thresholding", thresh) 
cv2.waitKey(0)

_, th2 = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
cv2.imshow("Otsu's Thresholding", thresh)
cv2.waitKey(0)

# Otsu's thresholding after Gaussian filtering
blur = cv2.GaussianBlur(image, (5, 5), 0)
_, th3 = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
cv2.imshow("Gaussian Otsu's Thresholding", thresh)
cv2.waitKey(0)

cv2.destroyAllWindows()


