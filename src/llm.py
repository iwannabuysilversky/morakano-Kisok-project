# src/llm.py

import json
import os

from dotenv import load_dotenv
from openai import OpenAI

from order_manager import MENU_DATA


# .env 파일의 API 키와 모델명을 불러옴
load_dotenv()

client = OpenAI()


def process_order_with_llm(user_text: str) -> dict:
    """
    OpenAI API를 호출하여 사용자 주문을 JSON으로 반환
    """

    # order_manager.py의 메뉴판을 AI에게 전달할 문자열로 변환
    menu_json = json.dumps(MENU_DATA, ensure_ascii=False)

    prompt = f"""
    너는 키오스크 주문 분석 AI다.

    메뉴판:
    {menu_json}

    사용자 주문:
    {user_text}

    다음 규칙을 지켜라.
    - 메뉴판에 있는 메뉴만 반환한다.
    - 수량을 말하지 않았다면 1로 처리한다.
    - 요청사항이 없다면 빈 리스트로 반환한다.
    - 설명 없이 반드시 JSON 객체만 반환한다.

    반환 형식:
    {{
        "orders": [
            {{"menu": "메뉴명", "qty": 1, "requests": []}}
        ]
    }}
    """

    response = client.responses.create(
        model=os.getenv("OPENAI_MODEL", "gpt-5.6-luna"),
        input=prompt,
        reasoning={"effort": "none"},
        text={"format": {"type": "json_object"}},
    )

    return json.loads(response.output_text)
