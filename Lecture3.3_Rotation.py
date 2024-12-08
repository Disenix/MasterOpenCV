import cv2
import numpy as np

image = cv2.imread('test.jpg')
height, width = image.shape[:2]

# Divide by two to rototate the image around its centre
rotation_matrix = cv2.getRotationMatrix2D((width/2, height/2), 90, .5)

rotated_image = cv2.warpAffine(image, rotation_matrix, (width, height))

cv2.imshow('Rotated Image', rotated_image)
cv2.waitKey()
cv2.destroyAllWindows()


# Other Option in rotate
img = cv2.imread('test.jpg')

rotated_image = cv2.transpose(img)

cv2.imshow('Rotated image - Method 2', rotated_image)
cv2.waitKey()
cv2.destroyAllWindows()

# Let's now to a horizontal flip
flipped = cv2.flip(image, 1)
cv2.imshow('Horizontal flip', flipped)
cv2.waitKey()
cv2.destroyAllWindows()

           