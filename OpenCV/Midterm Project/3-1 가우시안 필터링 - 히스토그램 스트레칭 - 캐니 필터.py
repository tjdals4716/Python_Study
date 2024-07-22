import cv2
import numpy as np

image = cv2.imread('image1.png')

gaussian = cv2.GaussianBlur(image, (5, 5), 0)
gray = cv2.cvtColor(gaussian, cv2.COLOR_BGR2GRAY)
stretching = cv2.normalize(gray, None, alpha=0, beta=255, norm_type=cv2.NORM_MINMAX)
canny = cv2.Canny(stretching, 100, 200)

cv2.imshow('Original', image)
cv2.imshow('Gaussian Filter', gaussian)
cv2.imshow('Histogram Stretching', stretching)
cv2.imshow('Canny Filter', canny)

cv2.waitKey(0)
cv2.destroyAllWindows()