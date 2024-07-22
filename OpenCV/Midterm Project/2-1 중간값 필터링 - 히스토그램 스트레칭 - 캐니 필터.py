import cv2
import numpy as np

image = cv2.imread('image1.png')

median = cv2.medianBlur(image, 5)
gray = cv2.cvtColor(median, cv2.COLOR_BGR2GRAY)
minVal, maxVal, minLoc, maxLoc = cv2.minMaxLoc(gray)
stretching = cv2.convertScaleAbs(gray, alpha=255/(maxVal-minVal), beta=-minVal*255/(maxVal-minVal))
canny = cv2.Canny(stretching, 100, 200)

cv2.imshow('Original', image)
cv2.imshow('Median Filter', median)
cv2.imshow('Histogram Stretching', stretching)
cv2.imshow('Canny Filter', canny)

cv2.waitKey(0)
cv2.destroyAllWindows()