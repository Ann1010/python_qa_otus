import csv
import json
from typing import List

CSV_FILE = "./files/books.csv"
JSON_FILE = "./files/users.json"
RESULT_FILE = "./files/result.json"


def read_csv(csv_file_name):
    with open(csv_file_name, 'r', newline='') as csv_file:
        rows = csv.DictReader(csv_file)
        result = [row for row in rows]
    return result


def read_json(json_file_name):
    with open(json_file_name, 'r') as json_file:
        result = json.load(json_file)
    return result


def create_users_list(users_list: List):
    new_users_list = [
        {"name": user["name"],
         "gender": user["gender"],
         "address": user["address"],
         "age": user["age"],
         "books": []}
        for user in users_list]
    return new_users_list


def create_books_list(books_list: List):
    new_books_list = [
        {"title": book["Title"],
         "author": book["Author"],
         "pages": int(book["Pages"]),
         "genre": book["Genre"]}
        for book in books_list]
    return new_books_list


def add_books_for_user(users_list, book_list):
    for index, book in enumerate(book_list):
        user = users_list[index % len(users_list)]
        user['books'].append(book)
    return users_list


def write_json(result_file, result_list):
    with open(result_file, "w") as json_file:
        json_res = json.dumps(result_list, indent=4)
        json_file.write(json_res)


if __name__ == "__main__":
    users = read_json(JSON_FILE)
    books = read_csv(CSV_FILE)

    filter_users = create_users_list(users)
    fileter_books = create_books_list(books)

    result_list = add_books_for_user(filter_users, fileter_books)

    write_json(RESULT_FILE, result_list)
