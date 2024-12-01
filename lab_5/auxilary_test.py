import csv
import os
import shutil
import pytest

from auxiliary import create_folder, write_csv
TEST_FOLDER = 'test_data'

def test_create_folder():
    """
    Проверяем, что функция create_folder создает папку, если она не существует.
    """
    create_folder(TEST_FOLDER)
    assert os.path.exists(TEST_FOLDER)

    shutil.rmtree(TEST_FOLDER)


def test_write_csv():
    """
    Проверяем, что функция write_csv создает CSV-файл с правильными данными.
    """
    data_folder = TEST_FOLDER
    name_csv = 'test_data'
    heading = ['Name', 'Age', 'City']
    parsered_data = [
        ['John', '25', 'New York'],
        ['Jane', '30', 'Los Angeles'],
        ['Bob', '35', 'Chicago']
    ]

    write_csv(data_folder, name_csv, heading, parsered_data)

    assert os.path.exists(os.path.join(data_folder, f'{name_csv}.csv'))

    with open(os.path.join(data_folder, f'{name_csv}.csv'), 'r') as f:
        reader = csv.reader(f, delimiter = ",")
        rows = list(reader)
        assert rows == [heading] + parsered_data

    shutil.rmtree(data_folder)