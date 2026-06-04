import logging
import os

# НАСТРОЙКА ЛОГГЕРА ДЛЯ МОДУЛЯ masks

log_dir = os.path.join(os.path.dirname(__file__), "..", "logs")
os.makedirs(log_dir, exist_ok=True)

logger = logging.getLogger("src.masks")
logger.setLevel(logging.DEBUG)

file_handler = logging.FileHandler(os.path.join(log_dir, "masks.log"), mode="w")
file_handler.setLevel(logging.DEBUG)

formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s", datefmt="%Y-%m-%d %H:%M:%S")
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)


def get_mask_card_number(card_number: str) -> str:
    """Функция, которая форматирует номер банковской карты"""
    try:
        card_number_str = str(card_number).strip()
        masked_card = f"{card_number_str[:4]} {card_number_str[4:6]}** **** {card_number_str[-4:]}"
        logger.info(f"Номер карты успешно замаскирован. Исходный: {card_number}")
        return masked_card
    except Exception as e:
        logger.error(f"Ошибка при маскировке карты: {e}")
        return "**ОШИБКА**"


def get_mask_account(account_number: str) -> str:
    """Функция, которая маскирует номер банковского счета"""
    try:
        account_number_str = str(account_number).strip()
        mask_account = f"**{account_number_str[-4:]}"
        logger.info(f"Номер счета успешно замаскирован. Исходный: {account_number}")
        return mask_account
    except Exception as e:
        logger.error(f"Ошибка при маскировке счета: {e}")
        return "**ОШИБКА**"
