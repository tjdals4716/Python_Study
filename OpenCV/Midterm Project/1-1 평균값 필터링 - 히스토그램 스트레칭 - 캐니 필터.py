import cv2
import numpy as np

image = cv2.imread('image1.png')

kernel_size = (5, 5)
average = cv2.blur(image, kernel_size)
gray = cv2.cvtColor(average, cv2.COLOR_BGR2GRAY)
minVal, maxVal, minLoc, maxLoc = cv2.minMaxLoc(gray)
Stretching = cv2.convertScaleAbs(gray, alpha=255/(maxVal-minVal), beta=-minVal*255/(maxVal-minVal))
canny= cv2.Canny(Stretching, 100, 200)

cv2.imshow('Original', image)
cv2.imshow('Average Filter', average)
cv2.imshow('Histogram Stretching', Stretching)
cv2.imshow('Canny Filter', canny)

cv2.waitKey(0)
cv2.destroyAllWindows()