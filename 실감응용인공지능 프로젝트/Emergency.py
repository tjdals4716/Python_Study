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
    print("API 응답 : ", response_text)  # 전체 응답 출력

    # XML 파싱
    root = ET.fromstring(response_text)

    # body 및 items 확인
    body = root.find('body')
    if body is not None:
        items = body.find('items')
        if items is not None:
            for item in items:
                duty_name = item.find('dutyName').text if item.find('dutyName') is not None else "정보 없음"
                duty_addr = item.find('dutyAddr').text if item.find('dutyAddr') is not None else "정보 없음"
                duty_tel1 = item.find('dutyTel1').text if item.find('dutyTel1') is not None else "정보 없음"
                print(f"병원명 : {duty_name}, 주소 : {duty_addr}, 대표전화 : {duty_tel1}")
        else:
            print("items 요소가 없습니다.")
    else:
        print("body 요소가 없습니다.")
else:
    print(f"API 호출 실패, 상태 코드 : {response.status_code}")
