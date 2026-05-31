import json
from typing import List, Dict


def load_transactions_from_json(file_path: str) -> List[Dict]:
    """Загружает данные о транзакциях из JSON-файла."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            # Проверяем, что данные являются списком
            return data if isinstance(data, list) else []
    except (FileNotFoundError, json.JSONDecodeError):
        return []
