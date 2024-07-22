import cv2
import numpy as np
import matplotlib.pyplot as plt

# 이미지 불러오기
img_left = cv2.imread('MSD9-1.png', cv2.IMREAD_GRAYSCALE)
img_right = cv2.imread('MSD9-2.png', cv2.IMREAD_GRAYSCALE)

# 이미지 크기 확인 및 일치시키기
if img_left.shape != img_right.shape:
    height, width = min(img_left.shape[0], img_right.shape[0]), min(img_left.shape[1], img_right.shape[1])
    img_left = cv2.resize(img_left, (width, height))
    img_right = cv2.resize(img_right, (width, height))

# 입력 이미지 전처리: 가우시안 블러 적용
img_left_blur = cv2.GaussianBlur(img_left, (5, 5), 0)
img_right_blur = cv2.GaussianBlur(img_right, (5, 5), 0)

# 블록 매칭을 위한 파라미터 설정
block_size = 11  # 블록 크기를 줄임
min_disp = 0     # 최소 시차
num_disp = 128   # 최대 시차 - 최소 시차 (디스패리티 범위 확대)

# StereoBM 객체 생성 및 파라미터 설정
stereo = cv2.StereoBM_create(numDisparities=num_disp, blockSize=block_size)
stereo.setMinDisparity(min_disp)
stereo.setNumDisparities(num_disp)
stereo.setBlockSize(block_size)
stereo.setSpeckleRange(16)
stereo.setSpeckleWindowSize(100)

# 시차 맵 계산
disparity = stereo.compute(img_left_blur, img_right_blur).astype(np.float32) / 16.0

# 시차 맵을 보기 좋게 조정 (시각화를 위해)
disparity_scaled = cv2.normalize(disparity, None, alpha=0, beta=255, norm_type=cv2.NORM_MINMAX)
disparity_scaled = np.uint8(disparity_scaled)

# 결과 시각화
plt.figure(figsize=(10, 5))
plt.subplot(1, 3, 1)
plt.title('Left Image')
plt.imshow(img_left, cmap='gray')
plt.subplot(1, 3, 2)
plt.title('Right Image')
plt.imshow(img_right, cmap='gray')
plt.subplot(1, 3, 3)
plt.title('BM Depth Map')
plt.imshow(disparity_scaled, cmap='jet')
plt.colorbar()
plt.show()
