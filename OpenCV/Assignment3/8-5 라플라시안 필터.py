import cv2 as cv

# Copy of Lena-Gaussian-noise.jpg 이미지 읽기
lena_gaussian_noise_img = cv.imread('img3.jpg')

# salt pepper noise.bmp 이미지 읽기
salt_pepper_noise_img = cv.imread('salt pepper noise.bmp')

# 두 이미지가 제대로 읽혔는지 확인
if lena_gaussian_noise_img is None or salt_pepper_noise_img is None:
    print('이미지를 읽을 수 없습니다')
    exit()

# 라플라시안 필터 적용 함수 정의
def apply_laplacian_filter(img):
    # 그레이스케일 변환
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    # 라플라시안 필터 적용
    laplacian = cv.Laplacian(gray, cv.CV_64F)
    # 결과 이미지 정규화
    laplacian = cv.normalize(laplacian, None, 0, 255, cv.NORM_MINMAX, cv.CV_8U)
    return laplacian

# 라플라시안 필터 적용
lena_gaussian_noise_filtered = apply_laplacian_filter(lena_gaussian_noise_img)
salt_pepper_noise_filtered = apply_laplacian_filter(salt_pepper_noise_img)

# 결과 이미지 표시
cv.imshow('Laplacian Filtered Lena Gaussian Noise', lena_gaussian_noise_filtered)
cv.imshow('Laplacian Filtered Salt Pepper Noise', salt_pepper_noise_filtered)

# 이미지를 화면에 표시
cv.waitKey(0)
cv.destroyAllWindows()