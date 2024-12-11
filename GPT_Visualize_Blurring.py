import cv2
import numpy as np
import time

# Загрузка изображения
image = cv2.imread('image.jpg')
image = cv2.resize(image, (300, 300))  # Уменьшаем для удобства визуализации
output = image.copy()  # Копия для отображения результата
kernel_size = 50  # Размер ядра

# Функция для рисования ядра на изображении
def draw_kernel(img, top_left, kernel_size, color=(0, 255, 0)):
    x, y = top_left
    cv2.rectangle(img, (x, y), (x + kernel_size, y + kernel_size), color, 2)

# Процесс визуализации
for y in range(0, image.shape[0] - kernel_size + 1):  # Движение по строкам
    for x in range(0, image.shape[1] - kernel_size + 1):  # Движение по столбцам
        # Копируем изображение для текущей итерации
        temp_image = image.copy()
        
        # Рисуем текущую область ядра
        draw_kernel(temp_image, (x, y), kernel_size)

        # Усреднение текущей области
        region = image[y:y + kernel_size, x:x + kernel_size]  # Вырезаем область
        average_color = region.mean(axis=(0, 1))  # Усредняем цвет (по каналам RGB)
        output[y + kernel_size // 2, x + kernel_size // 2] = average_color  # Присваиваем центральному пикселю

        # Показываем изображение с движением ядра
        combined = np.hstack((temp_image, output))  # Оригинал и результат рядом
        cv2.imshow('Kernel Movement', combined)

        # Задержка для анимации
        if cv2.waitKey(1) & 0xFF == 27:  # Нажми ESC для выхода
            break

cv2.destroyAllWindows()
