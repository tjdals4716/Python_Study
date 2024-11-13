import requests
import xml.etree.ElementTree as ET
from dotenv import load_dotenv
import os

# 환경변수 로드
load_dotenv()

# API 키 호출
api_key = os.getenv("API_KEY")
gemini_api_key = os.getenv("GEMINI_API_KEY")
location_endpoint = os.getenv("LOCATION_ENDPOINT")
gemini_endpoint = os.getenv("GEMINI_ENDPOINT")
google_geolocation_key = os.getenv("GOOGLE_GEOLOCATION_KEY")
google_geocoding_key = os.getenv("GOOGLE_GEOCODING_KEY")

def get_current_location():
    """사용자의 현재 위치 (위도, 경도) 조회"""
    url = f"https://www.googleapis.com/geolocation/v1/geolocate?key={google_geolocation_key}"
    response = requests.post(url)
    
    if response.status_code == 200:
        location_data = response.json()
        lat = location_data['location']['lat']
        lng = location_data['location']['lng']
        return lat, lng
    else:
        print("위치 정보를 가져오는데 실패했습니다.")
        return None, None

def get_address_from_coordinates(latitude, longitude):
    """위도와 경도로부터 도로명 주소 조회"""
    geocode_url = f"https://maps.googleapis.com/maps/api/geocode/json?latlng={latitude},{longitude}&key={google_geocoding_key}&language=ko"
    response = requests.get(geocode_url)
    
    if response.status_code == 200:
        result = response.json()
        if result['status'] == 'OK':
            address = result['results'][0]['formatted_address']
            return address
        else:
            print("주소 조회 실패.")
            return None
    else:
        print("Google Geocoding API 호출 실패.")
        return None

def search_emergency_rooms(latitude, longitude, radius=5000):
    """현재 위치 기반 응급실 정보 조회"""
    uri = f"{location_endpoint}?serviceKey={api_key}&pageNo=1&numOfRows=100&radius={radius}&xPos={longitude}&yPos={latitude}&_type=json"
    response = requests.get(uri)

    if response.status_code == 200:
        data = response.json()
        items = data.get("response", {}).get("body", {}).get("items", {}).get("item", [])
        return items
    else:
        print("응급실 정보 조회 실패.")
        return []

# 현재 위치 조회
latitude, longitude = get_current_location()
if not latitude or not longitude:
    print("현재 위치를 가져오는데 실패했습니다. 프로그램을 종료합니다.")
    exit()

# 현재 위치 주소 조회
address = get_address_from_coordinates(latitude, longitude)
if not address:
    print("주소를 조회할 수 없어 프로그램을 종료합니다.")
    exit()

print(f"현재 위치: {address} (위도: {latitude}, 경도: {longitude})")

# 사용자 증상 입력
symptom = input("어디가 불편하신가요?: ")

# 응급실 정보 조회 (처음엔 5km 범위로 조회)
emergency_rooms = search_emergency_rooms(latitude, longitude, radius=5000)

# AI 프롬프트 생성
prompt = f"""
당신은 한국에서 현재 사용자의 위치에 가장 가까운 응급 의료 기관을 안내하는 AI입니다.
사용자의 증상: {symptom}
현재 사용자는 {address}에 있으며, 위도 {latitude}, 경도 {longitude}에 위치해 있습니다.

"""

# 응급실 정보가 있으면 상위 5개 응급실을 제공
if emergency_rooms:
    prompt += "\n다음은 사용자의 위치에서 가장 가까운 응급실 목록입니다:\n"
    for idx, room in enumerate(emergency_rooms[:5], 1):  # 상위 5개만 표시
        hospital_name = room.get('dutyName', '정보 없음')
        hospital_address = room.get('dutyAddr', '정보 없음')
        contact = room.get('dutyTel1', '정보 없음')
        availability = room.get('hvamyn', '정보 없음')

        prompt += f"\n{idx}. 병원명: {hospital_name}\n주소: {hospital_address}\n연락처: {contact}\n구급차 가용 여부: {availability}\n"
else:
    # 응급실을 찾을 수 없다면 범위를 넓혀서 다시 시도
    prompt += "현재 주변에 응급실이 없으므로 더 넓은 범위로 응급실을 찾습니다.\n"

    # 범위 확장 (10km, 20km)
    for radius in [10000, 20000]:
        print(f"{radius // 1000}km 범위로 검색 중...")
        emergency_rooms = search_emergency_rooms(latitude, longitude, radius=radius)

        if emergency_rooms:
            prompt += f"\n{radius // 1000}km 범위에서 찾은 응급실 목록입니다:\n"
            for idx, room in enumerate(emergency_rooms[:5], 1):  # 상위 5개만 표시
                hospital_name = room.get('dutyName', '정보 없음')
                hospital_address = room.get('dutyAddr', '정보 없음')
                contact = room.get('dutyTel1', '정보 없음')
                availability = room.get('hvamyn', '정보 없음')

                prompt += f"\n{idx}. 병원명: {hospital_name}\n주소: {hospital_address}\n연락처: {contact}\n구급차 가용 여부: {availability}\n"
            break  # 가장 가까운 응급실을 찾으면 반복 종료
        else:
            prompt += f"{radius // 1000}km 범위에서도 응급실을 찾을 수 없습니다.\n"

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

gemini_response = requests.post(f"{gemini_endpoint}?key={gemini_api_key}", json=data, headers=headers)

# AI 응답 처리
if gemini_response.status_code == 200:
    result = gemini_response.json()
    ai_response = result.get("candidates", [{}])[0].get("content", "응답이 없습니다.")
    print("\nAI 응답:\n", ai_response)
else:
    print("Gemini API 호출 실패:", gemini_response.status_code)
