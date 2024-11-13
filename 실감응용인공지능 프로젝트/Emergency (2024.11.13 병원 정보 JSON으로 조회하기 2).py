import requests
import xml.etree.ElementTree as ET
from dotenv import load_dotenv
import os

# 환경변수 로드
load_dotenv()

# 환경변수에서 API 키 호출
api_key = os.getenv("API_KEY")
gemini_api_key = os.getenv("GEMINI_API_KEY")
location_endpoint = os.getenv("LOCATION_ENDPOINT")
gemini_endpoint = os.getenv("GEMINI_ENDPOINT")
google_geolocation_key = os.getenv("GOOGLE_GEOLOCATION_KEY")
google_geocoding_key = os.getenv("GOOGLE_GEOCODING_KEY")

def get_current_location():
    """사용자의 위도와 경도를 Google Geolocation API를 사용하여 조회"""
    try:
        url = f"https://www.googleapis.com/geolocation/v1/geolocate?key={google_geolocation_key}"
        response = requests.post(url)
        
        # print(f"응답 상태 코드: {response.status_code}")
        # print(f"응답 내용: {response.text}")

        if response.status_code == 200:
            location_data = response.json()
            lat = location_data['location']['lat']
            lng = location_data['location']['lng']
            return lat, lng
        else:
            print("위치 정보를 가져오는데 실패했습니다. 상태 코드:", response.status_code)
            return None, None
    except Exception as e:
        print(f"오류 발생: {e}")
        return None, None

def extract_address_component(components, type_name):
    """주소 구성요소에서 특정 타입의 값을 추출"""
    for component in components:
        if type_name in component['types']:
            return component['long_name']
    return None

def get_location_address(latitude, longitude):
    """Google Geocoding API를 사용하여 도로명 주소까지 조회"""
    google_maps_url = f"https://maps.googleapis.com/maps/api/geocode/json?latlng={latitude},{longitude}&key={google_geocoding_key}&language=ko"
    response = requests.get(google_maps_url)

    # print(f"Google Geocoding API 요청 URL: {google_maps_url}")
    # print(f"응답 상태 코드: {response.status_code}")
    # print(f"응답 내용: {response.text}")

    if response.status_code == 200:
        location_data = response.json()
        if location_data['status'] == 'OK' and location_data['results']:

            # 첫 번째 결과의 주소 구성요소 확인
            address_components = location_data['results'][0]['address_components']
            formatted_address = location_data['results'][0].get('formatted_address', '정보 없음')

            # 시도 추출
            stage1 = (
                extract_address_component(address_components, 'administrative_area_level_1') or
                extract_address_component(address_components, 'locality') or
                extract_address_component(address_components, 'sublocality_level_1')
            )
            
            # 시군구 추출
            stage2 = (
                extract_address_component(address_components, 'administrative_area_level_2') or
                extract_address_component(address_components, 'sublocality_level_2') or
                extract_address_component(address_components, 'sublocality')
            )
            
            # 동 추출
            stage3 = (
                extract_address_component(address_components, 'sublocality_level_3') or
                extract_address_component(address_components, 'neighborhood') or
                extract_address_component(address_components, 'premise')
            )

            # 도로명 주소 추출
            road_address = formatted_address

            if stage1 and stage2 and stage3:
                print(f"현재 사용자 위치 : {stage1} {stage2} {stage3}")
                print(f"도로명 주소 : {road_address}")
                return stage1, stage2, stage3, road_address
            else:
                print("필요한 주소 구성 요소를 찾지 못했습니다.")
                return None, None, None, None
        else:
            print("주소 결과가 없거나 API 응답이 OK가 아닙니다.")
            return None, None, None, None
    else:
        print("Google Geocoding API 호출 실패. 상태 코드 : ", response.status_code)
        return None, None, None, None


# 현재 위치 정보 가져오기
latitude, longitude = get_current_location()

# 위치 정보를 가져오지 못한 경우 수동 입력
if latitude is None or longitude is None:
    latitude = float(input("현재 위치의 위도를 입력하세요 : "))
    longitude = float(input("현재 위치의 경도를 입력하세요 : "))

# Google Geolocation API로 주소 조회
stage1, stage2, stage3, road_address = get_location_address(latitude, longitude)

# 주소 정보가 없을 경우 수동 입력
if not stage1 or not stage2 or not stage3 or not road_address:
    stage1 = input("주소 시도(STAGE1)를 입력하세요 : ")
    stage2 = input("주소 시군구(STAGE2)를 입력하세요 : ")
    stage3 = input("주소 동(STAGE3)를 입력하세요 : ")
    road_address = input("도로명 주소를 입력하세요 : ")

# 사용자의 불편 사항 입력
discomfort = input("어디가 불편하신가요? : ")

# 응급실 정보 조회 및 AI 프롬프트 생성 부분 (JSON 형식 요청)
uri = f"{location_endpoint}?serviceKey={api_key}&pageNo=1&numOfRows=100&Q0={stage1}&Q1={stage2}&_type=json"
response = requests.get(uri)

if response.status_code == 200:
    data_content = response.json()
    print("\n조회된 데이터 (JSON 형식): ", data_content)

    # JSON 데이터에서 필요한 정보 추출
    response_body = data_content.get("response", {}).get("body", {})
    total_count = response_body.get("totalCount", 0)

    # 응급실 정보가 있는지 확인
    if total_count == 0:
        print("조회된 응급실 정보가 없습니다.")
    else:
        items = response_body.get("items")
        
        # items가 문자열이 아니라 딕셔너리인지 확인
        if isinstance(items, dict) and "item" in items:
            item_list = items.get("item", [])
        else:
            item_list = []

        # AI 프롬프트 생성
        prompt = f"""당신은 한국에서 현재 사용자의 위치에 가장 가까운 응급 의료 기관을 안내하는 AI입니다.\n
        사용자 불편 사항 : {discomfort}\n
        사용자는 현재 한국 {stage1} {stage2}에 있으며, 위도 {latitude}, 경도 {longitude}에 위치해 있습니다.\n
        아래는 사용자 위치 근처에 있는 응급실 정보 목록입니다.\n\n"""

        # 응급실 정보 추가
        for item in item_list:
            duty_name = item.get('dutyName', "정보 없음")
            hvs04 = item.get('hvamyn', "정보 없음")
            duty_tel1 = item.get('dutyTel1', "정보 없음")
            dutyAddr = item.get('dutyAddr', "정보 없음")
            wgs84Lon = item.get('wgs84Lon', "정보 없음")
            wgs84Lat = item.get('wgs84Lat', "정보 없음")
            
            prompt += f"""병원명: {duty_name}
            구급차 가용 여부: {hvs04}
            전화번호: {duty_tel1}
            응급실 주소: {dutyAddr}
            위도: {wgs84Lat}, 경도: {wgs84Lon}\n\n"""

        if item_list:
            # Gemini API 요청
            headers = {"Content-Type": "application/json"}
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
                ai_response_text = result["candidates"][0]["content"]
                print("\nAI 응답 : ", ai_response_text)
            else:
                print(f"Gemini API 호출 실패 : {gemini_response.status_code}, 메시지 : {gemini_response.text}")
        else:
            print("조회된 응급실 정보가 없습니다.")
else:
    print(f"API 호출 실패, 상태 코드 : {response.status_code}")
