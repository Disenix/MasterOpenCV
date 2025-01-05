# Mini-Project # 3 - Counting Circles and Ellipses

import cv2
import numpy as np

# Load image
image = cv2.imread('images/blobs.jpg')
cv2.imshow('Original Image', image)
cv2.waitKey(0)

# Initialize the detector using the default parameters
detector = cv2.SimpleBlobDetector_create()

# Detect blobs
keypoints = detector.detect(image)

# Draw blobs on our image as red circles with fixed size
blank = np.zeros((1, 1))
blobs = cv2.drawKeypoints(image, keypoints, blank, (0, 0, 255), cv2.DRAW_MATCHES_FLAGS_DEFAULT)

# Display the total number of blobs
number_of_blobs = len(keypoints)
text = "Total Number of Blobs: " + str(len(keypoints))
cv2.putText(blobs, text, (20, 550), cv2.FONT_HERSHEY_SIMPLEX, 1, (100, 0, 255), 2)

# Display image with blob keypoints
cv2.imshow('Blobs using default parameters', blobs)
cv2.waitKey(0)

# Set our filtering parameters
# Initialize parameter setting using cv2.SimpleBlobDetector_Params
params = cv2.SimpleBlobDetector_Params()

# Set area filtering parameters
params.filterByArea = True
params.minArea = 100

# Set Circularity filtering parameters
params.filterByCircularity = True
params.minCircularity = 0.9

# Set Convexity filtering parameters
params.filterByConvexity = False
params.minConvexity = 0.2

# Set inertia filtering parameters
params.filterByInertia = True
params.minInertiaRatio = 0.01

# Create a detector with the parameters
detector = cv2.SimpleBlobDetector_create(params)

# Detect blobs
keypoints = detector.detect(image)

# Draw blobs on our image as green circles with fixed size
blobs = cv2.drawKeypoints(image, keypoints, blank, (0, 255, 0), cv2.DRAW_MATCHES_FLAGS_DEFAULT)

# Display the number of circular blobs
number_of_circular_blobs = len(keypoints)
text = 'Number of Circular Blobs: ' + str(len(keypoints))
cv2.putText(blobs, text, (20, 550), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 100, 255), 2)

# Show blobs
cv2.imshow('Filtering Circular Blobs Only', blobs)
cv2.waitKey(0)
cv2.destroyAllWindows()
