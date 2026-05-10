import pytest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


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


def test_filter_by_currency_iterator(sample_transactions) -> None:
    usd_transactions = filter_by_currency(sample_transactions, "USD")
    assert next(usd_transactions)["id"] == 939719570


def test_transaction_descriptions(sample_transactions) -> None:
    descriptions = transaction_descriptions(sample_transactions)
    assert next(descriptions) == "Перевод организации"


def test_card_number_generator_basic() -> None:
    result = list(card_number_generator(1, 5))
    expected = [
        "0000 0000 0000 0001",
        "0000 0000 0000 0002",
        "0000 0000 0000 0003",
        "0000 0000 0000 0004",
        "0000 0000 0000 0005",
    ]
    assert result == expected
