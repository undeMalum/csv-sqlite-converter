from pathlib import Path

import pytest

from src.sqlite_to_csv import (
    transfer_data_from_sqlite_to_csv,
    files_paths
)
from tests.constants_tests import (
    DATABASE,
    FACES_TABLE_CONTENT,
    FACES_TABLE_COLUMNS,
    FACESTYPE_TABLE_CONTENT,
    FACESTYPE_TABLE_COLUMNS
)


@pytest.mark.sqlitecsv
def test_fetch_tables():
    tables = transfer_data_from_sqlite_to_csv.fetch_tables(DATABASE)

    assert tables == ['facestype', 'faces']


@pytest.mark.sqlitecsv
@pytest.mark.parametrize("table, exp_content, exp_columns", [
    ("faces", FACES_TABLE_CONTENT, FACES_TABLE_COLUMNS),
    ("facestype", FACESTYPE_TABLE_CONTENT, FACESTYPE_TABLE_COLUMNS)
])
def test_fetch_data_from_sqlite(table, exp_content, exp_columns):
    content, columns = transfer_data_from_sqlite_to_csv.fetch_data_from_sqlite(DATABASE, table)

    assert content == exp_content
    assert columns == exp_columns


@pytest.mark.sqlitecsv
@pytest.mark.parametrize("path, exp_path", [
    (Path("test/test.txt"), files_paths.GENERATED_CSVS_DIR_PATH.joinpath("test")),
    (Path("test/text2.txt"), files_paths.GENERATED_CSVS_DIR_PATH.joinpath("text2"))
])
def test_create_csv_files_dir(path, exp_path):
    generated_path = transfer_data_from_sqlite_to_csv.create_csv_files_dir(path)

    assert generated_path == exp_path


@pytest.mark.sqlitecsv
def rm_dir():
    Path(files_paths.GENERATED_CSVS_DIR_PATH.joinpath("test")).rmdir()
    Path(files_paths.GENERATED_CSVS_DIR_PATH.joinpath("text2")).rmdir()
