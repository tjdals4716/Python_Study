import requests
import xml.etree.ElementTree as ET
from dotenv import load_dotenv
import os

# 환경변수 로드
load_dotenv()

# 환경변수에서 값 호출
api_key = os.getenv("API_KEY")
gemini_api_key = os.getenv("GEMINI_API_KEY")
endpoint = os.getenv("ENDPOINT")
gemini_endpoint = os.getenv("GEMINI_ENDPOINT")

# 사용자가 입력할 STAGE1, STAGE2 값
stage1 = input("주소 시도(STAGE1)를 입력하세요 : ")
stage2 = input("주소 시군구(STAGE2)를 입력하세요 : ")

# 전체 URI 출력
uri = f"{endpoint}?serviceKey={api_key}&pageNo=1&numOfRows=100&STAGE1={stage1}&STAGE2={stage2}"
print("전체 URI : ", uri)

# API 호출 (params 없이 직접 uri 사용)
response = requests.get(uri)

# API 호출 상태 코드 확인
if response.status_code == 200:
    response_text = response.content.decode('utf-8')
    print("API 응답 : ", response_text)

    # XML 파싱
    root = ET.fromstring(response_text)

    # body 및 items 확인
    body = root.find('body')
    if body is not None:
        items = body.find('items')
        if items is not None:
            prompt = "현재 나는 대구 달서구 계대동문로4길 19에 위치하고있어. 조회된 데이터에 대해 현재 사용자의 위치에서 가장 가까운 의료가 가능한 응급실을 알려줘:\n"
            for item in items:
                duty_name = item.find('dutyName').text if item.find('dutyName') is not None else "정보 없음"
                hvs04 = item.find('hvamyn').text if item.find('hvamyn') is not None else "정보 없음"
                duty_tel1 = item.find('dutyTel3').text if item.find('dutyTel3') is not None else "정보 없음"
                dutyAddr = item.find('dutyAddr').text if item.find('dutyAddr') is not None else "정보 없음"
                # 프롬프트 생성
                prompt += f"병원명 : {duty_name}, 구급차 가용 여부 : {hvs04}, 전화번호 : {duty_tel1}, 응급실 위치 : {dutyAddr}\n"
            print("생성된 프롬프트 : \n", prompt)

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

            if gemini_response.status_code == 200:
                result = gemini_response.json()
                print("AI 응답 : ", result["candidates"][0]["content"])
            else:
                print(f"Gemini API 호출 실패 : {gemini_response.status_code}, 메시지: {gemini_response.text}")
        else:
            print("items 요소가 없습니다.")
    else:
        print("body 요소가 없습니다.")
else:
    print(f"API 호출 실패, 상태 코드 : {response.status_code}")