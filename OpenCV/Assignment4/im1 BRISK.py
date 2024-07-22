import cv2

im1 = cv2.imread('im1.jpg')
if im1 is None:
    print('이미지 파일을 찾을 수 없거나 읽을 수 없습니다.')
    exit()

gray = cv2.cvtColor(im1, cv2.COLOR_BGR2GRAY)
brisk = cv2.BRISK_create()
keypoints_brisk = brisk.detect(gray, None)
im_with_keypoints_brisk = cv2.drawKeypoints(im1, keypoints_brisk, None, flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

im_concatenated_brisk = cv2.hconcat([im1, im_with_keypoints_brisk])
num_keypoints_brisk = len(keypoints_brisk)
print(f'BRISK로 검출된 특징점 개수 : {num_keypoints_brisk}')

cv2.imshow('Original Image and BRISK', im_concatenated_brisk)
cv2.waitKey(0)
cv2.destroyAllWindows()