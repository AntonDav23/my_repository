from functools import wraps
from datetime import datetime
from typing import Any, Callable, Optional


def log(filename: Optional[str] = None) -> Callable[..., Any]:
    """
    Декоратор для логирования времени вызова, аргументов и результата.
    """

    def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            call_time = datetime.now().strftime("%H:%M:%S")
            args_info = f"args: {str(args)}, kwargs: {str(kwargs)}"

            try:
                result = func(*args, **kwargs)
                success_msg = f"[{call_time}] {func.__name__} ok | {args_info} | result: {str(result)}"
                _write_log(success_msg, filename)
                return result

            except Exception as e:
                error_msg = f"[{call_time}] {func.__name__} error: {type(e).__name__} | {args_info}"
                _write_log(error_msg, filename)
                raise

        return wrapper

    return decorator


def _write_log(message: str, filename: Optional[str]) -> None:
    """Записывает сообщение в файл или выводит в консоль."""
    if filename:
        with open(filename, 'a', encoding='utf-8') as f:
            f.write(message + '\n')
    else:
        print(message)
