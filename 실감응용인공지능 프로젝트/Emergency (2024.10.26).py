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
    """Google Geocoding API를 사용하여 대략적인 주소(시도 및 시군구) 조회"""
    google_maps_url = f"https://maps.googleapis.com/maps/api/geocode/json?latlng={latitude},{longitude}&key={google_geocoding_key}&language=ko"
    response = requests.get(google_maps_url)

    # print(f"Google Geocoding API 요청 URL: {google_maps_url}")
    # print(f"응답 상태 코드: {response.status_code}")
    # print(f"응답 내용: {response.text}")

    if response.status_code == 200:
        location_data = response.json()
        if location_data['status'] == 'OK' and location_data['results']:
            # 첫 번째 결과의 주소 구성요소를 확인
            address_components = location_data['results'][0]['address_components']
            
            # 다양한 행정구역 레벨 확인
            stage1 = (
                extract_address_component(address_components, 'administrative_area_level_1') or
                extract_address_component(address_components, 'locality') or
                extract_address_component(address_components, 'sublocality_level_1')
            )
            
            stage2 = (
                extract_address_component(address_components, 'administrative_area_level_2') or
                extract_address_component(address_components, 'sublocality_level_2') or
                extract_address_component(address_components, 'sublocality')
            )

            # 주소를 찾지 못한 경우 다른 결과들도 확인
            if not stage1 or not stage2:
                for result in location_data['results'][1:]:
                    components = result['address_components']
                    if not stage1:
                        stage1 = (
                            extract_address_component(components, 'administrative_area_level_1') or
                            extract_address_component(components, 'locality') or
                            extract_address_component(components, 'sublocality_level_1')
                        )
                    if not stage2:
                        stage2 = (
                            extract_address_component(components, 'administrative_area_level_2') or
                            extract_address_component(components, 'sublocality_level_2') or
                            extract_address_component(components, 'sublocality')
                        )
                    if stage1 and stage2:
                        break

            if stage1 and stage2:
                print(f"현재 사용자 위치 : {stage1} {stage2}")
                return stage1, stage2
            else:
                print("필요한 주소 구성 요소를 찾지 못했습니다.")
                return None, None
        else:
            print("주소 결과가 없거나 API 응답이 OK가 아닙니다.")
            return None, None
    else:
        print("Google Geocoding API 호출 실패. 상태 코드 : ", response.status_code)
        return None, None

# 현재 위치 정보 가져오기
latitude, longitude = get_current_location()

# 위치 정보를 가져오지 못한 경우 수동 입력
if latitude is None or longitude is None:
    latitude = float(input("현재 위치의 위도를 입력하세요 : "))
    longitude = float(input("현재 위치의 경도를 입력하세요 : "))

# Google Geolocation API로 주소 조회
stage1, stage2 = get_location_address(latitude, longitude)

# 주소 정보가 없을 경우 수동 입력
if not stage1 or not stage2:
    stage1 = input("주소 시도(STAGE1)를 입력하세요 : ")
    stage2 = input("주소 시군구(STAGE2)를 입력하세요 : ")

# 사용자의 불편 사항 입력
discomfort = input("어디가 불편하신가요? : ")

# 응급실 정보 조회 및 AI 프롬프트 생성 부분
uri = f"{location_endpoint}?serviceKey={api_key}&pageNo=1&numOfRows=100&Q0={stage1}&Q1={stage2}"
response = requests.get(uri)

if response.status_code == 200:
    response_text = response.content.decode('utf-8')
    root = ET.fromstring(response_text)
    body = root.find('body')
    if body is not None:
        items = body.find('items')
        if items is not None:
            # AI 프롬프트 생성
            prompt = f"""당신은 한국에서 현재 사용자의 위치에 가장 가까운 응급 의료 기관을 안내하는 AI입니다.\n
            사용자 불편 사항 : {discomfort}\n
            우선 사용자가 입력한 불편 사항에 따라 확인하는 문장을 처음에 넣어주세요.\n
            예를들어 사용자가 머리가 아프다고 하면 "사용자님 두통을 겪고 계시는군요" 이런식으로.\n
            사용자는 현재 한국 {stage1} {stage2}에 있으며, 위도 {latitude}, 경도 {longitude}에 위치해 있습니다.\n
            우선 현재 조회되는 위치의 시, 구, 동, 군, 구, 읍을 모두 정확히 세밀하게 알려주세요.\n
            그다음 목표는 사용자의 위치에서 가장 가까운 응급 의료 시설을 찾아 제공하는 것입니다.\n
            아래는 사용자 위치 근처에 있는 응급실 정보 목록입니다.\n
            만약에 주변에 응급실이 없다면 가까운 주변 응급실이 없다고 알려주세요.\n
            그리고 현재 위치에서 제일 가까운 응급실을 매칭해주세요.\n
            각 응급실에 대한 상세 정보를 참고하여, 가장 적합한 병원을 추천해주세요.\n
            중요한 세부사항에는 구급차 가용 여부와 병원의 연락처가 포함됩니다.\n
            응급실을 추천할 때 가장 가까운 거리의 병원을 우선으로 고려해주세요.\n
            마지막으로는 최종적으로 정리된 병원을 알려주세요.\n
            예를 들어 최종적으로 분석된 응급실에 대해 "최종 추천 응급실 : [병원 정보들]과 함께 최종적으로 매칭된 응급실을 정리하여 알려주세요."\n\n"""

            for item in items:
                duty_name = item.find('dutyName').text if item.find('dutyName') is not None else "정보 없음"
                hvs04 = item.find('hvamyn').text if item.find('hvamyn') is not None else "정보 없음"
                duty_tel1 = item.find('dutyTel1').text if item.find('dutyTel1') is not None else "정보 없음"
                dutyAddr = item.find('dutyAddr').text if item.find('dutyAddr') is not None else "정보 없음"
                wgs84Lon = item.find('wgs84Lon').text if item.find('wgs84Lon') is not None else "정보 없음"
                wgs84Lat = item.find('wgs84Lat').text if item.find('wgs84Lat') is not None else "정보 없음"
                
                prompt += f"""병원명: {duty_name}
                구급차 가용 여부: {hvs04}
                전화번호: {duty_tel1}
                응급실 주소: {dutyAddr}
                위도: {wgs84Lat}, 경도: {wgs84Lon}\n\n"""

            # print("생성된 프롬프트:\n", prompt)

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
                print("\nAI 응답 (사용자 위치: 위도 {}, 경도 {}) : ".format(latitude, longitude))
                print(result["candidates"][0]["content"])
            else:
                print(f"Gemini API 호출 실패 : {gemini_response.status_code}, 메시지 : {gemini_response.text}")
        else:
            print("items 요소가 없습니다.")
    else:
        print("body 요소가 없습니다.")
else:
    print(f"API 호출 실패, 상태 코드 : {response.status_code}")