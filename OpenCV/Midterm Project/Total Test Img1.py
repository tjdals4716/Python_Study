# 평균값 필터링 -> 히스토그램 스트레칭 -> 캐니 필터
'''
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
'''



# 평균값 필터링 -> 히스토그램 스트레칭 -> LoG 필터
'''
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
'''



# 평균값 필터링 -> 히스토그램 평활화 -> 캐니 필터
'''
import cv2
import numpy as np

image = cv2.imread('image1.png')

kernel_size = (5, 5)
image_average = cv2.blur(image, kernel_size)
gray = cv2.cvtColor(image_average, cv2.COLOR_BGR2GRAY)
equalization = cv2.equalizeHist(gray)
canny = cv2.Canny(equalization, 100, 200)

cv2.imshow('Original', image)
cv2.imshow('Average Filter', image_average)
cv2.imshow('Histogram Equalization', equalization)
cv2.imshow('Canny Filter', canny)

cv2.waitKey(0)
cv2.destroyAllWindows()
'''



# 평균값 필터링 -> 히스토그램 평활화 -> LoG 필터
'''
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
'''




# 중간값 필터링 -> 히스토그램 스트레칭 -> 캐니 필터

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





# 중간값 필터링 -> 히스토그램 스트레칭 -> LoG 필터

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




# 중간값 필터링 -> 히스토그램 평활화 -> 캐니 필터

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




# 중간값 필터링 -> 히스토그램 평활화 -> LoG 필터

import cv2
import numpy as np

image = cv2.imread('image1.png')

median = cv2.medianBlur(image, 5)
gray = cv2.cvtColor(median, cv2.COLOR_BGR2GRAY)
equalization = cv2.equalizeHist(gray)
log = cv2.Laplacian(equalization, cv2.CV_64F)

cv2.imshow('Original', image)
cv2.imshow('Median Filter', median)
cv2.imshow('Histogram Equalization', equalization)
cv2.imshow('LoG Filter', log)

cv2.waitKey(0)
cv2.destroyAllWindows()





# 가우시안 필터링 -> 히스토그램 스트레칭 -> 캐니 필터
'''
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
'''



# 가우시안 필터링 -> 히스토그램 스트레칭 -> LoG 필터
'''
import cv2
import numpy as np

image = cv2.imread('image1.png')

gaussian = cv2.GaussianBlur(image, (5, 5), 0)
gray = cv2.cvtColor(gaussian, cv2.COLOR_BGR2GRAY)
stretching = cv2.normalize(gray, None, 0, 255, cv2.NORM_MINMAX)
log = cv2.Laplacian(stretching, cv2.CV_64F)

cv2.imshow('Original', image)
cv2.imshow('Gaussian Filter', gaussian)
cv2.imshow('Histogram Stretching', stretching)
cv2.imshow('LoG Filter', log)

cv2.waitKey(0)
cv2.destroyAllWindows()
'''



# 가우시안 필터링 -> 히스토그램 평활화 -> 캐니 필터
'''
import cv2
import numpy as np

image = cv2.imread('image1.png')

gaussian = cv2.GaussianBlur(image, (5, 5), 0)
gray = cv2.cvtColor(gaussian, cv2.COLOR_BGR2GRAY)
equalization = cv2.equalizeHist(gray)
canny = cv2.Canny(equalization, 100, 200)

cv2.imshow('Original', image)
cv2.imshow('Gaussian Filter', gaussian)
cv2.imshow('Histogram Equalization', equalization)
cv2.imshow('Canny  Filter', canny)

cv2.waitKey(0)
cv2.destroyAllWindows()
'''



# 가우시안 필터링 -> 히스토그램 평활화 -> LoG 필터
'''
import cv2
import numpy as np

image = cv2.imread('image1.png')

gaussian = cv2.GaussianBlur(image, (5, 5), 0)
gray = cv2.cvtColor(gaussian, cv2.COLOR_BGR2GRAY)
equalization = cv2.equalizeHist(gray)
log = cv2.Laplacian(equalization, cv2.CV_64F)

cv2.imshow('Original', image)
cv2.imshow('Gaussian Filter', gaussian)
cv2.imshow('Histogram Equalization', equalization)
cv2.imshow('LoG Filter' , log)

cv2.waitKey(0)
cv2.destroyAllWindows()
'''
