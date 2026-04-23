def mask_account_card(proces_inform: str) -> str:
    ''' Функция обрабатывает информацию как о картах, так и о счетах '''
    len_list = len(proces_inform)
    if len_list == 30:
        mask_numbers = f"{proces_inform[:4]} {proces_inform[5:13]} {proces_inform[14:18]} {proces_inform[19:21]} ** ***** {proces_inform[-4:]}"
    if len_list == 24:
        mask_numbers = f"{proces_inform[:7]} {proces_inform[8:12]} {proces_inform[13:15]} ** **** {proces_inform[-4:]}"
    if len_list == 25:
        mask_numbers = f"{proces_inform[:5]} ** {proces_inform[-4:]}"
    return mask_numbers


def get_date(formatting_date: str) -> str:
    '''  Функция меняет формат даты '''
    data = formatting_date[:10]
    new_data = []
    for element in data.split('-'):
        new_data.append(element)
        reversed_new_data = new_data[::-1]
    return '.'.join(reversed_new_data)