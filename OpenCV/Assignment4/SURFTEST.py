import cv2

# 이미지 불러오기
photo01 = cv2.imread("im3.jpg")
photo02 = cv2.imread("im3.jpg")

if photo01 is None or photo02 is None:
    print('이미지 파일을 찾을 수 없거나 읽을 수 없습니다.')
    exit()

# SURF 알고리즘 객체 생성
feature = cv2.xfeatures2d.SURF_create(400)

# 각 이미지에서 키포인트 추출
keyPoint01, descriptors01 = feature.detectAndCompute(photo01, None)
keyPoint02, descriptors02 = feature.detectAndCompute(photo02, None)

# Brute-force 방식으로 매칭
matcher = cv2.BFMatcher(cv2.NORM_L1, True)
matches = matcher.match(descriptors01, descriptors02)

# 키포인트 및 매칭 결과를 이미지에 그리기
keyPointImage01 = cv2.drawKeypoints(photo01, keyPoint01, None, None, cv2.DRAW_MATCHES_FLAGS_DEFAULT)
keyPointImage02 = cv2.drawKeypoints(photo02, keyPoint02, None, None, cv2.DRAW_MATCHES_FLAGS_DEFAULT)
matchImage = cv2.drawMatches(photo01, keyPoint01, photo02, keyPoint02, matches, None)

# 원본 이미지와 키포인트 이미지를 나란히 결합
original_and_keypoints_1 = cv2.hconcat([photo01, keyPointImage01])
original_and_keypoints_2 = cv2.hconcat([photo02, keyPointImage02])

# 결과 이미지 출력
cv2.imshow("Image 1", original_and_keypoints_1)
cv2.imshow("Image 2", original_and_keypoints_2)
cv2.imshow("Image matching", matchImage)

# 특징점 개수 출력
num_keypoints = len(keyPoint01)
print(f'SURF로 검출된 특징점 개수 : {num_keypoints}')

cv2.waitKey(0)
cv2.destroyAllWindows()
