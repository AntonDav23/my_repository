import pytest

from src.decorators import log


@pytest.fixture(autouse=True)
def cleanup_logfile() -> None:
    try:
        open("test_log.txt", "w").close()
    except Exception:
        pass


def test_log_success_prints_to_console(capsys) -> None:
    """
    Проверяет, что успешное выполнение декорированной функции
    приводит к выводу лога в консоль (stdout).
    """

    @log()
    def add(x, y):
        return x + y

    add(5, 3)
    captured = capsys.readouterr()

    assert captured.out != ""
    assert "add ok" in captured.out
    assert "result: 8" in captured.out


def test_log_error_prints_to_console(capsys) -> None:
    """
    Проверяет, что при возникновении исключения внутри декорированной функции
    в консоль выводится сообщение об ошибке.
    """

    @log()
    def divide(x, y):
        return x / y

    with pytest.raises(ZeroDivisionError):
        divide(10, 0)

    captured = capsys.readouterr()
    assert "divide error: ZeroDivisionError" in captured.out
    assert "args: (10, 0)" in captured.out
    assert "result:" not in captured.out


def test_log_success_writes_to_file() -> None:
    """
    Проверяет, что успешное выполнение декорированной функции
    приводит к записи лога в указанный файл.
    """

    @log(filename="test_log.txt")
    def multiply(x, y):
        return x * y

    multiply(2, 7)

    with open("test_log.txt", "r", encoding="utf-8") as f:
        content = f.read()
        assert "multiply ok" in content
        assert "result: 14" in content


def test_log_error_writes_to_file() -> None:
    """Проверяем, что ошибка записывает сообщение в файл."""

    @log(filename="test_log.txt")
    def get_value(data, key):
        return data[key]

    with pytest.raises(KeyError):
        get_value({}, "missing_key")

    with open("test_log.txt", "r", encoding="utf-8") as f:
        content = f.read()

        assert "get_value error: KeyError" in content
        assert "args: ({}, 'missing_key')" in content
        assert "kwargs: {}" in content


def test_preserves_function_name_and_doc() -> None:
    """
    Проверяет, что декоратор корректно сохраняет метаданные исходной функции.
    """

    @log()
    def my_func():
        """Важная документация функции."""
        pass

    assert my_func.__name__ == "my_func"
    assert my_func.__doc__ == "Важная документация функции."
