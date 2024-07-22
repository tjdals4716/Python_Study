import cv2
import numpy as np
import matplotlib.pyplot as plt

# 1. 이미지를 불러옵니다.
img1 = cv2.imread('web1-1.png', cv2.IMREAD_GRAYSCALE)
img2 = cv2.imread('web1-2.png', cv2.IMREAD_GRAYSCALE)

# 2. ORB 특징점을 검출하고 디스크립터를 계산합니다.
orb = cv2.ORB_create()

kp1, des1 = orb.detectAndCompute(img1, None)
kp2, des2 = orb.detectAndCompute(img2, None)

# 3. BFMatcher를 사용하여 특징점을 매칭합니다. (Brute Force Matcher)
bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
matches = bf.match(des1, des2)

# 매칭된 점들을 거리 기준으로 정렬합니다.
matches = sorted(matches, key=lambda x: x.distance)

# 최상위 매칭된 점들을 시각화하여 그립니다.
img_matches = cv2.drawMatches(img1, kp1, img2, kp2, matches[:50], None, flags=cv2.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)

plt.figure(figsize=(15, 5))
plt.imshow(img_matches)
plt.title('상위 50개의 특징점 매칭')
plt.show()

# 4. 좋은 매칭된 점들의 위치를 추출합니다.
pts1 = np.float32([kp1[m.queryIdx].pt for m in matches]).reshape(-1, 1, 2)
pts2 = np.float32([kp2[m.trainIdx].pt for m in matches]).reshape(-1, 1, 2)

# 5. Fundamental Matrix를 찾습니다.
F, mask = cv2.findFundamentalMat(pts1, pts2, cv2.FM_RANSAC)

# 인라이어(유효한 매칭 점)만 선택합니다.
pts1_inliers = pts1[mask.ravel() == 1]
pts2_inliers = pts2[mask.ravel() == 1]

# Fundamental Matrix를 출력합니다.
print("Fundamental Matrix (F):\n", F)

# 인라이어 매칭을 시각화합니다.
inlier_matches = [matches[i] for i in range(len(matches)) if mask[i]]
img_inlier_matches = cv2.drawMatches(img1, kp1, img2, kp2, inlier_matches, None, flags=cv2.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)

plt.figure(figsize=(15, 5))
plt.imshow(img_inlier_matches)
plt.title('RANSAC 후 인라이어 매칭')
plt.show()
