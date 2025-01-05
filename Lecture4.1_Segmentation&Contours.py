import cv2
import numpy as np

image = cv2.imread('images/shapes.jpg')
cv2.imshow('Input Image', image)
cv2.waitKey(0)

# Grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Find Canny edges
edged = cv2.Canny(gray, 30, 200) 
cv2.imshow('Canny Edges', edged)
cv2.waitKey(0)

# Finding Contours
# Use a copy of your image e.g. edged.copy(), since findContours alters the image
contours, hierarchy = cv2.findContours(edged, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
cv2.imshow('Canny Edges After Contouring', edged)
cv2.waitKey(0)

print('Number of Contours found = ' + str(len(contours)))

# Draw all conrours
# Use '-1' as the 3rd parameter to draw all
cv2.drawContours(image, contours, -1, (0, 255, 0), 3)

cv2.imshow('Contours', image)
cv2.waitKey(0)
cv2.destroyAllWindows()

#! cv2.findContours(image, Retrieval Mode, Approximation Method)
# Возвращает -> contours,hierarchy
# ПРИМЕЧАНИЕ В OpenCV 3.X findContours возвращает 3-й аргумент,
# который является ret (или логическим значением, указывающим, была ли функция успешно запущена).
# Если вы используете OpenCV 3.X, замените строку 12 на:
# _, contours,hierarchy = cv2.findContours(image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
# Переменная 'contours' хранится как массив numpy точек (x,y), которые образуют контур
# В то время как 'hierarchy' описывает отношения дочерних и родительских элементов между
# контурами (т. е. контурами внутри контуров)
# Методы аппроксимации
# Использование cv2.CHAIN_APPROX_NONE сохраняет все граничные точки.
# Но нам не обязательно нужны все граничные точки. Если точки
# образуют прямую линию, нам нужны только начальная и конечная точки этой линии.
# Использование cv2.CHAIN_APPROX_SIMPLE вместо этого предоставляет только эти
# начальные и конечные точки ограничивающих контуров, что приводит
# к гораздо более эффективному хранению информации о контурах.