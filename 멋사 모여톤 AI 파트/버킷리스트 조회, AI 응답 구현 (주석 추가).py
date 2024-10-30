import requests
import os
from dotenv import load_dotenv

# 환경 변수 로드
load_dotenv()

# 환경 변수에서 Gemini API 키와 엔드포인트 URL 호출
gemini_api_key = os.getenv("GEMINI_API_KEY")
gemini_endpoint = os.getenv("GEMINI_ENDPOINT")

# 사용자 ID 입력받기
user_id = input("조회할 userId를 입력하세요: ")

# API 요청 URL 구성
data_url = f"https://newteamsgoody.shop/api/bucket/all/{user_id}"

# GET 요청으로 데이터 조회
data_response = requests.get(data_url)

if data_response.status_code == 200:
    # 조회된 데이터를 JSON 형식으로 로드
    data_content = data_response.json()
    print("조회된 데이터 : ", data_content)

    # 프롬프트에 조회 데이터 추가
    prompt = (
        f"조회된 데이터는 다음과 같아 : \n{data_content} 여기서 조회된 버킷 데이터로 어디가는지에 대해 설명하고 추가로 주변도 추천해줘"
    )

    # Gemini API 요청 데이터 구성
    headers = {
        "Content-Type": "application/json"
    }
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

    # Gemini API 호출 결과 확인
    if gemini_response.status_code == 200:
        result = gemini_response.json()
        print("AI 응답 : ", result["candidates"][0]["content"])
    else:
        print(f"Gemini API 호출 실패 : {gemini_response.status_code}, 메시지 : {gemini_response.text}")
else:
    print(f"데이터 조회 실패: 상태 코드 {data_response.status_code}, 메시지: {data_response.text}")
