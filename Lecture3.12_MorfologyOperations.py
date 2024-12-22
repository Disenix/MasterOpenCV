import cv2
import numpy as np

image = cv2.imread('Origin_of_Species.jpg', 0)

cv2.imshow('Original', image)
cv2.waitKey(0)

# Let's define our kernel size
kernel = np.ones((5, 5), np.uint8)
# np.uint8: Указывает тип данных ядра — 8-битные целые числа.
# Размер ядра влияет на степень воздействия операций: большее ядро — сильнее эффект.


# Now we erode(эрозия - сужение)
# cv2.erode: Выполняет эрозию, то есть "съедает" белые пиксели (255) по краям объектов.
# kernel: Определяет, как далеко "сужать" белые области.
# iterations=1: Указывает, сколько раз применять эрозию. Больше итераций — сильнее эффект.
erosion = cv2.erode(image, kernel, iterations=1)
cv2.imshow('Erosion', erosion)
cv2.waitKey(0)
# Назначение:
# - Уменьшение белых объектов.
# - Удаление мелких белых шумов.


# Dilation - Дилатация(Расширение)
# cv2.dilate: Выполняет дилатацию, то есть расширяет белые пиксели (255) по краям объектов
# kernel: Определяет, насколько "расширять" белые области.
# iterations=1: Количество итераций дилатации.
dilation = cv2.dilate(image, kernel, iterations=1)
cv2.imshow('Dilation', dilation)
cv2.waitKey(0)
# Назначение:
# - Увеличение белых объектов.
# - Заполнение мелких дыр в белых областях.

# Opening (Открытие)
# cv2.morphologyEx: Выполняет морфологическую операцию.
# cv2.MORPH_OPEN: Открытие — это эрозия, затем дилатация.
opening = cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel)
cv2.imshow('Opening', opening)
cv2.waitKey(0)
# Назначение:
# - Удаление мелкого шума (мелкие белые точки исчезают).
# - Сглаживание объектов, сохраняя их общий размер.

# Closing (Закрытие)
# cv2.morphologyEx: Выполняет морфологическую операцию.
# cv2.MORPH_CLOSE: Закрытие — это дилатация, затем эрозия.
closing = cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernel)
cv2.imshow('Closing', closing)
cv2.waitKey(0)
# Назначение:
# - Заполнение дыр внутри белых объектов.
# - Соединение разорванных частей объекта.


cv2.destroyAllWindows()
