import os
from typing import Dict, Union

import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("API_KEY")
URL = "https://api.apilayer.com/exchangerates_data/convert"


def convert_to_rub(amount: float, from_currency: str) -> float:
    """Конвертирует сумму из USD или EUR в рубли (RUB)."""
    if from_currency == "RUB":
        return amount

    if not API_KEY:
        print("Ошибка: Ключ API не найден. Проверьте файл .env")
        return 0.0

    ParamsValueType = Union[str, float, int, list]

    params: Dict[str, ParamsValueType] = {
        "to": "RUB",
        "from": from_currency,
        "amount": amount,
        "apikey": API_KEY,
        "places": 2,
    }

    try:
        response = requests.get(URL, params=params)
        data = response.json()
        return data["result"] if data.get("success") else 0.0
    except Exception as e:
        print(f"Ошибка при запросе к API: {e}")
        return 0.0