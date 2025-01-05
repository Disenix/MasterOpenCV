import cv2
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Укажи путь к своему изображению
image_path = "your_image_path.jpg"
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)  # Загружаем в оттенках серого

# Выделение границ с помощью алгоритма Канни
edges = cv2.Canny(image, 100, 200)

# Поиск контуров (все точки)
contours, hierarchy = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

# Готовим данные для анимации
all_points = [np.squeeze(contour) for contour in contours]  # Убираем лишние измерения
flat_points = np.concatenate(all_points, axis=0)  # Объединяем все точки в один массив

# Функция для обновления анимации
fig, ax = plt.subplots(figsize=(6, 6))
ax.imshow(image, cmap='gray')
scatter, = ax.plot([], [], 'ro', markersize=2)

def update(frame):
    if frame < len(flat_points):
        scatter.set_data(flat_points[:frame, 0], flat_points[:frame, 1])
    return scatter,

# Анимация
ani = FuncAnimation(fig, update, frames=len(flat_points), interval=5, blit=True)
plt.title("Алгоритм обхода контура")
plt.axis('off')
plt.show()
