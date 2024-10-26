import csv
import logging
import os


logging.basicConfig(level=logging.DEBUG)


def create_folder(data_folder: str) -> None:
    """
    Form a folder
    
    Args:
        data_folder: str
            Название для новой папки
    
    Return:
        None
    """
    try:
        if not os.path.exists(data_folder):
            os.mkdir(data_folder)
    except OSError as e:
        logging.exception(f"OS error: {e}")


def write_csv(data_folder: str,
              name_csv: str,
              heading: list,
              parsered_data: list) -> None:
    """Записывает данные в CSV файл.

    Args:
        data_folder (str): 
            Путь к папке, в которой будет создан файл CSV.
        name_csv (str): 
            Имя файла без расширения, в который будут записаны данные.
        heading (list): 
            Заголовки столбцов для CSV файла.
        parsered_data (list): 
            Данные, которые будут записаны в файл, должны быть в формате списка списков.

    Return:
        None: Функция не возвращает значения, но создает файл CSV в указанной папке.
    """
    create_folder(data_folder)
    with open(f'{os.path.join(data_folder, name_csv)}.csv',
              'w',
              encoding='utf-8') as f:
        csv_writer = csv.writer(f)
        csv_writer.writerow(heading)
        csv_writer.writerows(parsered_data)
