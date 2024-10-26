import requests
import xml.etree.ElementTree as ET
from dotenv import load_dotenv
import os
from math import radians, sin, cos, sqrt, atan2

# 환경변수 로드
load_dotenv()

# 환경변수에서 API 키 호출
api_key = os.getenv("API_KEY")
gemini_api_key = os.getenv("GEMINI_API_KEY")
location_endpoint = os.getenv("LOCATION_ENDPOINT")
gemini_endpoint = os.getenv("GEMINI_ENDPOINT")
google_geolocation_key = os.getenv("GOOGLE_GEOLOCATION_KEY")
google_geocoding_key = os.getenv("GOOGLE_GEOCODING_KEY")

def calculate_distance(lat1, lon1, lat2, lon2):
    """두 지점 간의 거리를 계산 (Haversine 공식)"""
    R = 6371  # 지구의 반경 (km)
    
    lat1, lon1, lat2, lon2 = map(float, [lat1, lon1, lat2, lon2])
    
    dlat = radians(lat2 - lat1)
    dlon = radians(lon2 - lon1)
    a = sin(dlat/2) * sin(dlat/2) + cos(radians(lat1)) \
        * cos(radians(lat2)) * sin(dlon/2) * sin(dlon/2)
    c = 2 * atan2(sqrt(a), sqrt(1-a))
    distance = R * c
    
    return distance

def get_nearby_cities(latitude, longitude):
    """현재 위치 주변의 주요 도시들을 반환"""
    url = f"https://maps.googleapis.com/maps/api/geocode/json?latlng={latitude},{longitude}&key={google_geocoding_key}&language=ko&result_type=administrative_area_level_1|administrative_area_level_2"
    response = requests.get(url)
    
    nearby_cities = []
    if response.status_code == 200:
        data = response.json()
        if data['status'] == 'OK':
            # 현재 위치의 시/도를 찾아서 해당 지역의 주요 도시들을 반환
            for result in data['results']:
                for component in result['address_components']:
                    if 'administrative_area_level_1' in component['types']:
                        province = component['long_name']
                        # 시/도별 주요 도시 매핑
                        city_mapping = {
                            '경상북도': ['구미시', '포항시', '경주시', '안동시', '대구광역시'],
                            '경상남도': ['창원시', '김해시', '진주시', '양산시', '부산광역시'],
                            '전라북도': ['전주시', '익산시', '군산시', '광주광역시'],
                            '전라남도': ['목포시', '여수시', '순천시', '광주광역시'],
                            '충청북도': ['청주시', '충주시', '제천시', '대전광역시'],
                            '충청남도': ['천안시', '아산시', '서산시', '대전광역시'],
                            '경기도': ['수원시', '성남시', '고양시', '용인시', '서울특별시'],
                            '강원도': ['춘천시', '원주시', '강릉시', '속초시'],
                        }
                        nearby_cities = city_mapping.get(province, [])
                        break
    
    return nearby_cities

def get_current_location():
    """사용자의 위도와 경도를 Google Geolocation API를 사용하여 조회"""
    try:
        url = f"https://www.googleapis.com/geolocation/v1/geolocate?key={google_geolocation_key}"
        response = requests.post(url)
        
        print(f"응답 상태 코드: {response.status_code}")
        print(f"응답 내용: {response.text}")

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

def get_emergency_rooms(stage1, stage2):
    """특정 지역의 응급실 정보를 조회"""
    uri = f"{location_endpoint}?serviceKey={api_key}&pageNo=1&numOfRows=100&Q0={stage1}&Q1={stage2}"
    response = requests.get(uri)
    
    if response.status_code == 200:
        response_text = response.content.decode('utf-8')
        root = ET.fromstring(response_text)
        body = root.find('body')
        if body is not None:
            items = body.find('items')
            if items is not None:
                return items
    return None

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

    if response.status_code == 200:
        location_data = response.json()
        if location_data['status'] == 'OK' and location_data['results']:
            address_components = location_data['results'][0]['address_components']
            
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
                print(f"찾은 주소: {stage1} {stage2}")
                return stage1, stage2
            
    return None, None

