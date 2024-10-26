import requests
import xml.etree.ElementTree as ET
from dotenv import load_dotenv
import os

# 보고서에 작성할 것
# 파이썬의 'requests' 라이브러리를 사용하여 ipapi.co API를 호출.
# API는 무료로 사용할 수 있고 별도의 인증 키가 필요 없음
# 단점은 사용자의 IP 주소를 기반으로 대략적인 위치를 제공하여 정확도가 높지 않을 수 있음
def get_current_location():
    try:
        response = requests.get('https://ipapi.co/json/')
        if response.status_code == 200:
            data = response.json()
            return data['latitude'], data['longitude']
        else:
            print("위치 정보를 가져오는데 실패했습니다. 수동으로 입력해주세요.")
            return None, None
    except Exception as e:
        print(f"오류 발생: {e}")
        print("위치 정보를 가져오는데 실패했습니다. 수동으로 입력해주세요.")
        return None, None

# 환경변수 로드
load_dotenv()

# 환경변수에서 값 호출
api_key = os.getenv("API_KEY")
gemini_api_key = os.getenv("GEMINI_API_KEY")
endpoint = os.getenv("LOCATION_ENDPOINT")
gemini_endpoint = os.getenv("GEMINI_ENDPOINT")

# 사용자가 입력할 STAGE1, STAGE2 값
stage1 = input("주소 시도(STAGE1)를 입력하세요 : ")
stage2 = input("주소 시군구(STAGE2)를 입력하세요 : ")

# 현재 위치 정보 가져오기
latitude, longitude = get_current_location()

# 위치 정보를 가져오지 못한 경우 수동 입력
if latitude is None or longitude is None:
    latitude = float(input("현재 위치의 위도를 입력하세요 : "))
    longitude = float(input("현재 위치의 경도를 입력하세요 : "))

# 사용자의 현재 위치 출력
print(f"\n현재 사용자의 위치: 위도 {latitude}, 경도 {longitude}")

# 전체 URI 출력
uri = f"{endpoint}?serviceKey={api_key}&pageNo=1&numOfRows=100&Q0={stage1}&Q1={stage2}"
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
            prompt = f"현재 나는 위도 {latitude}, 경도 {longitude}에 위치하고 있어. 현재 내가 어디있는지 알 수 있겠어? 알 수 있겠다면 어딘지 말해봐. 그리고 조회된 데이터에 대해 현재 사용자의 위치에서 가장 가까운 의료가 가능한 응급실을 알려줘:\n"
            
            for item in items:
                duty_name = item.find('dutyName').text if item.find('dutyName') is not None else "정보 없음"
                hvs04 = item.find('hvamyn').text if item.find('hvamyn') is not None else "정보 없음"
                duty_tel1 = item.find('dutyTel1').text if item.find('dutyTel1') is not None else "정보 없음"
                dutyAddr = item.find('dutyAddr').text if item.find('dutyAddr') is not None else "정보 없음"
                wgs84Lon = item.find('wgs84Lon').text if item.find('wgs84Lon') is not None else "정보 없음"
                wgs84Lat = item.find('wgs84Lat').text if item.find('wgs84Lat') is not None else "정보 없음"
                
                # 프롬프트 생성
                prompt += f"병원명 : {duty_name}, 구급차 가용 여부 : {hvs04}, 전화번호 : {duty_tel1}, 응급실 주소 : {dutyAddr}, 위도 : {wgs84Lat}, 경도 : {wgs84Lon}\n"
            
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
                print("\nAI 응답 (사용자 위치: 위도 {}, 경도 {}): ".format(latitude, longitude))
                print(result["candidates"][0]["content"])
            else:
                print(f"Gemini API 호출 실패 : {gemini_response.status_code}, 메시지: {gemini_response.text}")
        else:
            print("items 요소가 없습니다.")
    else:
        print("body 요소가 없습니다.")
else:
    print(f"API 호출 실패, 상태 코드 : {response.status_code}")