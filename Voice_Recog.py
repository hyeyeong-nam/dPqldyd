import speech_recognition as sr
from STT_test import kakao_stt, KAKAO_APP_KEY
class voice_recog:
    def get_speech(self):
        
    # 마이크에서 음성을 추출하는 객체
        recognizer = sr.Recognizer()

    # 마이크 설정
        microphone = sr.Microphone(sample_rate=16000)

    # 마이크 소음 수치 반영
        with microphone as source:
            recognizer.adjust_for_ambient_noise(source)
            

    # 음성 수집
        with microphone as source:
            result = recognizer.listen(source)
            audio = result.get_raw_data()

        return audio
    
    def kakao_voice(self):
        audio = self.get_speech()
        text = kakao_stt(KAKAO_APP_KEY, "stream", audio)
        return text