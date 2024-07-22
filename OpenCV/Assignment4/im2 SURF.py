import cv2

im1 = cv2.imread('im2.jpg')
if im1 is None:
    print('이미지 파일을 찾을 수 없거나 읽을 수 없습니다.')
    exit()

gray = cv2.cvtColor(im1, cv2.COLOR_BGR2GRAY)
surf = cv2.xfeatures2d.SURF_create(400)
keypoints = surf.detect(gray, None)
im_with_keypoints = cv2.drawKeypoints(im1, keypoints, None, flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

im_concatenated = cv2.hconcat([im1, im_with_keypoints])
num_keypoints = len(keypoints)
print(f'검출된 특징점 개수 : {num_keypoints}')

cv2.imshow('Original Image and SURF', im_concatenated)
cv2.waitKey(0)
cv2.destroyAllWindows()