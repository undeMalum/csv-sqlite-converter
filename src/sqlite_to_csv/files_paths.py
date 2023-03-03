from pathlib import Path

PROJECT_PATH = Path(__file__).absolute().parent.parent.parent  # abs path of the project
GENERATED_CSVS_DIR_PATH = PROJECT_PATH.joinpath("generated_csv_files")  # path to the destination of created csv files

if __name__ == "__main__":
    print(PROJECT_PATH, GENERATED_CSVS_DIR_PATH)
