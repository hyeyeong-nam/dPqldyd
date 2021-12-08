import requests
import json

# 함수 정의부
def kakao_stt(app_key, stype, data):
    if stype == 'file':
        filename = data
        with open(filename, "rb") as fp:
            audio = fp.read()
    else:
        audio =data

    headers = {
        "Content-Type": "application/octet-stream",
        "Authorization": "KakaoAK " + app_key,
    }

    # 카카오 음성 url
    kakao_speech_url = "https://kakaoi-newtone-openapi.kakao.com/v1/recognize"
    # 카카오 음성 api 요청
    res = requests.post(kakao_speech_url, headers=headers, data=audio)
    # 요청에 실패했다면,
    if res.status_code != 200:
        text=""
        print("error! because ", res.json())
    else: # 성공했다면,
        result = res.text[res.text.index('{"type":"finalResult"'):res.text.rindex('}')+1]
        text = json.loads(result).get('value')
    return text

# 함수 호출부
KAKAO_APP_KEY = "e434ec843f36bf9e271b5942731dedbe"

