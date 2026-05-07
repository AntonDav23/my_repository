import pytest
from src.masks import get_mask_account, get_mask_card_number


def test_get_mask_card_number_standard() -> None:
    """Проверяет стандартную маску для 16-значной карты."""
    card: str = "7000792289606361"
    expected: str = "7000 79** **** 6361"
    assert get_mask_card_number(card) == expected


@pytest.mark.parametrize("invalid_input", ["7000", "", None,])
# ---------------------------------------------
def test_get_mask_card_number_invalid(invalid_input) -> None:
    """Проверяет, что функция возвращает предсказуемый результат на некорректных данных."""
    result = get_mask_card_number(invalid_input)

    assert result != "7000 79** **** 6361"


def test_get_mask_account_standard() -> None:
    """Проверяет стандартную маску для номера счета."""
    account: str = "73654108430135874305"
    expected: str = "**4305"
    assert get_mask_account(account) == expected


def test_get_mask_account_short() -> None:
    """Проверяет маску для очень короткого 'номера счета'."""
    account: str = "12"
    expected: str = "**12"
    assert get_mask_account(account) == expected