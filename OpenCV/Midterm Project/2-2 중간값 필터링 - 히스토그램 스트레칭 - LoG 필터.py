import cv2
import numpy as np

image = cv2.imread('image1.png')

median = cv2.medianBlur(image, 5)
gray = cv2.cvtColor(median, cv2.COLOR_BGR2GRAY)
stretching = cv2.normalize(gray, None, 0, 255, cv2.NORM_MINMAX)
gaussian = cv2.GaussianBlur(stretching, (5, 5), 0)
log = cv2.Laplacian(gaussian, cv2.CV_64F)

cv2.imshow('Original', image)
cv2.imshow('Median Filter', median)
cv2.imshow('Histogram Stretching', stretching)
cv2.imshow('LoG Filter', log)

cv2.waitKey(0)
cv2.destroyAllWindows()
