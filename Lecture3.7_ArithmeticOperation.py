# Арифметические операции
# Это простые операции, которые позволяют нам напрямую добавлять или вычитать интенсивность цвета.
# Вычисляет операцию для каждого элемента двух массивов. Общий эффект — увеличение или уменьшение яркости.

import cv2 
import numpy as np

image = cv2.imread('image.jpg')

# Создаем матрицу из единиц, затем умножаем ее на масштаб 100
# Это дает матрицу с теми же размерами, что и наше изображение, со всеми значениями 100
M = np.ones(image.shape, dtype = "uint8") * 175

# Мы используем это, чтобы добавить эту матрицу M к нашему изображению
# Обратите внимание на увеличение яркости
added = cv2.add(image, M)
cv2.imshow("Added", added)

# Аналогично мы можем вычесть
# Обратите внимание на уменьшение яркости
subtracted = cv2.subtract(image, M)
cv2.imshow("Subtracted", subtracted)

cv2.waitKey(0)
cv2.destroyAllWindows()

