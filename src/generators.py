from typing import Generator


def filter_by_currency(transactions: list, currency_code: str) -> "Generator":
    """
    Фильтрует транзакции по коду валюты и возвращает итератор.
    """
    for transaction in transactions:
        currency = transaction.get("operationAmount", {}).get("currency", {})
        if currency.get("code") == currency_code:
            yield transaction


def transaction_descriptions(transactions: list) -> "Generator":
    """
    Генератор, который возвращает описание каждой транзакции.
    """
    for transaction in transactions:
        yield transaction.get("description", "")


def card_number_generator(start: int = 1, end: int = 9999_9999_9999_9999) -> "Generator":
    """
    Генератор, который выдает номера банковских карт в заданном диапазоне.
    Номера генерируются в формате XXXX XXXX XXXX XXXX.
    """
    for number in range(start, end + 1):
        num_str = f"{number:016d}"
        formatted = f"{num_str[:4]} {num_str[4:8]} {num_str[8:12]} {num_str[12:]}"
        yield formatted
