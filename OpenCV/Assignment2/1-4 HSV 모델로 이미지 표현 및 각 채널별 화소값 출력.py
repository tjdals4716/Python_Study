import cv2 as cv

# 이미지 파일 읽기
img = cv.imread('camera.bmp')

# 이미지가 제대로 읽어졌는지 확인
if img is None:
    print('이미지를 읽을 수 없습니다')
    exit()

# RGB 이미지를 HSV 모델로 변환
hsv_image = cv.cvtColor(img, cv.COLOR_BGR2HSV)

# 이미지의 높이와 너비를 가져옴
height, width = hsv_image.shape[:2]

# 각 채널별 화소값 출력
print("HSV 이미지의 각 채널별 화소값 : ")
for y in range(height):
    for x in range(width):
        pixel_value = hsv_image[y, x]
        print(f'픽셀 좌표 : ({x}, {y}), H : {pixel_value[0]}, S : {pixel_value[1]}, V : {pixel_value[2]}')

# HSV 이미지를 화면에 표시
cv.imshow('HSV Image', hsv_image)
cv.waitKey(0)
cv.destroyAllWindows()