import cv2
import numpy as np

image = cv2.imread('image1.png')

kernel_size = (5, 5)
average = cv2.blur(image, kernel_size)
gray = cv2.cvtColor(average, cv2.COLOR_BGR2GRAY)
equalization = cv2.equalizeHist(gray)
sigma = 1.0
gaussian = cv2.GaussianBlur(equalization, (0, 0), sigma)
log = cv2.Laplacian(gaussian, cv2.CV_64F)

cv2.imshow('Original', image)
cv2.imshow('Average Filter', average)
cv2.imshow('Histogram Equalization', equalization)
cv2.imshow('LoG Filter', log)

cv2.waitKey(0)
cv2.destroyAllWindows()