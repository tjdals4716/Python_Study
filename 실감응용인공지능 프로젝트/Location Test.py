import os
import requests
from dotenv import load_dotenv

# .env 파일에서 환경변수 로드
load_dotenv()

# Google Geolocation API와 Geocoding API 키 가져오기
GOOGLE_GEOLOCATION_KEY = os.getenv("GOOGLE_GEOLOCATION_KEY")
GOOGLE_GEOCODING_KEY = os.getenv("GOOGLE_GEOCODING_KEY")

def get_current_location():
    url = f"https://www.googleapis.com/geolocation/v1/geolocate?key={GOOGLE_GEOLOCATION_KEY}"
    response = requests.post(url)

    if response.status_code == 200:
        location_data = response.json()
        lat = location_data['location']['lat']
        lng = location_data['location']['lng']
        print(f"현재 위치: 위도 {lat}, 경도 {lng}")
        return lat, lng
    else:
        print(f"위치 조회 실패: {response.status_code} - {response.text}")
        return None, None

def get_address(lat, lng):
    # 한국어로 응답 받기 위해 language=ko 파라미터 추가
    url = f"https://maps.googleapis.com/maps/api/geocode/json?latlng={lat},{lng}&language=ko&key={GOOGLE_GEOCODING_KEY}"
    response = requests.get(url)

    if response.status_code == 200:
        address_data = response.json()
        if address_data['results']:
            address_components = address_data['results'][0]['address_components']
            city = None
            district = None
            province = None
            neighborhood = None

            for component in address_components:
                if 'locality' in component['types']:  # 도시
                    city = component['long_name']
                elif 'administrative_area_level_2' in component['types']:  # 구
                    district = component['long_name']
                elif 'administrative_area_level_1' in component['types']:  # 주
                    province = component['long_name']
                elif 'sublocality' in component['types']:  # 동
                    neighborhood = component['long_name']

            print(f"도시: {city}, 구: {district}, 주: {province}, 동: {neighborhood}")
        else:
            print("주소를 찾을 수 없습니다.")
    else:
        print(f"주소 조회 실패: {response.status_code} - {response.text}")

if __name__ == "__main__":
    lat, lng = get_current_location()
    if lat and lng:
        get_address(lat, lng)
