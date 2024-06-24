# 교재 2-2 코드
'''
import cv2 as cv 
import sys

# 새 경로에서 이미지 읽기
img = cv.imread('camera.bmp')

if img is None:
    sys.exit('파일을 찾을 수 없습니다.')

cv.imshow('Image Display', img)

cv.waitKey()
cv.destroyAllWindows()
'''



# 교재 2-3 코드
'''
import cv2 as cv 
import sys

img = cv.imread('camera.bmp')

if img is None:
    sys.exit('파일을 찾을 수 없습니다.')

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
gray_small = cv.resize(gray, dsize=(0, 0), fx=0.5, fy=0.5) 

# 파일 확장자 수정
cv.imwrite('soccer_gray.jpg', gray)
cv.imwrite('soccer_gray_small.jpg', gray_small)

cv.imshow('Color image', img)
cv.imshow('Gray image', gray)
cv.imshow('Gray image small', gray_small)

cv.waitKey()
cv.destroyAllWindows()
'''



# 과제1 이미지의 픽셀값 출력하기 코드
'''
import cv2 as cv

# 이미지 파일을 읽어옵니다.
img = cv.imread('camera.bmp')

# 이미지가 제대로 읽어졌는지 확인합니다.
if img is None:
    print('이미지를 읽을 수 없습니다.')
    exit()

# 이미지의 높이와 너비를 가져옵니다.
height, width = img.shape[:2]

# 각 픽셀의 BGR 값을 출력합니다.
for y in range(height):
    for x in range(width):
        pixel = img[y, x]
        print(f'픽셀 좌표: ({x}, {y}), BGR 값: {pixel}')

# 이미지를 화면에 표시합니다.
cv.imshow('Image', img)
cv.waitKey(0)
cv.destroyAllWindows()
'''



# 과제1 이미지의 사이즈 출력하기 코드
'''
import cv2 as cv

# 이미지 파일을 읽어옵니다.
img = cv.imread('lena.jpg')

# 이미지가 제대로 읽어졌는지 확인합니다.
if img is None:
    print('이미지를 읽을 수 없습니다.')
    exit()

# 이미지의 높이와 너비를 가져옵니다.
height, width = img.shape[:2]

print(f'이미지의 너비: {width}')
print(f'이미지의 높이: {height}')
'''



# 과제 1-1 코드
'''
import cv2 as cv

# 이미지 파일 읽기
img = cv.imread('girl.jpg')

# 이미지가 제대로 읽어졌는지 확인하는 부분
if img is None:
    print('이미지를 읽을 수 없습니다')
    exit()

# 이미지의 높이와 너비를 가져옴
height, width = img.shape[:2]

# 각 채널별 이미지 생성
blue_channel = img[:, :, 0]
green_channel = img[:, :, 1]
red_channel = img[:, :, 2]

# 각 채널별 화소값 출력
print("Red 채널 화소값 : ")
for y in range(height):
    for x in range(width):
        pixel_value = red_channel[y, x]
        print(f'픽셀 좌표 : ({x}, {y}), Red 화소값 : {pixel_value}')

print("\nGreen 채널 화소값 : ")
for y in range(height):
    for x in range(width):
        pixel_value = green_channel[y, x]
        print(f'픽셀 좌표 : ({x}, {y}), Green 화소값 : {pixel_value}')

print("\nBlue 채널 화소값 : ")
for y in range(height):
    for x in range(width):
        pixel_value = blue_channel[y, x]
        print(f'픽셀 좌표 : ({x}, {y}), Blue 화소값 : {pixel_value}')

# 이미지와 각 채널별 이미지를 화면에 표시
cv.imshow("image", img)
cv.imshow("blue", blue_channel)
cv.imshow("green", green_channel)
cv.imshow("red", red_channel)
cv.waitKey(0)
cv.destroyAllWindows()
'''



# 과제 1-2 코드 (RGB 이미지 HSV 이미지로 변환 코드)
'''
import cv2 as cv

# 이미지 파일 읽기
img = cv.imread('camera.bmp')

# 이미지가 제대로 읽어졌는지 확인
if img is None:
    print('이미지를 읽을 수 없습니다')
    exit()

# RGB 이미지를 HSV 모델로 변환
hsv_image = cv.cvtColor(img, cv.COLOR_BGR2HSV)

# 이미지의 높이와 너비를 가져옴
height, width = hsv_image.shape[:2]

# 각 채널별 화소값 출력
print("HSV 이미지의 각 채널별 화소값 : ")
for y in range(height):
    for x in range(width):
        pixel_value = hsv_image[y, x]
        print(f'픽셀 좌표 : ({x}, {y}), H : {pixel_value[0]}, S : {pixel_value[1]}, V : {pixel_value[2]}')

# HSV 이미지를 화면에 표시
cv.imshow('HSV Image', hsv_image)
cv.waitKey(0)
cv.destroyAllWindows()
'''



