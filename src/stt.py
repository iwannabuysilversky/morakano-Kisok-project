import re
import speech_recognition as sr

def clean_korean_text(text: str) -> str:
    # 1. '장' 오인식 보정 (10장 -> 10잔)
    text = re.sub(r'(\d+)\s*장(?=[ 은는이가을를만도.,!?]|$)', r'\1잔', text)
    korean_numbers = r'(한|두|세|네|다섯|여섯|일곱|여덟|아홉|열|열한|열두|열세|열네|열다섯|스무|스물둘|스물두)'
    text = re.sub(rf'({korean_numbers})\s*장(?=[ 은는이가을를만도.,!?]|$)', r'\1잔', text)
    
    # 2. 음료 뒤에 단위 없이 숫자만 붙은 경우 '잔' 보완 (예: "아메리카노 22" -> "아메리카노 22잔")
    text = re.sub(r'(\d+)(?=\s*$|\s+(?:주세요|줘|부탁|결제))', r'\1잔', text)
    
    return text

def get_user_voice_input() -> str:
    recognizer = sr.Recognizer()
    
    # 말 사이의 딜레이 1.5초까지 기다려줌 (초 조정가능)
    recognizer.pause_threshold = 1.5 
    
    messages = {
        sr.WaitTimeoutError: "말씀이 없어 대기 시간이 초과되었습니다.",
        sr.UnknownValueError: "음성을 정확하게 인식하지 못했습니다. 다시 말씀해 주세요.",
    }

    with sr.Microphone() as source:
        print("\n🎙️ 주변 소음 측정 중...")
        recognizer.adjust_for_ambient_noise(source, duration=0.8)

        print("🎧 듣고 있습니다. 주문을 말씀해 주세요! (대기 시간 10초)")
        try:
            # timeout=10 (10초간 말 시작 대기 잡음이나 주변 소음 잡힐 시 시간 카운팅), phrase_time_limit=15 (최대 15초 동안 말 가능)
            audio = recognizer.listen(source, timeout=10, phrase_time_limit=15)
            user_input = recognizer.recognize_google(audio, language="ko-KR")
            
            refined_input = clean_korean_text(user_input.strip())
            print(f"✅ 인식 결과: {refined_input}")
            return refined_input

        except (sr.WaitTimeoutError, sr.UnknownValueError) as e:
            print(f"⚠️ {messages[type(e)]}")
        except sr.RequestError as e:
            print(f"❌ STT 서비스 연결 실패: {e}")

    return ""

if __name__ == "__main__":
    result = get_user_voice_input()
    print(f"\n👉 최종 텍스트: '{result}'" if result else "\n❌ 음성 인식 실패")