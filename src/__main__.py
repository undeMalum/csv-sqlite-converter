from pathlib import Path

from src.sqlite_to_csv import transfer_data_from_sqlite_to_csv
from src.csv_to_sqlite import input_checks
from src.validation import db_input_validation


def db_mode(database_path: Path) -> None:
    for table in transfer_data_from_sqlite_to_csv.fetch_tables(database_path):
        transfer_data_from_sqlite_to_csv.import_sqlite_to_csv(database_path, table)
        print(f"Data from {table} table are now stored in {table}.csv.")


def csv_mode(database_path: Path) -> None:
    csv_dir_path = Path(input("Copy path to directory with csv files: ").replace('"', ''))
    if not csv_dir_path.is_dir():
        return print("Provided path is incorrect.")

    for csv_file in csv_dir_path.iterdir():
        csv_management_message = input_checks.check_input_and_insert_into_db(
            database_path,
            csv_file
        )

        print(csv_management_message)


def main() -> None:
    mode = ""

    while mode != "stop":
        mode = input("""
Choose one of the following:
\t1. "db" to transfer data from a database to a csv file
\t2. "csv" to transfer data from a csv file to a database
\t3. "stop" to stop
> """).lower()

        if mode == "stop":
            break

        # get db_path
        database_path = Path(input("Copy path to database: ").replace('"', ''))

        if not database_path.is_file() or not db_input_validation.is_extension_correct(database_path, (".db",)):
            print("Provided path is incorrect.")
            continue

        if mode == "db":
            db_mode(database_path)
        elif mode == "csv":
            csv_mode(database_path)
        else:
            print("Chosen mode is incorrect.")


if __name__ == "__main__":
    main()
