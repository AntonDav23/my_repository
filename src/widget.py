import re
from masks import get_mask_card_number, get_mask_account


def mask_account_card(input_str: str) -> str:
    """Функция обрабатывает информацию как о картах, так и о счетах"""
    card_match = re.search(r'\b\d{16}\b', input_str)

    if card_match:
        card_number = card_match[0]
        masked_card = get_mask_card_number(card_number)
        return input_str.replace(card_number, masked_card)

    account_match = re.search(r'Счет (\d+)', input_str)

    if account_match:
        account_number = account_match[0]
        masked_account = get_mask_account(account_number)
        return input_str.replace(account_number, masked_account)


from datetime import datetime


def get_date(format_date: str) -> str:
    """Функция меняет формат даты"""
    date_object = datetime.strptime(format_date, "%Y-%m-%dT%H:%M:%S.%f")
    return date_object.strftime("%d.%m.%Y")
