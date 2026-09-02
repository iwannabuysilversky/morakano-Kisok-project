# src/main.py
# 일단 식당은 시끄러워서 음성인식에 어려움이 있음

from order_manager import display_menu, confirm_order
from stt import get_user_voice_input
from llm import process_order_with_llm

def main():
    print("morakano 키오스크 시스템을 시작합니다")
    
    while True:
        # A. 메뉴 화면 출력
        display_menu()
        
        # B. 사용자 음성 입력 대기 및 텍스트 변환 
        user_text = get_user_voice_input()
        
        if user_text.strip() == "종료":
            print("시스템을 종료합니다.")
            break
            
        # C. AI에게 텍스트 전달 및 주문 내역 JSON 파싱
        print("\n[시스템] AI가 주문을 분석 중입니다...")
        order_json = process_order_with_llm(user_text)
        
        # A. 사용자 주문 확인 및 정정 루프
        is_confirmed = confirm_order(order_json)


        # 결제 완료 후 다음 손님을 위해 다시 루프 시작
        if is_confirmed:

            print("결제 해주세요")
            print("했다치고")
            print("주문끝")
            print("==========================================\n")
            break
        else:
            #처음부터 다시 받는 옵션 말고 일부 수정한다던가 그냥 주문을 그만 둔다던가 하는 옵션도 필요함 일단 미구현
            print("\n 주문을 처음부터 다시 받습니다.\n")

if __name__ == "__main__":
    main()