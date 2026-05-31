from typing import Dict, Union
from external_api import convert_to_rub


def filter_by_state(items: list[dict], state_value: str = "EXECUTED") -> list[dict]:
    """Функция, которая фильтрует список словарей по значению ключа 'state'"""

    return [item for item in items if item.get("state") == state_value]


def sort_by_date(items: "list[dict]", reverse: bool = True) -> "list[dict]":
    """Функция, которая сортирует список словарей по ключу 'date''"""

    return sorted(items, key=lambda x: x["date"], reverse=reverse)


def get_transaction_amount_in_rub(transaction: Dict) -> Union[float, None]:
    """Возвращает сумму одной транзакции в рублях."""
    try:
        amount = float(transaction['operationAmount']['amount'])
        currency = transaction['operationAmount']['currency']['code']
        return convert_to_rub(amount, currency)
    except (KeyError, ValueError):
        # KeyError - если ключа нет в словаре
        # ValueError - если amount не является числом
        return None
