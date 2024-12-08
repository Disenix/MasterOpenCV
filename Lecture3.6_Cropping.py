import cv2
import numpy as np

image = cv2.imread('test.jpg')
height, width = image.shape[:2]

#Let's get the starting pixel coordinates (top Left of cropping rectangle)
start_row, start_col = int(height * .25), int(width * .25)

# Let's get the ending pixel coordinated (bottom right)
end_row, end_col = int(height * .75), int(width * .75)

# Simply use indexing to crop out the rectangle we desire
cropped = image[start_row:end_row, start_col:end_col]

cv2.imshow('Original image', image)
cv2.waitKey(0)
cv2.imshow("Cropped image", cropped)
cv2.waitKey(0)
cv2.destroyAllWindows()
