import torch
import torch.nn as nn
import torch.nn.functional as F
import cv2
import numpy as np
import matplotlib.pyplot as plt

# DeepPruner 모델 로드
class DeepPrunerNet(nn.Module):
    # 여기에 DeepPruner의 실제 네트워크 정의가 필요합니다.
    # 이 예제에서는 간략화된 구조를 사용하겠습니다.
    def __init__(self):
        super(DeepPrunerNet, self).__init__()
        # 실제 DeepPruner 구조는 훨씬 더 복잡합니다.

    def forward(self, left_img, right_img):
        # 여기서는 간단한 Forward 패스를 정의합니다.
        return None

# DeepPruner 사전 학습된 모델 로드 (실제 모델 파일 경로를 사용해야 합니다)
# model = DeepPrunerNet()
# model.load_state_dict(torch.load('deeppruner_model.pth'))  # 실제 모델 경로로 대체

# 예제에서는 실제 DeepPruner 대신, 단순히 다른 사전 학습된 스테레오 매칭 모델을 사용
model = torch.hub.load('intel-isl/MiDaS', 'DPT_Large')  # 예제에서 MiDaS 모델 사용 (대체)

# 모델 평가 모드로 설정
model.eval()

# 스테레오 이미지 불러오기 및 전처리
img_left = cv2.imread('MSD1-1.png')
img_right = cv2.imread('MSD1-2.png')

# 이미지 크기 조정 (DeepPruner의 요구 사항에 맞게 조정해야 함)
img_left_resized = cv2.resize(img_left, (640, 480))  # DeepPruner에 맞는 크기로 조정
img_right_resized = cv2.resize(img_right, (640, 480))

# 이미지를 텐서로 변환 및 정규화
left_tensor = torch.from_numpy(img_left_resized).permute(2, 0, 1).float().unsqueeze(0) / 255.0
right_tensor = torch.from_numpy(img_right_resized).permute(2, 0, 1).float().unsqueeze(0) / 255.0

# GPU 사용 설정
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)
left_tensor = left_tensor.to(device)
right_tensor = right_tensor.to(device)

# 깊이 추정
with torch.no_grad():
    # DeepPruner는 두 개의 이미지를 입력으로 받습니다.
    disparity_map = model(left_tensor, right_tensor)

# 시차 맵 후처리
disparity_map = disparity_map.squeeze().cpu().numpy()
disparity_map = cv2.normalize(disparity_map, None, alpha=0, beta=255, norm_type=cv2.NORM_MINMAX)
disparity_map = np.uint8(disparity_map)

# 결과 시각화
plt.figure(figsize=(10, 5))
plt.subplot(1, 3, 1)
plt.title('Left Image')
plt.imshow(cv2.cvtColor(img_left, cv2.COLOR_BGR2RGB))
plt.axis('off')
plt.subplot(1, 3, 2)
plt.title('Right Image')
plt.imshow(cv2.cvtColor(img_right, cv2.COLOR_BGR2RGB))
plt.axis('off')
plt.subplot(1, 3, 3)
plt.title('Depth Map using DeepPruner')
plt.imshow(disparity_map, cmap='jet')
plt.colorbar()
plt.axis('off')
plt.show()
