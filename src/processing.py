def filter_by_state(items: list[dict], state_value: str = "EXECUTED") -> list[dict]:
    """Функция, которая фильтрует список словарей по значению ключа 'state'"""

    return [item for item in items if item.get("state") == state_value]


def sort_by_date(items: "list[dict]", reverse: bool = True) -> "list[dict]":
    """Функция, которая сортирует список словарей по ключу 'date''"""

    return sorted(items, key=lambda x: x["date"], reverse=reverse)
