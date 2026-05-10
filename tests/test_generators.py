import pytest
from src.generators import (
    filter_by_currency,
    transaction_descriptions,
    card_number_generator
)


@pytest.fixture
def sample_transactions():
    return [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "description": "Перевод организации",
            "operationAmount": {"amount": "9824.07", "currency": {"code": "USD"}},
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "description": "Перевод со счета на счет",
            "operationAmount": {"amount": "79114.93", "currency": {"code": "USD"}},
        },
        {
            "id": 111111111,
            "state": "EXECUTED",
            "date": "2023-01-01T12:00:00",
            "description": "Перевод с карты на карту",
            "operationAmount": {"amount": "5000.00", "currency": {"code": "RUB"}},
        },
    ]


@pytest.mark.parametrize("currency, expected_ids", [
    ("USD", [939719570, 142264268]),  # Проверяем фильтрацию по USD
    ("RUB", [111111111]),  # Проверяем фильтрацию по RUB
    ("EUR", []),  # Проверяем, что нет транзакций в EUR
])
def test_filter_by_currency(sample_transactions, currency, expected_ids) -> None:
    """Проверяет фильтрацию транзакций по разным валютам."""
    filtered = filter_by_currency(sample_transactions, currency)
    result_ids = [tx["id"] for tx in filtered]

    assert result_ids == expected_ids


@pytest.mark.parametrize("expected_descriptions", [
    (["Перевод организации", "Перевод со счета на счет", "Перевод с карты на карту"]),
])
def test_transaction_descriptions(sample_transactions, expected_descriptions) -> None:
    """Проверяет, что генератор выдает описания в правильном порядке."""
    descriptions = transaction_descriptions(sample_transactions)

    # Сравниваем список, полученный из генератора, с ожидаемым списком
    assert list(descriptions) == expected_descriptions


@pytest.mark.parametrize("start, end, expected_first, expected_last", [
    (1, 5, "0000 0000 0000 0001", "0000 0000 0000 0005"),  # Малый диапазон
    (9999_9999_9999_9995, 9999_9999_9999_9999,
     "9999 9999 9999 9995", "9999 9999 9999 9999"),  # Большой диапазон (конец)
])
def test_card_number_generator(start, end, expected_first, expected_last) -> None:
    """Проверяет генерацию номеров карт в заданном диапазоне."""
    gen = card_number_generator(start, end)

    assert next(gen) == expected_first

    result_list = list(gen)
    assert result_list[-1] == expected_last
    assert len(result_list) == (end - start)
