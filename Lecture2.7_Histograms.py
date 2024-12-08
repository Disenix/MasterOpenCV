import cv2
import numpy as np

# We need to import matplotlib to create our histogram plots
from matplotlib import pyplot as plt

image = cv2.imread('example.jpg')

# Вычисляем гистограмму для полного изображения
# cv2.calcHist(
#    [image],    # Изображение для расчета гистограммы (в формате списка)
#    [0],        # Канал изображения (0 - синий, 1 - зеленый, 2 - красный)
#    None,       # Маска (если None, рассчитывается для всего изображения)
#    [256],      # Количество ячеек (диапазон значений от 0 до 255 разбивается на 256 интервалов)
#    [0, 256]    # Диапазон значений для гистограммы
histogram = cv2.calcHist([image], [0], None, [256], [0, 256])

# Cтроим гистограмму, ravel() преобразует массив изображения в одномерный
plt.hist(image.ravel(), 256, [0, 256]); plt.show()

# Просмотр отдельный световых каналов
color = ('b', 'g', 'r')

# Разделяем каналы цветов и строим гистограмму для каждого из них
for i, col in enumerate(color):
    histogram2 = cv2.calcHist([image], [i], None, [256], [0, 256])
    plt.plot(histogram2, color=col)
    plt.xlim([0, 256])

plt.show()
