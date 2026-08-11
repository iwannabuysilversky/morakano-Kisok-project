# src/order_manager.py

# 메뉴판 출력
def display_menu():

    # json으로 이쁘게 출력권장 -> 메뉴 수정도 편함
    print("\n================ 📋 메뉴판 ================")
    print("1. 햄버거(4,500원)")
    print("2. 오징어 (5,000원)")
    print("3. 콜라 (5,500원)")
    print("==========================================")


def confirm_order(order_data: dict) -> bool:
    """
    JSON 데이터를 예쁘게 출력하고 정정 여부를 묻는 함수 필요
    """
    print("\n[시스템] 주문하신 내역을 확인해 주세요:")
    orders = order_data.get("orders", [])
    
    for item in orders:
        menu = item.get("menu")
        qty = item.get("qty")
        req = ", ".join(item.get("requests", []))
        req_text = f" (요청사항: {req})" if req else ""
        
        print(f" - {menu} {qty}개{req_text}")
        
    print("\n이대로 주문 진행할까요? (네/아니오)")
    answer = input("👉 사용자 응답: ")

    #일단 이렇게 해놓는데 부분수정이나 다시듣기 이런거에 따라서 달라질 수 있음 그런 로직도 해주길 권장함
    if "네" in answer or "맞" in answer or "응" in answer:
        return True
    else:
        return False