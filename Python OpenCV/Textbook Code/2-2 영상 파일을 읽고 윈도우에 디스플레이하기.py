# 교재 2-2 코드

import cv2 as cv 
import sys

# 새 경로에서 이미지 읽기
img = cv.imread('camera.bmp')

if img is None:
    sys.exit('파일을 찾을 수 없습니다.')

cv.imshow('Image Display', img)

cv.waitKey()
cv.destroyAllWindows()