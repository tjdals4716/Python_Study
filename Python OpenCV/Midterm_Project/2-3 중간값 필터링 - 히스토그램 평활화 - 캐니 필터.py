import cv2
import numpy as np

image = cv2.imread('image1.png')

median = cv2.medianBlur(image, 5)
gray = cv2.cvtColor(median, cv2.COLOR_BGR2GRAY)
equalization = cv2.equalizeHist(gray)
canny = cv2.Canny(equalization, 100, 200)

cv2.imshow('Original', image)
cv2.imshow('Median Filter', median)
cv2.imshow('Histogram Equalization', equalization)
cv2.imshow('Canny Filter', canny)

cv2.waitKey(0)
cv2.destroyAllWindows()