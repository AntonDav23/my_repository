import pytest
from src.search import process_bank_search, process_bank_operations


def test_search_found_case_insensitive():
    """Тест: Поиск находит совпадение независимо от регистра букв"""
    data = [{"id": 1, "description": "Перевод в МОСКВУ"}]
    result = process_bank_search(data, "москв")
    assert len(result) == 1
    assert result[0]["id"] == 1


def test_search_not_found():
    """Тест: Если совпадений нет, возвращается пустой список"""
    data = [{"id": 1, "description": "Оплата телефона"}]
    result = process_bank_search(data, "аренда")
    assert result == []


def test_search_empty_data():
    """Тест: Если на вход подан пустой список данных, возвращается пустой список"""
    data = []
    result = process_bank_search(data, "что угодно")
    assert result == []


def test_search_with_regex_digit():
    """Тест: Функция корректно обрабатывает регулярные выражения"""
    data = [{"id": 1, "description": "Цена товара: 100.50$\""}]

    result = process_bank_search(data, r"\d")

    assert result != []
    assert len(result) == 1


def test_count_operations_by_categories():
    """Тест: Функция правильно подсчитывает количество операций для каждой категории"""
    data = [
        {"id": 1, "description": "Перевод в МОСКВУ и оплата ЖКХ"},
        {"id": 2, "description": "Снятие наличных в банкомате"},
        {"id": 3, "description": "Покупка в магазине продуктов"},
        {"id": 4, "description": "Прочая операция"}
    ]
    categories = ["ПЕРЕВОД", "ОПЛАТА", "СНЯТИЕ", "ПОКУПКА"]
    expected_result = {
        "ПЕРЕВОД": 1,
        "ОПЛАТА": 1,
        "СНЯТИЕ": 1,
        "ПОКУПКА": 1
    }
    result = process_bank_operations(data, categories)
    assert result == expected_result


def test_count_operations_no_matches():
    """Тест: Если ни одна категория не найдена, возвращается словарь с нулями"""
    data = [{"id": 1, "description": "Прочая операция"}]
    categories = ["ЕДА", "ТРАНСПОРТ"]
    expected_result = {"ЕДА": 0, "ТРАНСПОРТ": 0}
    result = process_bank_operations(data, categories)
    assert result == expected_result


def test_count_operations_empty_data():
    """Тест: Если на вход подан пустой список транзакций, возвращаются нули"""
    data = []
    categories = ["ЛЮБАЯ"]
    expected_result = {"ЛЮБАЯ": 0}
    result = process_bank_operations(data, categories)
    assert result == expected_result
