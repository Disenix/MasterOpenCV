import cv2
import numpy as np

# Функция для создания эффекта скетча
def sketch(image):
    # Преобразуем изображение в оттенки серого
    imgGray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Убираем шум с помощью размытия Гаусса
    imgGrayBlur = cv2.GaussianBlur(imgGray, (5, 5), 0)

    # Извлекаем края изображения с использованием детектора Кэнни
    cannyEdges = cv2.Canny(imgGrayBlur, 10, 70)

    # Применяем бинаризацию с инверсией: светлые области становятся темными, и наоборот
    ret, mask = cv2.threshold(cannyEdges, 70, 255, cv2.THRESH_BINARY_INV)

    # Возвращаем итоговое изображение
    return mask

# Инициализация веб-камеры: создаем объект cap для захвата видео
# Инициализируем веб-камеру, cap — это объект, предоставленный VideoCapture
# Он содержит логическое значение, указывающее, было ли это успешно (ret)
# Он также содержит изображения, полученные с веб-камеры (frame)
cap = cv2.VideoCapture(0)

while True:
    # Считываем текущий кадр с веб-камеры
    ret, frame = cap.read()

    # Показываем обработанный кадр с эффектом скетча в отдельном окне
    cv2.imshow('Our Live Sketcher', sketch(frame))

    # Если нажата клавиша Enter (код 13), выходим из цикла
    if cv2.waitKey(1) == 13: 
        break

# Освобождаем веб-камеру для других приложений
cap.release()

# Закрываем все окна OpenCV
cv2.destroyAllWindows()