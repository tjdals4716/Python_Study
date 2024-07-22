import cv2
import numpy as np

# 이미지 읽기
im1 = cv2.imread('4.jpg')
im2 = cv2.imread('7.jpg')

if im1 is None or im2 is None:
    print('이미지 파일을 찾을 수 없거나 읽을 수 없습니다.')
    exit()

# 그레이스케일로 변환
gray1 = cv2.cvtColor(im1, cv2.COLOR_BGR2GRAY)
gray2 = cv2.cvtColor(im2, cv2.COLOR_BGR2GRAY)

# 템플릿 이미지 설정 (im1의 일부분)
template = gray1[100:200, 100:200]  # 예시로 (100, 100) 위치에서 100x100 크기의 템플릿을 선택

# Template Matching 수행
result = cv2.matchTemplate(gray2, template, cv2.TM_CCOEFF_NORMED)
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

# 매칭 결과의 위치와 크기 계산
top_left = max_loc
bottom_right = (top_left[0] + template.shape[1], top_left[1] + template.shape[0])

# 매칭 결과를 직사각형으로 표시
result_image = cv2.cvtColor(gray2, cv2.COLOR_GRAY2BGR)
cv2.rectangle(result_image, top_left, bottom_right, (0, 255, 0), 2)

# 템플릿 이미지를 붉은색 직사각형으로 표시
cv2.rectangle(im1, (100, 100), (200, 200), (0, 0, 255), 2)

# result_image를 im2와 같은 크기로 변환
result_image_resized = cv2.resize(result_image, (im2.shape[1], im2.shape[0]))

# im1을 result_image_resized와 같은 크기로 변환
im1_resized = cv2.resize(im1, (result_image_resized.shape[1], result_image_resized.shape[0]))

# 원본 이미지와 매칭 결과 이미지를 나란히 출력
concatenated_image = cv2.hconcat([im1_resized, result_image_resized])

# 매칭 결과 출력
result_image = cv2.resize(result_image, (600, 300))
cv2.imshow('Template Matching Result', concatenated_image)
cv2.waitKey(0)
cv2.destroyAllWindows()