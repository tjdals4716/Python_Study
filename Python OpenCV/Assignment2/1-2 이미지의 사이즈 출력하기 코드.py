import cv2 as cv

# 이미지 파일을 읽어옵니다.
img = cv.imread('lena.jpg')

# 이미지가 제대로 읽어졌는지 확인합니다.
if img is None:
    print('이미지를 읽을 수 없습니다.')
    exit()

# 이미지의 높이와 너비를 가져옵니다.
height, width = img.shape[:2]

print(f'이미지의 너비: {width}')
print(f'이미지의 높이: {height}')