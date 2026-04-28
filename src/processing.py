def filter_by_state(items: list[dict], state_value: str = 'EXECUTED') -> list[dict]:
    """Функция, которая фильтрует список словарей по значению ключа 'state'"""
    return [item for item in items if item.get('state') == state_value]