# 교재 1-3 코드
'''
import cv2 as cv

# 이미지 파일을 그레이스케일로 읽어옴
img_gray = cv.imread('airplane.bmp', cv.IMREAD_GRAYSCALE)

# 이미지가 제대로 읽어졌는지 확인
if img_gray is None:
    print('이미지를 읽을 수 없습니다')
    exit()

# 이미지의 높이와 너비를 가져옴
height, width = img_gray.shape[:2]

# 각 픽셀의 그레이스케일 화소값을 출력
print("Gray scale 이미지의 화소값 : ")
for y in range(height):
    for x in range(width):
        pixel_value = img_gray[y, x]
        print(f'픽셀 좌표 : ({x}, {y}), 화소값 : {pixel_value}')

# 이미지를 화면에 표시
cv.imshow('Grayscale Image', img_gray)
cv.waitKey(0)
cv.destroyAllWindows()
'''



# 과제 2-1 코드
'''
import cv2 as cv

# 첫 번째 이미지 읽기
img1 = cv.imread('lena.jpg')

# 두 번째 이미지 읽기
img2 = cv.imread('butterfly.bmp')

# 이미지가 제대로 읽어졌는지 확인
if img1 is None or img2 is None:
    print('이미지를 읽을 수 없습니다')
    exit()

# 이미지 사이즈 맞추기
img2 = cv.resize(img2, (img1.shape[1], img1.shape[0]))

# 이미지를 그레이스케일로 변환
img1_gray = cv.cvtColor(img1, cv.COLOR_BGR2GRAY)
img2_gray = cv.cvtColor(img2, cv.COLOR_BGR2GRAY)

# 비트 AND, OR, XOR 연산 수행
result_and = cv.bitwise_and(img1_gray, img2_gray)
result_or = cv.bitwise_or(img1_gray, img2_gray)
result_xor = cv.bitwise_xor(img1_gray, img2_gray)

# 결과 이미지 출력
cv.imshow('AND : ', result_and)
cv.imshow('OR : ', result_or)
cv.imshow('XOR : ', result_xor)

# 이미지를 화면에 표시
cv.imshow('Image1', img1)
cv.imshow('Image2', img2)
cv.waitKey(0)
cv.destroyAllWindows()
'''



# 과제 3 코드
'''
import cv2 as cv

# 첫 번째 이미지 읽기
lena_rgb = cv.imread('lena.jpg')

# 두 번째 이미지 읽기
mandrill_rgb = cv.imread('mandrill.jpg')

# 이미지가 제대로 읽어졌는지 확인
if lena_rgb is None or mandrill_rgb is None:
    print('이미지를 읽을 수 없습니다')
    exit()

# RGB 이미지를 Gray scale로 변환
lena_gray = cv.cvtColor(lena_rgb, cv.COLOR_BGR2GRAY)
mandrill_gray = cv.cvtColor(mandrill_rgb, cv.COLOR_BGR2GRAY)

# 이미지 출력
cv.imshow('Lena RGB', lena_rgb)
cv.imshow('Lena Gray', lena_gray)

cv.imshow('Mandrill RGB', mandrill_rgb)
cv.imshow('Mandrill Gray', mandrill_gray)

cv.waitKey(0)
cv.destroyAllWindows()
'''




# 과제 3-1 코드 (전역 임계값 적용)
'''
import cv2 as cv

# 이미지 파일 읽기
lena_img = cv.imread('lena.jpg')
mandrill_img = cv.imread('mandrill.jpg')

# 이미지가 제대로 읽어졌는지 확인
if lena_img is None or mandrill_img is None:
    print('이미지를 읽을 수 없습니다')
    exit()

# 이미지를 그레이스케일로 변환
lena_gray = cv.cvtColor(lena_img, cv.COLOR_BGR2GRAY)
mandrill_gray = cv.cvtColor(mandrill_img, cv.COLOR_BGR2GRAY)

# 전역 임계값 적용
_, lena_thresh = cv.threshold(lena_gray, 127, 255, cv.THRESH_BINARY)
_, mandrill_thresh = cv.threshold(mandrill_gray, 127, 255, cv.THRESH_BINARY)

# 객체 분할 결과 표시
cv.imshow('Lena Threshold', lena_thresh)
cv.imshow('Mandrill Threshold', mandrill_thresh)

# 원본 이미지도 표시
cv.imshow('Lena Original', lena_img)
cv.imshow('Mandrill Original', mandrill_img)

# 이미지를 화면에 표시
cv.waitKey(0)
cv.destroyAllWindows()
'''




