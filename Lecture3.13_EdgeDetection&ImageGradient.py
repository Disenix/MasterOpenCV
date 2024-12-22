import cv2
import numpy as np

image = cv2.imread('image.jpg', 0)

height, width = image.shape

# Extract Sobel Edges
sobel_x = cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize=5)
sobel_y = cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize=5)

cv2.imshow('Original', image)
cv2.waitKey(0)
cv2.imshow('Sobel X', sobel_x)
cv2.waitKey(0)
cv2.imshow('Sobel Y', sobel_y)
cv2.waitKey(0)

sobel_OR = cv2.bitwise_or(sobel_x, sobel_y)
cv2.imshow('sobel_OR', sobel_OR)
cv2.waitKey(0)

laplacian = cv2.Laplacian(image, cv2.CV_64F)
cv2.imshow('Laplacian', laplacian)
cv2.waitKey(0)

## Затем нам нужно указать два значения: threshold1 и threshold2. Любое значение градиента больше, чем threshold2
# считается краем. Любое значение ниже threshold1 не считается краем.
#Значения между threshold1 и threshold2 классифицируются как края или не-края в зависимости от того, как их
#интенсивности «связаны». В этом случае любые значения градиента ниже 60 считаются не-краями,
#тогда как любые значения выше 120 считаются краями.

# Canny Edge Detection использует значения градиента в качестве порогов
# Первый пороговый градиент
canny = cv2.Canny(image, 50, 120)
cv2.imshow('Canny', canny)
cv2.waitKey(0)

cv2.destroyAllWindows()
