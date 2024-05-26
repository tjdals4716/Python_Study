import cv2 as cv

# 이미지 파일을 읽어옵니다.
img = cv.imread('camera.bmp')

# 이미지가 제대로 읽어졌는지 확인합니다.
if img is None:
    print('이미지를 읽을 수 없습니다.')
    exit()

# 이미지의 높이와 너비를 가져옵니다.
height, width = img.shape[:2]

# 각 픽셀의 BGR 값을 출력합니다.
for y in range(height):
    for x in range(width):
        pixel = img[y, x]
        print(f'픽셀 좌표: ({x}, {y}), BGR 값: {pixel}')

# 이미지를 화면에 표시합니다.
cv.imshow('Image', img)
cv.waitKey(0)
cv.destroyAllWindows()