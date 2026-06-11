import logging
import os
import re
from collections import Counter
from typing import Any, Dict, List

log_dir = os.path.join(os.path.dirname(__file__), "..", "logs")
os.makedirs(log_dir, exist_ok=True)

logger = logging.getLogger("src.search")
logger.setLevel(logging.DEBUG)

handler = logging.FileHandler(os.path.join(log_dir, "search.log"), mode="w")
handler.setLevel(logging.DEBUG)

formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s", datefmt="%Y-%m-%d %H:%M:%S")
handler.setFormatter(formatter)

logger.addHandler(handler)


def process_bank_search(data: List[Dict[str, Any]], search: str) -> List[Dict[str, Any]]:
    """Выполняет поиск подстроки в поле 'description' транзакций с использованием регулярных выражений"""
    logger.info(f"Начало поиска по строке: '{search}'")

    pattern = re.compile(search, re.IGNORECASE)

    result = [tx for tx in data if "description" in tx and pattern.search(tx["description"])]

    logger.debug(f"Поиск завершен. Найдено совпадений: {len(result)}")
    return result


def process_bank_operations(data: List[Dict[str, Any]], categories: List[str]) -> Dict[str, int]:
    """Подсчитывает количество банковских операций для каждой из указанных категорий"""
    logger.info(f"Начало подсчета операций по категориям: {categories}")

    all_descriptions = " ".join(tx.get("description", "").lower() for tx in data)

    found_categories = []
    for category in categories:
        if category.lower() in all_descriptions:
            found_categories.append(category.lower())

    counts = Counter(found_categories)

    result = {category: counts.get(category.lower(), 0) for category in categories}

    logger.info(f"Подсчет завершен. Результат: {result}")
    return result
