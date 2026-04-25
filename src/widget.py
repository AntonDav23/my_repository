def mask_account_card(process_info: str) -> str:
    """Функция обрабатывает информацию как о картах, так и о счетах"""
    len_list = len(process_info)
    if len_list == 30:
        mask_numbers = f"{process_info[:4]} {process_info[5:13]} {process_info[14:18]} {process_info[19:21]} ** ***** {process_info[-4:]}"
    if len_list == 24:
        mask_numbers = f"{process_info[:7]} {process_info[8:12]} {process_info[13:15]} ** **** {process_info[-4:]}"
    if len_list == 25:
        mask_numbers = f"{process_info[:5]} ** {process_info[-4:]}"
    return mask_numbers

from datetime import datetime

def get_date(format_date: str) -> str:
    """Функция меняет формат даты"""
    date_object = datetime.strptime(format_date, '%Y-%m-%dT%H:%M:%S.%f')
    return date_object.strftime('%d.%m.%Y')
