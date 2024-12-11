import cv2
import numpy as np

# Загрузка изображения
image = cv2.imread('portrait.jpg')
image = cv2.resize(image, (400, 400))  # Уменьшаем для удобства визуализации

# Создание окна для отображения
cv2.namedWindow('Blurring Methods', cv2.WINDOW_NORMAL)

# Функция для показа результата с задержкой
def show_result(title, processed_image, delay=10000):
    combined = np.hstack((image, processed_image))  # Оригинал + обработанное
    cv2.imshow(title, combined)
    cv2.waitKey(delay)

# 1. Averaging (Усреднение)
blur = cv2.blur(image, (15, 15))  # Большое окно для заметного эффекта
show_result('Averaging', blur)

# 2. Gaussian Blurring (Гауссово размытие)
gaussian = cv2.GaussianBlur(image, (15, 15), 0)
show_result('Gaussian Blurring', gaussian)

# 3. Median Blurring (Медианное размытие)
median = cv2.medianBlur(image, 15)  # Размер окна должен быть нечётным
show_result('Median Blurring', median)

# 4. Bilateral Blurring (Билатеральное размытие)
bilateral = cv2.bilateralFilter(image, 9, 75, 75)  # Параметры: диаметр, sigmaColor, sigmaSpace
show_result('Bilateral Blurring', bilateral)

# 5. Non-Local Means Denoising (Удаление шума методом нелокального среднего)
denoised = cv2.fastNlMeansDenoisingColored(image, None, 10, 10, 7, 21)
show_result('Non-Local Means Denoising', denoised)

cv2.destroyAllWindows()
