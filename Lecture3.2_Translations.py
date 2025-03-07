import cv2
import numpy as np

image = cv2.imread('test.jpg')

# Сохраняем высоту и ширину изображения
height, width = image.shape[:2]

quarter_height, quarter_width = height/4, width/4

#       | 1 0 Tx |
#  T  = | 0 1 Ty |

# T is our translations matrix
T = np.float32([[1, 0, quarter_width], [0, 1, quarter_height]])

# We use warpAffine to transform the image using the matrix, T
img_translation = cv2.warpAffine(image, T, (width, height))
cv2.imshow('Translation', img_translation)
cv2.waitKey()
cv2.destroyAllWindows()
