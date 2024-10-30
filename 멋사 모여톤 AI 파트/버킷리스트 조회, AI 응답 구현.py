import requests
import os
from dotenv import load_dotenv

load_dotenv()

gemini_api_key = os.getenv("GEMINI_API_KEY")
gemini_endpoint = os.getenv("GEMINI_ENDPOINT")

user_id = input("\n 조회할 userId를 입력하세요 : ")

data_url = f"https://newteamsgoody.shop/api/bucket/all/{user_id}"
data_response = requests.get(data_url)

if data_response.status_code == 200:
    data_content = data_response.json()
    user_id = data_response.json()
    print("\n 조회된 데이터 : ", data_content)

    prompt = (
        "현재 사용자의 아이디를 보고 알려줘."
        "사용자는 바다가는것을 좋아해. 그러니 여기서 바다와 관련된 내용이 포함된 버킷리스트를 추천해줘."
        "그리고 왜 추천하는지 그 이유도 설명해줘."

        "사용자의 생성 버킷리스트 취향에 따라 "
    )

    # 데이터와 프롬프트를 별도로 전달
    headers = {
        "Content-Type": "application/json"
    }
    data = {
        "model": "gemini-1.5-flash-latest",
        "contents": [
            {
                "parts": [
                    {"text" : prompt},
                    {"text" : f"\n 사용자 데이터 : {data_content}"},
                    {"text" : f"\n 유저 Id : {user_id}"}
                ]
            }
        ]
    }

    print("\n 입력된 요청 : ", prompt)

    # Gemini API 호출
    gemini_response = requests.post(f"{gemini_endpoint}?key={gemini_api_key}", json=data, headers=headers)

    if gemini_response.status_code == 200:
        result = gemini_response.json()
        print("\n AI 응답 : ", result["candidates"][0]["content"])
    else:
        print(f"Gemini API 호출 실패 : {gemini_response.status_code}, 메시지 : {gemini_response.text}")
else:
    print(f"데이터 조회 실패 : 상태 코드 {data_response.status_code}, 메시지 : {data_response.text}")
