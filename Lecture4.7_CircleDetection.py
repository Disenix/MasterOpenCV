import cv2
import numpy as np

# Загружаем изображение
image = cv2.imread('images/bottlecaps.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Применяем размытие
blur = cv2.medianBlur(gray, 5)

# Находим круги методом Хафа
circles = cv2.HoughCircles(blur, cv2.HOUGH_GRADIENT, dp=1.5, minDist=10)

# Проверяем, найдены ли круги
if circles is not None:
    circles = np.uint16(np.around(circles))
    for i in circles[0, :]:
        # Рисуем внешний круг
        cv2.circle(image, (i[0], i[1]), i[2], (255, 0, 0), 2)
        # Рисуем центр круга
        cv2.circle(image, (i[0], i[1]), 2, (0, 255, 0), 5)

# Отображаем результат
cv2.imshow('Detected Circles', image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# not worked
