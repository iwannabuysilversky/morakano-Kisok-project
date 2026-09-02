# src/llm.py

def process_order_with_llm(user_text: str) -> dict:
    """
    OpenAI API를 호출하여 프롬프트 엔지니어링 후 JSON 반환

    """
    
    # 임시 테스트용 메뉴와 양, 요청사항

    mock_response = {
        "orders": [
            {"menu": "아메리카노", "qty": 2, "requests": ["얼음 적게"]}
        ]
    }
    
    return mock_response