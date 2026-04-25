from masks import get_mask_account, get_mask_card_number


def mask_account_card(process_info: str) -> str:
    """Функция обрабатывает информацию как о картах, так и о счетах"""
    part_name = process_info.split()
    number = part_name[-1]
    together = " ".join(part_name[:-1])
    if together.upper() == "Счет":
        masked_number = get_mask_account(number)
    else:
        masked_number = get_mask_card_number(number)
    return f"{together}{masked_number}"


from datetime import datetime


def get_date(format_date: str) -> str:
    """Функция меняет формат даты"""
    date_object = datetime.strptime(format_date, "%Y-%m-%dT%H:%M:%S.%f")
    return date_object.strftime("%d.%m.%Y")
