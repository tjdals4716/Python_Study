import requests
import os
from dotenv import load_dotenv

# 환경 변수 로드
load_dotenv()

# 환경 변수에서 API 키와 엔드포인트 URL 호출
gemini_api_key = os.getenv("GEMINI_API_KEY")
gemini_endpoint = os.getenv("GEMINI_ENDPOINT")

# 프롬프트 설정
prompt = "오늘의 운세를 알려줘. 그냥 재미로하는거야."

# 요청 헤더 설정
headers = {
    "Content-Type": "application/json"
}

# 요청 데이터 구성
data = {
    "model": "gemini-1.5-flash-latest",
    "contents": [
        {
            "parts": [
                {
                    "text": prompt
                }
            ]
        }
    ]
}

# Gemini API 호출
gemini_response = requests.post(f"{gemini_endpoint}?key={gemini_api_key}", json=data, headers=headers)

# 호출 결과 확인
if gemini_response.status_code == 200:
    result = gemini_response.json()
    print(result["candidates"][0]["content"])
else:
    print(f"Gemini API 호출 실패 : {gemini_response.status_code}, 메시지 : {gemini_response.text}")
