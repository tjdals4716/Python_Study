import cv2

im1 = cv2.imread('im2.jpg')
if im1 is None:
    print('이미지 파일을 찾을 수 없거나 읽을 수 없습니다.')
    exit()

gray = cv2.cvtColor(im1, cv2.COLOR_BGR2GRAY)
orb = cv2.ORB_create()
keypoints_orb = orb.detect(gray, None)
im_with_keypoints_orb = cv2.drawKeypoints(im1, keypoints_orb, None, flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

im_concatenated_orb = cv2.hconcat([im1, im_with_keypoints_orb])
num_keypoints_orb = len(keypoints_orb)
print(f'ORB로 검출된 특징점 개수 : {num_keypoints_orb}')

cv2.imshow('Original Image and ORB', im_concatenated_orb)
cv2.waitKey(0)
cv2.destroyAllWindows()