import cv2 as cv

# 이미지 파일 읽기
img = cv.imread('girl.jpg')

# 이미지가 제대로 읽어졌는지 확인하는 부분
if img is None:
    print('이미지를 읽을 수 없습니다')
    exit()

# 이미지의 높이와 너비를 가져옴
height, width = img.shape[:2]

# 각 채널별 이미지 생성
blue_channel = img[:, :, 0]
green_channel = img[:, :, 1]
red_channel = img[:, :, 2]

# 각 채널별 화소값 출력
print("Red 채널 화소값 : ")
for y in range(height):
    for x in range(width):
        pixel_value = red_channel[y, x]
        print(f'픽셀 좌표 : ({x}, {y}), Red 화소값 : {pixel_value}')

print("\nGreen 채널 화소값 : ")
for y in range(height):
    for x in range(width):
        pixel_value = green_channel[y, x]
        print(f'픽셀 좌표 : ({x}, {y}), Green 화소값 : {pixel_value}')

print("\nBlue 채널 화소값 : ")
for y in range(height):
    for x in range(width):
        pixel_value = blue_channel[y, x]
        print(f'픽셀 좌표 : ({x}, {y}), Blue 화소값 : {pixel_value}')

# 이미지와 각 채널별 이미지를 화면에 표시
cv.imshow("image", img)
cv.imshow("blue", blue_channel)
cv.imshow("green", green_channel)
cv.imshow("red", red_channel)
cv.waitKey(0)
cv.destroyAllWindows()