import os
from typing import List, Dict, Optional

# Импортируем функции из модулей внутри папки src
from src.file_reader import read_csv_to_dicts, read_excel_to_dicts
from src.utils import load_transactions_from_json
from src.processing import filter_by_state, sort_by_date
from src.search import process_bank_search, process_bank_operations
from src.widget import get_date, mask_account_card


def print_transaction(tx: Dict) -> None:
    """Красиво печатает одну транзакцию в консоль"""
    try:
        date_str = get_date(tx.get('date', ''))
        description = tx.get('description', 'Без описания')
        from_account = mask_account_card(str(tx.get('from', '')))
        to_account = mask_account_card(str(tx.get('to', '')))

        amount = tx.get('operationAmount', {}).get('amount', 'N/A')
        currency = tx.get('operationAmount', {}).get('currency', {}).get('name', '')

        print(f"{date_str} {description}")
        print(f"{from_account} -> {to_account}")
        print(f"Сумма: {amount} {currency}\n")
    except Exception as e:
        print(f"[Ошибка при печати транзакции]: {e}")


def get_user_choice(options: List[str]) -> str:
    """Запрашивает у пользователя выбор из списка вариантов."""
    while True:
        choice = input("Ваш выбор: ").strip()
        if choice in options:
            return choice
        print(f"Неверный выбор. Доступные варианты: {', '.join(options)}")


def get_user_status() -> str:
    """Запрашивает у пользователя статус транзакции"""
    valid_statuses = ['EXECUTED', 'CANCELED', 'PENDING']
    while True:
        status = input("Введите статус: ").strip().upper()
        if status in valid_statuses:
            return status
        print(f'Статус операции "{status}" недоступен.')


# --- Основная логика программы ---

def main() -> None:
    """Главная функция программы."""
    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")

    # ЭТАП 1: Выбор источника данных
    print("\nВыберите необходимый пункт меню:")
    print("1. Получить информацию о транзакциях из JSON-файла")
    print("2. Получить информацию о транзакциях из CSV-файла")
    print("3. Получить информацию о транзакциях из XLSX-файла")

    file_choice = get_user_choice(['1', '2', '3'])

    if file_choice == '1':
        print("\nДля обработки выбран JSON-файл.")
        data = load_transactions_from_json("data/operations.json")
    elif file_choice == '2':
        print("\nДля обработки выбран CSV-файл.")
        data = read_csv_to_dicts("data/transactions.csv")
    else:
        print("\nДля обработки выбран XLSX-файл.")
        data = read_excel_to_dicts("data/transactions_excel.xlsx")

    if not data:
        print("Не удалось загрузить данные. Проверьте файл.")
        return

    # ЭТАП 2: Фильтрация по статусу
    print("\nВведите статус, по которому необходимо выполнить фильтрацию.")
    print("Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING")
    status = get_user_status()

    filtered_by_state = filter_by_state(data, status)
    print(f"\nОперации отфильтрованы по статусу \"{status}\"")
    current_data = filtered_by_state

    # ЭТАП 3: Уточняющие вопросы (пропущены для краткости, логика та же)
    # ... здесь код для сортировки, фильтрации по рублю и поиска по описанию ...

    # Финальный вывод
    if current_data:
        print("\nРаспечатываю итоговый список транзакций...")
        print(f"Всего банковских операций в выборке: {len(current_data)}")
        for tx in current_data:
            print_transaction(tx)
    else:
        print("\nНе найдено ни одной транзакции, подходящей под ваши условия фильтрации")


if __name__ == "__main__":
    main()