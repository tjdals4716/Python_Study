import cv2
import numpy as np
import matplotlib.pyplot as plt

# 한 쌍의 이미지 가져오기
img1 = cv2.imread('12-1.jpg', cv2.IMREAD_GRAYSCALE)
img2 = cv2.imread('12-2.jpg', cv2.IMREAD_GRAYSCALE)

# SIFT 알고리즘으로 특징 생성
sift = cv2.SIFT_create()

# 특징점과 디스크립터 추출
keypoints1, descriptors1 = sift.detectAndCompute(img1, None)
keypoints2, descriptors2 = sift.detectAndCompute(img2, None)

# BFMatcher를 사용하여 특징점 매칭
bf = cv2.BFMatcher(cv2.NORM_L2, crossCheck=True)
matches = bf.match(descriptors1, descriptors2)

# 거리가 가까운 것부터 매칭 결과를 정렬
matches = sorted(matches, key=lambda x: x.distance)

# 상위 매칭된 점들을 선택
num_matches_to_draw = 50
matches = matches[:num_matches_to_draw]

# 매칭된 점들을 가져오기
pts1 = np.float32([keypoints1[m.queryIdx].pt for m in matches])
pts2 = np.float32([keypoints2[m.trainIdx].pt for m in matches])

# RANSAC을 사용하여 Fundamental Matrix 계산
F, mask = cv2.findFundamentalMat(pts1, pts2, cv2.FM_RANSAC)

# 매칭된 점들 중 마스크된 점들만 선택
pts1_inliers = pts1[mask.ravel() == 1]
pts2_inliers = pts2[mask.ravel() == 1]

# 결과 출력
print("RANSAC을 이용한 Fundamental Matrix 3 x 3 행렬 : \n", F)

# 매칭된 점들을 그리기 위해 마스크된 점들만으로 이미지 준비
matches_masked = [m for m, msk in zip(matches, mask) if msk == 1]
img_matches = cv2.drawMatches(img1, keypoints1, img2, keypoints2, matches_masked, None, flags=cv2.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)

# 크기에 맞도록 이미지를 조절하여 표시
plt.figure(figsize=(10, 5))
plt.imshow(img_matches)
plt.title("제일 잘 나온 50개의 인라이너 특징점 매칭")
plt.show()

# 에피폴라 선 그리기 추가 (그냥 해봄)
def draw_epipolar_lines(img1, img2, pts1, pts2, F):
    def draw_lines(img, lines, pts):
        r, c = img.shape
        img = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
        for r, pt1 in zip(lines, pts):
            color = tuple(np.random.randint(0, 255, 3).tolist())
            x0, y0 = map(int, [0, -r[2] / r[1]])
            x1, y1 = map(int, [c, -(r[2] + r[0] * c) / r[1]])
            img = cv2.line(img, (x0, y0), (x1, y1), color, 1)
            # 좌표를 정수로 변환하여 circle 함수에 전달
            pt1 = tuple(map(int, pt1))
            img = cv2.circle(img, pt1, 5, color, -1)
        return img

    lines1 = cv2.computeCorrespondEpilines(pts2.reshape(-1, 1, 2), 2, F)
    lines1 = lines1.reshape(-1, 3)
    img1_with_lines = draw_lines(img1, lines1, pts1)

    lines2 = cv2.computeCorrespondEpilines(pts1.reshape(-1, 1, 2), 1, F)
    lines2 = lines2.reshape(-1, 3)
    img2_with_lines = draw_lines(img2, lines2, pts2)

    return img1_with_lines, img2_with_lines

# 에피폴라 선 그리기
img1_with_epilines, img2_with_epilines = draw_epipolar_lines(img1, img2, pts1_inliers, pts2_inliers, F)

# 이미지 표시
plt.figure(figsize=(10, 5))
plt.subplot(121)
plt.imshow(img1_with_epilines)
plt.title("Epilines Image 1")
plt.subplot(122)
plt.imshow(img2_with_epilines)
plt.title("Epilines Image 2")
plt.show()
