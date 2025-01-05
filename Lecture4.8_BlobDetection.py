# Импорт библиотек
import cv2
import numpy as np

# Загрузка изображения
image = cv2.imread("images/Sunflowers.jpg")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Применяем размытие для удаления шума
blur = cv2.GaussianBlur(gray, (5, 5), 0)

# Настраиваем параметры для детектора
params = cv2.SimpleBlobDetector_Params()

# Фильтрация по цвету
params.filterByColor = True
params.blobColor = 255  # Белые объекты

# Фильтрация по размеру
params.filterByArea = True
params.minArea = 30  # Минимальная площадь
params.maxArea = 5000  # Максимальная площадь

# Фильтрация по круговой форме
params.filterByCircularity = True
params.minCircularity = 0.5  # Уровень округлости

# Создаём детектор
detector = cv2.SimpleBlobDetector_create(params)

# Находим круги
keypoints = detector.detect(blur)

# Рисуем круги на изображении в оттенках серого
blobs_on_gray = cv2.drawKeypoints(gray, keypoints, np.zeros((1, 1)), 
                                  (0, 255, 255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

# Отображаем результат
cv2.imshow("Blobs on Gray Image", blobs_on_gray)
cv2.waitKey(0)
cv2.destroyAllWindows()
