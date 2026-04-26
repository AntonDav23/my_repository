import re

from masks import get_mask_account, get_mask_card_number


def mask_account_card(input_str: str) -> str:
    """Функция обрабатывает информацию как о картах, так и о счетах"""
    card_match = re.search(r"\b\d{16}\b", input_str)

    if card_match:
        card_number = card_match[0]
        masked_card = get_mask_card_number(card_number)

        parts = masked_card.split(" ")

        final_masked_card = f"{parts[0]} {parts[1]}** **** {parts[2]}"

        return input_str.replace(card_number, final_masked_card)

    account_match = re.search(r"Счет (\d+)", input_str)

    if account_match:
        account_digits = account_match[1]
        masked_account = get_mask_account(account_digits)
        return input_str.replace(account_digits, masked_account)

    return input_str


from datetime import datetime


def get_date(format_date: str) -> str:
    """Функция меняет формат даты"""
    date_object = datetime.strptime(format_date, "%Y-%m-%dT%H:%M:%S.%f")
    return date_object.strftime("%d.%m.%Y")

if __name__ == "__main__":
    result_card = mask_account_card("Visa Platinum 7000792289606361")
    print(result_card)
    # Выведет: Visa Platinum 7000 79** **** 6361 (Верно!)

    result_account = mask_account_card("Счет 73654108430135874305")
    print(result_account)