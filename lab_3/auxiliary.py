import csv
import logging
import os


logging.basicConfig(level=logging.DEBUG)


def create_folder(data_folder: str) -> None:
    try:
        if not os.path.exists(data_folder):
            os.mkdir(data_folder)
    except OSError as e:
        logging.exception(f"OS error: {e}")


def write_csv(data_folder: str,
              name_csv: str,
              heading: list,
              parsered_data: list) -> None:
    create_folder(data_folder)
    with open(f'{os.path.join(data_folder, name_csv)}.csv',
              'w',
              encoding='utf-8') as f:
        csv_writer = csv.writer(f)
        csv_writer.writerow(heading)
        csv_writer.writerows(parsered_data)
