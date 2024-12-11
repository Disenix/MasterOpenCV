import cv2
import numpy as np

image = cv2.imread('image.jpg')
cv2.imshow("Original image", image)
cv2.waitKey(0)

# Creating our 3x3 kernel
kernel_3x3 = np.ones((3, 3), np.float32) / 9

# We use the cv2.filter2D to convolve the kernel with an image
blurred = cv2.filter2D(image, -1, kernel_3x3)
cv2.imshow('3x3 Kernel Blurring', blurred)
cv2.waitKey(0)

# Creating our 7x7 kernel
kernel_7x7 = np.ones((7, 7), np.float32) / 49

blurred2 = cv2.filter2D(image, -1, kernel_7x7)
cv2.imshow('7x7 Kernel Blurring', blurred2)
cv2.waitKey(0)

cv2.destroyAllWindows()

# Other commonly used blurring methods in OpenCV

# Размытие с использованием усреднения (Averaging)
# Averaging done by convolving the image with a normalized box filter /  Усреднение выполняется путём свёртки изображения с нормализованным "коробочным" фильтром
# This takes the pixels under the box and replaces the centreal element /  Фильтр берёт пиксели внутри окна и заменяет центральный элемент усреднённым значением
# Box size needs to odd and positive / Размер окна (коробки) должен быть нечётным и положительным
blur = cv2.blur(image, (3, 3))
cv2.imshow('Averaging', blur)
cv2.waitKey(0)

# Размытие с использованием гауссового фильтра
# Instead of box filter, gaussian kernel / Вместо коробочного фильтра используется гауссово ядро
Gaussian = cv2.GaussianBlur(image, (7, 7), 0)
cv2.imshow('Gaussian Bluring', Gaussian)
cv2.waitKey(0)


# Размытие с использованием медианного фильтра(salt and pepper)
# Takes median of all the pixels under kernel area and centeal element is replaced with this median volue / Берётся медианное значение всех пикселей в области ядра, и центральный элемент заменяется этим значением
median = cv2.medianBlur(image, 5)
cv2.imshow('Median Blurring', median)
cv2.waitKey(0)

# Билатеральное размытие
# Bilateral is very effective in noice removal while keeping edges sharp / Очень эффективно для удаления шума, при этом сохраняет чёткие границы объектов
bilateral = cv2.bilateralFilter(image, 9, 75, 75)
cv2.imshow('Bilateral Blurring', bilateral)
cv2.waitKey(0)
cv2.destroyAllWindows()


# Удаление шума с помощью метода Non-Local Means / # Удаление шума методом нелокального среднего)
# Image De-noising - Non-Local Means Denoising

import cv2
import numpy as np

image = cv2.imread('image.jpg')

# parameters, after None are - the filter strength 'h' (5-10 is a good range)
# Next is hForColorComponents, set as same value as h again
# Параметры после None:
# - Сила фильтрации 'h' (обычно в диапазоне от 5 до 10)
# - hForColorComponents: значение для цветных компонент, обычно устанавливается таким же, как 'h'

dst = cv2.fastNlMeansDenoisingColored(image, None, 6, 6, 7, 21)

cv2.imshow('Fast Means Denosing', dst)
cv2.waitKey(0)

cv2.destroyAllWindows()

# There are 4 variations of Non-Local Means Denoising:
# cv2.fastNlMeansDenoising() - works with a single grayscale images
# cv2.fastNlMeansDenoisingColored() - works with a color image.
# cv2.fastNlMeansDenoisingMulti() - works with image sequence captured in short period of time (grayscale images)
# cv2.fastNlMeansDenoisingColoredMulti() - same as above, but for color images.

# cv2.fastNlMeansDenoising() - работает с одиночными изображениями в градациях серого
# cv2.fastNlMeansDenoisingColored() - работает с цветными изображениями
# cv2.fastNlMeansDenoisingMulti() - работает с последовательностью изображений в градациях серого, захваченных в короткий промежуток времени
# cv2.fastNlMeansDenoisingColoredMulti() - аналогично предыдущему, но для цветных изображений
