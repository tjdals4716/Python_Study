import cv2

# 이미지 읽기
im1 = cv2.imread('im1.jpg')

if im1 is None:
    print('이미지 파일을 찾을 수 없거나 읽을 수 없습니다.')
    exit()

# 그레이스케일로 변환
gray = cv2.cvtColor(im1, cv2.COLOR_BGR2GRAY)

# SURF 객체 생성
surf = cv2.xfeatures2d.SURF_create(400)

# 특징점 검출
keypoints = surf.detect(gray, None)

# 특징점 그리기
im_with_keypoints = cv2.drawKeypoints(im1, keypoints, None, flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

# 원본 이미지와 특징점이 그려진 이미지를 나란히 출력
im_concatenated = cv2.hconcat([im1, im_with_keypoints])

# 특징점 개수 출력
num_keypoints = len(keypoints)
print(f'검출된 특징점 개수 : {num_keypoints}')

# 결과 이미지 출력
cv2.imshow('Original Image and SURF', im_concatenated)
cv2.waitKey(0)
cv2.destroyAllWindows()