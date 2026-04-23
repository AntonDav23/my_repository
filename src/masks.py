def get_mask_card_number(card_number: str) -> str:
    """Функция, которая маскирует номер банковской карты"""
    card_number_str = str(card_number).strip()
    masked_card = f"{card_number_str[:4]} {card_number_str[4:6]} {card_number_str[-4:]}"

    return masked_card


def get_mask_account(account_number: str) -> str:
    """Функция, которая маскирует номер банковского счета"""
    account_number_str = str(account_number).strip()
    mask_account = f"**{account_number_str[-4:]}"

    return mask_account
