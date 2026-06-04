import logging
import os
from typing import List, Dict
import pandas as pd


log_dir = os.path.join(os.path.dirname(__file__), '..', 'logs')
os.makedirs(log_dir, exist_ok=True)

logger = logging.getLogger('src.file_reader')
logger.setLevel(logging.DEBUG)

handler = logging.FileHandler(os.path.join(log_dir, 'file_reader.log'), mode='w')
handler.setLevel(logging.DEBUG)

formatter = logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)
handler.setFormatter(formatter)

logger.addHandler(handler)


def read_csv_to_dicts(file_path: str) -> List[Dict]:
    """Считывает финансовые операции из CSV-файла"""
    logger.info(f"Чтение CSV-файла: {file_path}")
    try:
        df = pd.read_csv(file_path)
        result = df.to_dict(orient='records')
        logger.debug(f"Успешно считано {len(result)} строк из CSV.")
        return result
    except Exception as e:
        logger.error(f"Ошибка при чтении CSV-файла '{file_path}': {e}")
        return []


def read_excel_to_dicts(file_path: str) -> List[Dict]:
    """Считывает финансовые операции из Excel-файла (.xlsx)"""
    logger.info(f"Чтение Excel-файла: {file_path}")
    try:
        df = pd.read_excel(file_path)
        result = df.to_dict(orient='records')
        logger.debug(f"Успешно считано {len(result)} строк из Excel.")
        return result
    except Exception as e:
        logger.error(f"Ошибка при чтении Excel-файла '{file_path}': {e}")
        return []
