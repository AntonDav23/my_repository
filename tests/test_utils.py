import json
import pytest

from src.utils import load_transactions_from_json
from src.processing import get_transaction_amount_in_rub


def test_load_transactions_success(monkeypatch):
    """Тест: Успешная загрузка данных из существующего файла."""
    mock_data = [{"id": 1}]


    from unittest.mock import mock_open

    monkeypatch.setattr('builtins.open', mock_open(read_data=json.dumps(mock_data)))

    result = load_transactions_from_json('fake_path.json')

    assert result == mock_data


def test_load_transactions_file_not_found():
    """Тест: Возвращает пустой список, если файл не найден."""
    result = load_transactions_from_json('missing.json')
    assert result == []


def test_ruble_transaction():
    """Тест: Если валюта RUB, сумма не меняется."""
    transaction = {
        "operationAmount": {
            "amount": "1500",
            "currency": {"code": "RUB"}
        }
    }
    assert get_transaction_amount_in_rub(transaction) == 1500.0


def test_usd_transaction(monkeypatch):
    """Тест: USD конвертируется через API."""

    def mock_get(*args, **kwargs):
        """Заглушка для ответа API."""

        class MockResponse:
            def json(self):
                return {"success": True, "result": 9500.0}

        return MockResponse()

    monkeypatch.setattr('requests.get', mock_get)

    transaction = {
        "operationAmount": {
            "amount": "100",
            "currency": {"code": "USD"}
        }
    }

    assert get_transaction_amount_in_rub(transaction) == 9500.0


def test_broken_transaction():
    """Тест: Если структура данных неверна, возвращается None."""
    broken = {"operationAmount": {}}
    assert get_transaction_amount_in_rub(broken) is None


def test_amount_not_number():
    """Тест: Если amount не число, возвращается None."""
    broken = {
        "operationAmount": {
            "amount": "abc",
            "currency": {"code": "RUB"}
        }
    }
    assert get_transaction_amount_in_rub(broken) is None