# 과제 3-2 코드 (적응적 임계값 적용)
'''
import cv2 as cv

# 이미지 파일 읽기
img1 = cv.imread('lena.jpg')
img2 = cv.imread('mandrill.jpg')

# 이미지가 제대로 읽어졌는지 확인
if img1 is None or img2 is None:
    print('이미지를 읽을 수 없습니다')
    exit()

# 이미지를 그레이스케일로 변환
gray_img1 = cv.cvtColor(img1, cv.COLOR_BGR2GRAY)
gray_img2 = cv.cvtColor(img2, cv.COLOR_BGR2GRAY)

# 적응적 임계값 적용
adaptive_thresh1 = cv.adaptiveThreshold(gray_img1, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 11, 2)
adaptive_thresh2 = cv.adaptiveThreshold(gray_img2, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 11, 2)

# 객체 분할 결과 표시
cv.imshow('Adaptive Threshold Lena', adaptive_thresh1)
cv.imshow('Adaptive Threshold Mandrill', adaptive_thresh2)

cv.imshow('Lena Original', img1)
cv.imshow('Mandrill Original', img2)

# 이미지를 화면에 표시
cv.waitKey(0)
cv.destroyAllWindows()
'''



# 과제 4-1 코드 (히스토그램 스트레칭)

import cv2 as cv
import numpy as np

# 이미지 파일 읽기
lena_img = cv.imread('lena.jpg')
mandrill_img = cv.imread('mandrill.jpg')

# 이미지가 제대로 읽어졌는지 확인
if lena_img is None or mandrill_img is None:
    print('이미지를 읽을 수 없습니다')
    exit()

# 그레이스케일로 변환
lena_gray = cv.cvtColor(lena_img, cv.COLOR_BGR2GRAY)
mandrill_gray = cv.cvtColor(mandrill_img, cv.COLOR_BGR2GRAY)

# 히스토그램 스트레칭 적용 전 그레이스케일 이미지
cv.imshow('Lena', lena_gray)
cv.imshow('Mandrill', mandrill_gray)

# 히스토그램 스트레칭 함수 정의
def histogram_stretching(img):
    # 최솟값과 최댓값 계산
    min_val = np.min(img)
    max_val = np.max(img)
    
    # 히스토그램 스트레칭 적용
    stretched_img = ((img - min_val) / (max_val - min_val) * 255).astype(np.uint8)
    
    return stretched_img

# 히스토그램 스트레칭 적용
lena_stretched = histogram_stretching(lena_gray)
mandrill_stretched = histogram_stretching(mandrill_gray)

# 히스토그램 스트레칭 적용 후 그레이스케일 이미지
cv.imshow('Stretching Lena', lena_stretched)
cv.imshow('Stretching Mandrill', mandrill_stretched)

# 이미지를 화면에 표시
cv.waitKey(0)
cv.destroyAllWindows()




# 과제 4-2 코드 (히스토그램 평활화)

import cv2 as cv

# 이미지 파일 읽기
img1 = cv.imread('lena.jpg')
img2 = cv.imread('mandrill.jpg')

# 이미지가 제대로 읽어졌는지 확인
if img1 is None or img2 is None:
    print('이미지를 읽을 수 없습니다')
    exit()

# 이미지를 그레이스케일로 변환
gray_img1 = cv.cvtColor(img1, cv.COLOR_BGR2GRAY)
gray_img2 = cv.cvtColor(img2, cv.COLOR_BGR2GRAY)

# 히스토그램 평활화 적용
equalized_img1 = cv.equalizeHist(gray_img1)
equalized_img2 = cv.equalizeHist(gray_img2)

# 히스토그램 평활화 적용 전 이미지 표시
cv.imshow('Lena', gray_img1)
cv.imshow('Mandrill', gray_img2)

# 히스토그램 평활화 적용 후 이미지 표시
cv.imshow('Equalized Lena', equalized_img1)
cv.imshow('Equalized Mandrill', equalized_img2)

# 이미지를 화면에 표시
cv.waitKey(0)
cv.destroyAllWindows()
