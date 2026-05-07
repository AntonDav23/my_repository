import re
from datetime import datetime
from masks import get_mask_account, get_mask_card_number


def mask_account_card(input_str: str) -> str:
    """Функция обрабатывает информацию как о картах, так и о счетах"""
    card_match = re.search(r"\b\d{16}\b", input_str)

    if card_match:
        card_number = card_match[0]
        masked_card = get_mask_card_number(card_number)
        return input_str.replace(card_number, masked_card)

    account_match = re.search(r"Счет (\d+)", input_str)

    if account_match:
        account_number = account_match[1]
        masked_account = get_mask_account(account_number)
        return input_str.replace(account_number, masked_account)

    return input_str


def get_date(date_string: str) -> str:
    """Функция меняет формат даты"""
    date_object = datetime.strptime(date_string, "%Y-%m-%dT%H:%M:%S.%f")
    return date_object.strftime("%d.%m.%Y")