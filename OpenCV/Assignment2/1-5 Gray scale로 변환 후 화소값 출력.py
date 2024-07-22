import cv2 as cv

# 이미지 파일을 그레이스케일로 읽어옴
img_gray = cv.imread('airplane.bmp', cv.IMREAD_GRAYSCALE)

# 이미지가 제대로 읽어졌는지 확인
if img_gray is None:
    print('이미지를 읽을 수 없습니다')
    exit()

# 이미지의 높이와 너비를 가져옴
height, width = img_gray.shape[:2]

# 각 픽셀의 그레이스케일 화소값을 출력
print("Gray scale 이미지의 화소값 : ")
for y in range(height):
    for x in range(width):
        pixel_value = img_gray[y, x]
        print(f'픽셀 좌표 : ({x}, {y}), 화소값 : {pixel_value}')

# 이미지를 화면에 표시
cv.imshow('Grayscale Image', img_gray)
cv.waitKey(0)
cv.destroyAllWindows()