import cv2
import numpy as np

# 이미지 읽기
im1 = cv2.imread('web3-1.png')
im2 = cv2.imread('web3-2.png')

if im1 is None or im2 is None:
    print('이미지 파일을 찾을 수 없거나 읽을 수 없습니다.')
    exit()

# 그레이스케일로 변환
gray1 = cv2.cvtColor(im1, cv2.COLOR_BGR2GRAY)
gray2 = cv2.cvtColor(im2, cv2.COLOR_BGR2GRAY)

# SIFT 객체 생성
sift = cv2.SIFT_create()

# 특징점 검출 및 기술자 계산
keypoints1, descriptors1 = sift.detectAndCompute(gray1, None)
keypoints2, descriptors2 = sift.detectAndCompute(gray2, None)

# FLANN 매칭 객체 생성
flann_index_kdtree = 1
index_params = dict(algorithm=flann_index_kdtree, trees=5)
search_params = dict(checks=50)
flann = cv2.FlannBasedMatcher(index_params, search_params)

# 특징점 매칭
matches = flann.knnMatch(descriptors1, descriptors2, k=2)

# 좋은 매칭 결과 선별
good_matches = []
for m, n in matches:
    if m.distance < 0.7 * n.distance:
        good_matches.append(m)

# RANSAC을 사용하여 호모그래피 계산
src_pts = np.float32([keypoints1[m.queryIdx].pt for m in good_matches]).reshape(-1, 1, 2)
dst_pts = np.float32([keypoints2[m.trainIdx].pt for m in good_matches]).reshape(-1, 1, 2)
M, mask = cv2.findHomography(src_pts, dst_pts, cv2.RANSAC, 5.0)
matchesMask = mask.ravel().tolist()

# RANSAC으로 선별된 인라이어 매칭 결과
inliers = [m for i, m in enumerate(good_matches) if matchesMask[i]]

# 매칭 결과 그리기
draw_params = dict(matchColor=(0, 255, 0), singlePointColor=None, flags=2)
result_image = cv2.drawMatches(im1, keypoints1, im2, keypoints2, inliers, None, **draw_params)

# 매칭 결과 출력
result_image = cv2.resize(result_image, (600, 300))
cv2.imshow('RANSAC Result', result_image)
cv2.waitKey(0)
cv2.destroyAllWindows()