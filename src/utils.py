import json
import logging
import os
from typing import Dict, List

# НАСТРОЙКА ЛОГГЕРА ДЛЯ МОДУЛЯ utils
log_dir = os.path.join(os.path.dirname(__file__), "..", "logs")
os.makedirs(log_dir, exist_ok=True)

logger = logging.getLogger("src.utils")
logger.setLevel(logging.DEBUG)

file_handler = logging.FileHandler(os.path.join(log_dir, "utils.log"), mode="w")
file_handler.setLevel(logging.DEBUG)

formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s", datefmt="%Y-%m-%d %H:%M:%S")
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)


def load_transactions_from_json(file_path: str) -> List[Dict]:
    """
    Загружает данные о транзакциях из JSON-файла"""
    try:
        logger.info(f"Попытка загрузки данных из файла: {file_path}")
        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)
            if isinstance(data, list):
                logger.info(f"Данные успешно загружены. Количество транзакций: {len(data)}")
                return data
            else:
                logger.warning(f"Файл {file_path} не содержит список. Возвращен пустой список.")
                return []
    except FileNotFoundError:
        logger.error(f"Файл не найден: {file_path}")
        return []
    except json.JSONDecodeError as e:
        logger.error(f"Ошибка декодирования JSON в файле {file_path}: {e}")
        return []
