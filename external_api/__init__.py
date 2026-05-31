import os
import requests
from dotenv import load_dotenv

# Загружаем переменные окружения из файла .env
load_dotenv()
API_KEY = os.getenv('API_KEY')
API_URL = 'https://api.apilayer.com/exchangerates_data/convert'

def convert_to_rub(amount: float, from_currency: str) -> float:
    """Конвертирует сумму из USD или EUR в рубли (RUB) по текущему курсу."""
    # Если валюта уже рубли, ничего не конвертируем
    if from_currency == 'RUB':
        return amount

    # Проверяем наличие API ключа
    if not API_KEY:
        print("Ошибка: Ключ API не найден. Проверьте файл .env")
        return 0.0

    try:
        response = requests.get(API_URL, params={
            'to': 'RUB',
            'from': from_currency,
            'amount': amount,
            'apikey': API_KEY,
            'places': 2 # Округление до 2 знаков
        })
        data = response.json()
        return data['result'] if data.get('success') else 0.0
    except Exception as e:
        print(f"Ошибка при запросе к API: {e}")
        return 0.0
