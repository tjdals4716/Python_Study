import cv2
import numpy as np

image = cv2.imread('image1.png')

kernel_size = (5, 5)
average = cv2.blur(image, kernel_size)
gray = cv2.cvtColor(average, cv2.COLOR_BGR2GRAY)
minVal, maxVal, minLoc, maxLoc = cv2.minMaxLoc(gray)
stretching = cv2.convertScaleAbs(gray, alpha=255/(maxVal-minVal), beta=-minVal*255/(maxVal-minVal))
sigma = 1.0
gaussian = cv2.GaussianBlur(stretching, (0, 0), sigma)
log = cv2.Laplacian(gaussian, cv2.CV_64F)

cv2.imshow('Original', image)
cv2.imshow('Average Filter', average)
cv2.imshow('Histogram Stretching', stretching)
cv2.imshow('LoG Filter', log)

cv2.waitKey(0)
cv2.destroyAllWindows()