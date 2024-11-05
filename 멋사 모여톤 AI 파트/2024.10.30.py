import requests
import os
import json
import jwt
from dotenv import load_dotenv

load_dotenv()

gemini_api_key = os.getenv("GEMINI_API_KEY")
gemini_endpoint = os.getenv("GEMINI_ENDPOINT")

def login(uid, password):
    login_url = "https://newteamsgoody.shop/user/login"
    payload = {
        "uid": uid,
        "password": password
    }
    response = requests.post(login_url, json=payload)
    if response.status_code == 200:
        json_response = response.json()
        print("로그인 성공!")
        print("\n 로그인된 유저 데이터 : ")
        print(json.dumps(json_response, ensure_ascii=False, indent=9))
        return json_response["token"], json_response["user"]
    else:
        print(f"아이디가 존재하지않거나 비밀번호가 틀립니다 : 상태 코드 {response.status_code}, 메시지 : {response.text}")
        return None, None

def get_user_data(user_id, token):
    print("\n uid 체크 : ", user_id)
    print("\n 토큰값 체크 : ", token)
    
    def get_user_id_from_token(token):
        try:
            payload = jwt.decode(token, options={"verify_signature": False})
            print("\n 토큰 페이로드 : ", payload)
            return payload.get("uid")
        except jwt.ExpiredSignatureError:
            print("토큰이 만료되었습니다.")
            return None
        except jwt.InvalidTokenError:
            print("유효하지 않은 토큰입니다.")
            return None

    authenticated_user_id = get_user_id_from_token(token)

    if authenticated_user_id == user_id:
        print("권한이 없습니다.")
        return

    data_url = f"https://newteamsgoody.shop/api/bucket/all/{user_id}"
    headers = {
        "Authorization": f"{token}",
        "Content-Type": "application/json"
    }
    data_response = requests.get(data_url, headers=headers)  
    if data_response.status_code == 200:
        data_content = data_response.json()
        print("\n 조회된 데이터 : ")
        print(json.dumps(data_content, ensure_ascii=False, indent=4))
        user_url = f"https://newteamsgoody.shop/user/{user_id}"
        user_response = requests.get(user_url, headers=headers)
        if user_response.status_code == 200:
            user_data = user_response.json()
            nickname = user_data.get("nickname", "사용자")
            prompt = (
                f"{nickname}님 안녕하세요!로 문장을 시작해줘. "
                "이 사용자는 헬스하는 것을 좋아해요."
                "현재 조회된 버킷리스트 데이터에서 제목과 내용을 분석하여 현재 사용자의 취향에 맞는 버킷리스트를 추천해 주세요."
                "관련된 버킷리스트의 제목을 보여주세요."
                "그리고 왜 추천하는지 그 이유는 짧게 간단히 설명해주세요."
            )
            data = {
                "model": "gemini-1.5-flash-latest",
                "contents": [
                    {
                        "parts": [
                            {"text": prompt},
                            {"text": f"\n 사용자 데이터 : {data_content}"},
                            {"text": f"\n 유저 Id : {user_id}"},
                            {"text": f"\n 유저 닉네임 : {nickname}"}
                        ]
                    }
                ]
            }
            # print("\n 입력된 요청 : ", prompt)
            gemini_response = requests.post(f"{gemini_endpoint}?key={gemini_api_key}", json=data, headers=headers)

            if gemini_response.status_code == 200:
                result = gemini_response.json()
                print("\n AI 응답 : ", result["candidates"][0]["content"])
            else:
                print(f"Gemini API 호출 실패 : {gemini_response.status_code}, 메시지 : {gemini_response.text}")
        else:
            print(f"사용자 조회 실패 : 상태 코드 {user_response.status_code}, 메시지 : {user_response.text}")
    else:
        print(f"데이터 조회 실패 : 상태 코드 {data_response.status_code}, 메시지 : {data_response.text}")
if __name__ == "__main__":
    uid = input("\n 조회할 uid를 입력하세요 : ")
    password = input("비밀번호를 입력하세요 : ")
    token, user_info = login(uid, password)
    if token:
        get_user_data(uid, token)
