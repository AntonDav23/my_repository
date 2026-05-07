import pytest
from src.widget import mask_account_card, get_date


def test_mask_account_card_for_card() -> None:
    """Проверяет, что функция правильно маскирует номер карты в строке."""
    input_text = "Visa Platinum 7000792289606361"
    expected = "Visa Platinum 7000 79** **** 6361"
    assert mask_account_card(input_text) == expected


def test_mask_account_card_for_account() -> None:
    """Проверяет, что функция правильно маскирует номер счета в строке."""
    input_text = "Счет 73654108430135874305"
    expected = "Счет **4305"
    assert mask_account_card(input_text) == expected


def test_get_date_format() -> None:
    """Проверяет изменение формата даты."""
    input_date = "2024-03-11T02:26:18.671407"
    expected = "11.03.2024"
    assert get_date(input_date) == expected


def test_get_date_invalid_format() -> None:
    """Проверяет, что функция падает с понятной ошибкой на неверном формате даты."""
    invalid_date = "11-03-2024"

    with pytest.raises(ValueError):
        get_date(invalid_date)


def test_get_date_empty_input() -> None:
    """Проверяет, что функция корректно обрабатывает пустую строку."""
    empty_input = ""

    with pytest.raises(ValueError):
        get_date(empty_input)