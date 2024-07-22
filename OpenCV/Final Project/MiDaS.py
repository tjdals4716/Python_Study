import torch
import torchvision.transforms as transforms
import cv2
import matplotlib.pyplot as plt
import numpy as np

# MiDaS 모델 로드
model_type = "DPT_Large"  # 사용할 모델 유형 (DPT_Large, DPT_Hybrid, MiDaS_small 등)
model = torch.hub.load("intel-isl/MiDaS", model_type)

# 모델 평가 모드로 설정
model.eval()

# 입력 이미지 전처리 변환 로드
transform = torch.hub.load("intel-isl/MiDaS", "transforms")

# 이미지 불러오기 및 전처리
img = cv2.imread("MSD1-1.png")  # 사용자의 이미지 파일 경로
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
input_batch = transform(img).unsqueeze(0)  # 이미지 전처리 및 배치 차원 추가

# GPU 사용 가능 시 모델을 GPU로 이동
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)
input_batch = input_batch.to(device)

# 깊이 추정
with torch.no_grad():
    prediction = model(input_batch)

# 결과 후처리
prediction = prediction.squeeze().cpu().numpy()
depth_map = cv2.normalize(prediction, None, 0, 255, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_8U)

# 결과 시각화
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.title('Input Image')
plt.imshow(img)
plt.axis('off')
plt.subplot(1, 2, 2)
plt.title('Depth Map using MiDaS')
plt.imshow(depth_map, cmap='inferno')
plt.axis('off')
plt.colorbar()
plt.show()
