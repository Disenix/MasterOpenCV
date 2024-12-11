import cv2
import numpy as np

image = cv2.imread('image.jpg')
cv2.imshow('Original Image', image)

# 1. Базовое ядро для усиления резкости
kernel_sharpening = np.array(([-1, -1, -1],
                              [-1, 9, -1],
                              [-1, -1, -1]))

sharpened = cv2.filter2D(image, -1, kernel_sharpening)
cv2.imshow('Sharpening (Basic)', sharpened)

# 2. Более сильное усиление резкости
# Увеличиваем значение в центре, чтобы усилить контраст ещё больше
kernel_sharpening_strong = np.array([[-1, -1, -1],
                                     [-1, 12, -1],
                                     [-1, -1, -1]])

sharpened_strong = cv2.filter2D(image, -1, kernel_sharpening_strong)
cv2.imshow('Sharpening (Strong)', sharpened_strong)

# 3. Уменьшенное усиление резкости (мягкое)
# Уменьшаем центральное значение, чтобы добиться мягкой резкости
kernel_sharpening_soft = np.array([[-1, -1, -1],
                                     [-1, 5, -1],
                                     [-1, -1, -1]])

sharpened_soft = cv2.filter2D(image, -1, kernel_sharpening_soft)
cv2.imshow('Sharpening (Soft)', sharpened_soft)

# 4. Ядро для усиления горизонтальных деталей
# Усиливаем горизонтальные линии, подавляя вертикальные
kernel_horizontal = np.array([[-1, -1, -1],
                              [2, 2, 2],
                              [-1, -1, -1]])

sharpened_horizontal = cv2.filter2D(image, -1, kernel_horizontal)
cv2.imshow('Sharpening(Horizontal Details)', sharpened_horizontal)

# 5. Ядро для усиления вертикальных деталей
# Усиливаем вертикальные линии, подавляя горизонтальные
kernel_vertical = np.array([[-1, 2, -1],
                            [-1, 2, -1],
                            [-1, 2, -1]])

sharpened_vertical = cv2.filter2D(image, -1, kernel_vertical)
cv2.imshow('Sharpening (Vertical Details)', sharpened_vertical)

cv2.waitKey(0)
cv2.destroyAllWindows()

