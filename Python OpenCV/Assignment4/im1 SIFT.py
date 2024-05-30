import cv2

# 이미지 읽기
im1 = cv2.imread('im1.jpg')

if im1 is None:
    print('이미지 파일을 찾을 수 없거나 읽을 수 없습니다.')
    exit()

# 그레이스케일로 변환
gray = cv2.cvtColor(im1, cv2.COLOR_BGR2GRAY)

# SIFT 객체 생성
sift = cv2.SIFT_create()

# 특징점 검출 및 기술자 계산
keypoints, descriptors = sift.detectAndCompute(gray, None)

# 특징점 그리기
im_with_keypoints = cv2.drawKeypoints(im1, keypoints, None, flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

# im_concatenated 메서드는 원본 이미지와 특징점이 그려진 이미지를 보기 편하게 나란히 출력하게 함
im_concatenated = cv2.hconcat([im1, im_with_keypoints])

# 특징점 개수 및 기술자 크기 출력
num_keypoints = len(keypoints)
descriptor_size = descriptors.shape[1]
print(f'검출된 특징점 개수 : {num_keypoints}')

# 결과 이미지 출력
cv2.imshow('Original Image and SIFT', im_concatenated)
cv2.waitKey(0)
cv2.destroyAllWindows()