def search_emergency_rooms(latitude, longitude, current_location=None):
    """현재 위치와 주변 도시의 응급실을 검색"""
    all_hospitals = []
    searched_cities = set()

    # 현재 위치에서 검색
    if current_location:
        stage1, stage2 = current_location
        items = get_emergency_rooms(stage1, stage2)
        if items is not None:
            for item in items:
                hospital = {
                    'name': item.find('dutyName').text if item.find('dutyName') is not None else "정보 없음",
                    'hvamyn': item.find('hvamyn').text if item.find('hvamyn') is not None else "정보 없음",
                    'tel': item.find('dutyTel1').text if item.find('dutyTel1') is not None else "정보 없음",
                    'addr': item.find('dutyAddr').text if item.find('dutyAddr') is not None else "정보 없음",
                    'lat': item.find('wgs84Lat').text if item.find('wgs84Lat') is not None else "0",
                    'lng': item.find('wgs84Lon').text if item.find('wgs84Lon') is not None else "0"
                }
                hospital['distance'] = calculate_distance(
                    latitude, longitude,
                    float(hospital['lat']), float(hospital['lng'])
                )
                all_hospitals.append(hospital)
                searched_cities.add(f"{stage1} {stage2}")

    # 주변 도시 검색
    if not all_hospitals:
        nearby_cities = get_nearby_cities(latitude, longitude)
        for city in nearby_cities:
            if f"{stage1} {city}" not in searched_cities:
                items = get_emergency_rooms(stage1, city)
                if items is not None:
                    for item in items:
                        hospital = {
                            'name': item.find('dutyName').text if item.find('dutyName') is not None else "정보 없음",
                            'hvamyn': item.find('hvamyn').text if item.find('hvamyn') is not None else "정보 없음",
                            'tel': item.find('dutyTel1').text if item.find('dutyTel1') is not None else "정보 없음",
                            'addr': item.find('dutyAddr').text if item.find('dutyAddr') is not None else "정보 없음",
                            'lat': item.find('wgs84Lat').text if item.find('wgs84Lat') is not None else "0",
                            'lng': item.find('wgs84Lon').text if item.find('wgs84Lon') is not None else "0"
                        }
                        hospital['distance'] = calculate_distance(
                            latitude, longitude,
                            float(hospital['lat']), float(hospital['lng'])
                        )
                        all_hospitals.append(hospital)
                        searched_cities.add(f"{stage1} {city}")

    # 거리순으로 정렬
    all_hospitals.sort(key=lambda x: x['distance'])
    return all_hospitals

def main():
    # 현재 위치 정보 가져오기
    latitude, longitude = get_current_location()

    # 위치 정보를 가져오지 못한 경우 수동 입력
    if latitude is None or longitude is None:
        latitude = float(input("현재 위치의 위도를 입력하세요 : "))
        longitude = float(input("현재 위치의 경도를 입력하세요 : "))

    # 현재 위치의 주소 정보 가져오기
    stage1, stage2 = get_location_address(latitude, longitude)

    # 주소 정보가 없을 경우 수동 입력
    if not stage1 or not stage2:
        stage1 = input("주소 시도(STAGE1)를 입력하세요 : ")
        stage2 = input("주소 시군구(STAGE2)를 입력하세요 : ")

    # 응급실 검색 (현재 위치 및 주변 도시)
    hospitals = search_emergency_rooms(latitude, longitude, (stage1, stage2))

    if hospitals:
        # AI 프롬프트 생성
        prompt = f"""당신은 한국에서 현재 사용자의 위치에 가장 가까운 응급 의료 기관을 안내하는 AI입니다.
        사용자는 현재 한국 {stage1} {stage2}에 있으며, 위도 {latitude}, 경도 {longitude}에 위치해 있습니다.\n
        우선 현재 조회되는 위치의 시, 구, 동, 군, 구, 읍을 모두 정확히 세밀하게 알려주세요.\n
        그다음 목표는 사용자의 위치에서 가장 가까운 응급 의료 시설을 찾아 제공하는 것입니다.\n
        아래는 사용자 위치 근처에 있는 응급실 정보 목록입니다.\n
        각 응급실에 대한 상세 정보를 참고하여, 가장 적합한 병원을 추천해주세요.\n
        중요한 세부사항에는 구급차 가용 여부와 병원의 연락처가 포함됩니다.\n
        응급실을 추천할 때 가장 가까운 거리의 병원을 우선으로 고려해주세요.\n\n"""

        for hospital in hospitals:
            prompt += f"""병원명: {hospital['name']}
            구급차 가용 여부: {hospital['hvamyn']}
            전화번호: {hospital['tel']}
            응급실 주소: {hospital['addr']}
            위도: {hospital['lat']}, 경도: {hospital['lng']}
            현재 위치에서의 거리: {hospital['distance']:.2f}km\n\n"""

        print("생성된 프롬프트:\n", prompt)

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
