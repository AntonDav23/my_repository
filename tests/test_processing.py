import pytest

from src.processing import filter_by_state, sort_by_date


def test_filter_by_state_default(sample_transactions: list[dict]) -> None:
    """Проверяет фильтрацию по умолчанию (статус EXECUTED)."""
    result = filter_by_state(sample_transactions)
    assert len(result) == 2
    assert all(item["state"] == "EXECUTED" for item in result)


def test_filter_by_state_custom(sample_transactions: list[dict]) -> None:
    """Проверяет фильтрацию по заданному статусу (CANCELED)."""
    result = filter_by_state(sample_transactions, state_value="CANCELED")
    assert len(result) == 1
    assert result[0]["id"] == 2


def test_filter_by_state_not_found(sample_transactions: list[dict]) -> None:
    """Проверяет поведение, если статус не найден в списке."""
    result = filter_by_state(sample_transactions, state_value="REFUNDED")
    assert result == []


def test_sort_by_date_desc(sample_transactions: list[dict]) -> None:
    """Проверяет сортировку по убыванию (от новых к старым)."""
    result = sort_by_date(sample_transactions)
    # Самая поздняя дата (id=3) должна быть первой в списке
    assert result[0]["id"] == 3


def test_sort_by_date_asc(sample_transactions: list[dict]) -> None:
    """Проверяет сортировку по возрастанию (от старых к новым)."""
    result = sort_by_date(sample_transactions, reverse=False)
    # Самая ранняя дата (id=1) должна быть первой в списке
    assert result[0]["id"] == 1


def test_sort_by_date_same_dates(sample_transactions: list[dict]) -> None:
    """Проверяет стабильность сортировки при одинаковых датах."""
    result = sort_by_date(sample_transactions)

    index_3 = next(i for i, item in enumerate(result) if item["id"] == 3)
    index_4 = next(i for i, item in enumerate(result) if item["id"] == 4)

    assert index_3 < index_4
