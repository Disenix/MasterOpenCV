import cv2
import numpy as np

image = cv2.imread('test.jpg')

# Let's make our image 3/4 of it's original size
image_scaled = cv2.resize(image, None, fx=0.75, fy=0.75)
cv2.imshow('Scalling - Linear Interpolation', image_scaled)
cv2.waitKey()

# Let's double the size of our image
img_scalled = cv2.resize(image, None, fx=2, fy=2, interpolation = cv2.INTER_CUBIC)
cv2.imshow('Scalling - Cubic Interpolation', image_scaled)
cv2.waitKey()

# Let's sker the re-sizing by setting exact dimensions
img_scaled = cv2.resize(image, (900, 400), interpolation = cv2.INTER_AREA)
cv2.waitKey()

cv2.destroyAllWindows()