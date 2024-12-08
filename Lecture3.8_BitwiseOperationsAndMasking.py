# Побитовые операции и маскирование
# Чтобы продемонстрировать эти операции, давайте создадим несколько простых изображений

import cv2
import numpy as np

# Если вам интересно, почему только два измерения, ну, это изображение в оттенках серого,
# если бы мы делали цветное изображение, мы бы использовали
# прямоугольник = np.zeros((300, 300, 3),np.uint8)

# Создаем квадрат
square = np.zeros((300, 300), np.uint8)
cv2.rectangle(square, (50, 50), (250, 250), 255, -2)
cv2.imshow("Square", square)
cv2.waitKey(0)

# Making a elliple
ellipse = np.zeros((300, 300), np.uint8)
cv2.ellipse(ellipse, (150, 150), (150, 150), 30, 0, 180, 255, -1)
cv2.imshow("Ellipse", ellipse)
cv2.waitKey(0)

cv2.destroyAllWindows()

# Experimenting with some bitwise operations

# Shows only where they intersect
And = cv2.bitwise_and(square, ellipse)
cv2.imshow("AND", And)
cv2.waitKey(0)

# Shows where either square or ellipse is
bitwiseOr = cv2.bitwise_or(square, ellipse)
cv2.imshow("OR", bitwiseOr)
cv2.waitKey(0)

# Shows where either square or ellipse is
bitwiseXor = cv2.bitwise_xor(square, ellipse)
cv2.imshow("XOR", bitwiseXor)
cv2.waitKey(0)

# Shows everything that isn't part of the square
bitwiseNot_sq = cv2.bitwise_not(square)
cv2.imshow("NOT - square", bitwiseNot_sq)
cv2.waitKey(0)

### Обратите внимание, что последняя операция полностью инвертирует изображение.

cv2.destroyAllWindows()