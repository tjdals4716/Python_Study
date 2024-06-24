import cv2
import numpy as np
import matplotlib.pyplot as plt

# 이미지를 읽어옵니다.
image = cv2.imread('MSD1-1.png', cv2.IMREAD_GRAYSCALE)

# 원본 이미지 시각화
plt.subplot(1, 3, 1)
plt.title('Original Image')
plt.imshow(image, cmap='gray')

# 이진 임계값 적용
_, binary_image = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)

# 이진 임계값 이미지 시각화
plt.subplot(1, 3, 2)
plt.title('Binary Image')
plt.imshow(binary_image, cmap='gray')

# 이진 임계값을 이용한 심도 맵 추정
depth_map = cv2.Canny(binary_image, 100, 200)

# 심도 맵 시각화
plt.subplot(1, 3, 3)
plt.title('Depth Map')
plt.imshow(depth_map, cmap='jet')
plt.colorbar()

plt.show()
