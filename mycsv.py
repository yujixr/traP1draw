import csv
import os


def get_filepath(filename: str) -> str:
    folder_path = os.path.abspath("")
    return os.path.join(folder_path, filename)


def get_last_row(filename: str) -> list:
    with open(get_filepath(filename)) as f:
        reader = csv.reader(f)
        return [row for row in reader][-1]


def append_row(filename: str, new_row: list):
    with open(get_filepath(filename), "a") as f:
        writer = csv.writer(f)
        writer.writerow(new_row)
