import csv
import os


def get_last_row(filename: str) -> list:
    folder_path = os.getenv("FOLDER_PATH")
    with open(f"{folder_path}//{filename}") as f:
        reader = csv.reader(f)
        return [row for row in reader][-1]


def append_row(filename: str, new_row: list):
    folder_path = os.getenv("FOLDER_PATH")
    with open(f"{folder_path}//{filename}", "a") as f:
        writer = csv.writer(f)
        writer.writerow(new_row)
