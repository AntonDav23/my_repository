import pandas
import pytest
from src.file_reader import read_csv_to_dicts, read_excel_to_dicts


def test_read_csv_to_dicts_success(mocker):
    """
    Тест: read_csv_to_dicts успешно вызывает pandas.read_csv и возвращает результат.
    """
    expected_data = [
        {"id": "1", "amount": "100.50", "currency": "USD"},
        {"id": "2", "amount": "200.00", "currency": "EUR"}
    ]

    mock_df = mocker.Mock()
    mock_df.to_dict.return_value = expected_data

    mocker.patch('pandas.read_csv', return_value=mock_df)

    result = read_csv_to_dicts("data/transactions.csv")

    assert result == expected_data

    pandas.read_csv.assert_called_once_with("data/transactions.csv")


def test_read_csv_to_dicts_pandas_error(mocker):
    """
    Тест: read_csv_to_dicts корректно обрабатывает ошибку внутри pandas.
    """
    mocker.patch('pandas.read_csv', side_effect=Exception("Ошибка парсинга CSV"))
    result = read_csv_to_dicts("data/broken.csv")
    assert result == []


def test_read_excel_to_dicts_success(mocker):
    """
    Тест: read_excel_to_dicts успешно вызывает pandas.read_excel и возвращает результат.
    """
    expected_data = [{"id": "101", "amount": "500", "currency": "RUB"}]

    mock_df = mocker.Mock()
    mock_df.to_dict.return_value = expected_data

    mocker.patch('pandas.read_excel', return_value=mock_df)

    result = read_excel_to_dicts("data/transactions.xlsx")

    assert result == expected_data
    pandas.read_excel.assert_called_once_with("data/transactions.xlsx")


def test_read_excel_to_dicts_pandas_error(mocker):
    """
    Тест: read_excel_to_dicts корректно обрабатывает ошибку внутри pandas.
    """
    mocker.patch('pandas.read_excel', side_effect=Exception("Файл Excel поврежден"))
    result = read_excel_to_dicts("data/broken.xlsx")
    assert result == []
