# This Py Script is used to add test book dataset to database
import datetime
import os
from random import randint
import requests

from database import ORM

db = ORM()

scifi = requests.get(
    "https://openlibrary.org/subjects/scifi.json").json()["works"][:12]

fiction = requests.get(
    "https://openlibrary.org/subjects/fiction.json").json()["works"][:8]

fantasy = requests.get(
    "https://openlibrary.org/subjects/fantasy.json").json()["works"][:16]

horror = requests.get(
    "https://openlibrary.org/subjects/horror.json").json()["works"][:10]

user_id = 5028606
user_name = "Prayag"

# print(len(scifi_books))
# db.delAllBooks()

for i in scifi:
    book = requests.get(f"https://openlibrary.org/{i['key']}.json").json()
    try:
        db.addBook(user_name, randint(1_000_000, 9_999_999), book["title"], book["description"]["value"], datetime.datetime.fromisoformat(
            book["created"]["value"]).year, randint(1, 5), randint(4, 18), randint(6, 18), "Sci-fi")
    except:
        db.addBook(user_name, randint(1_000_000, 9_999_999), book["title"], book["description"], datetime.datetime.fromisoformat(
            book["created"]["value"]).year, randint(1, 5), randint(4, 18), randint(6, 18), "Sci-fi")

    with open(os.path.join(os.getcwd(), f"src\\assets\\uploads\\{book['title']}.png"), "wb+") as img:
        img.write(requests.get(
            f"https://covers.openlibrary.org/b/id/{book['covers'][0]}-L.jpg").content)

for i in fiction:
    book = requests.get(f"https://openlibrary.org/{i['key']}.json").json()
    try:
        db.addBook(user_name, randint(1_000_000, 9_999_999), book["title"], book["description"]["value"], datetime.datetime.fromisoformat(
            book["created"]["value"]).year, randint(1, 5), randint(4, 18), randint(6, 18), "Sci-fi")
    except:
        db.addBook(user_name, randint(1_000_000, 9_999_999), book["title"], book["description"], datetime.datetime.fromisoformat(
            book["created"]["value"]).year, randint(1, 5), randint(4, 18), randint(6, 18), "Sci-fi")

    with open(os.path.join(os.getcwd(), f"src\\assets\\uploads\\{book['title']}.png"), "wb+") as img:
        img.write(requests.get(
            f"https://covers.openlibrary.org/b/id/{book['covers'][0]}-L.jpg").content)

for i in fantasy:
    book = requests.get(f"https://openlibrary.org/{i['key']}.json").json()
    try:
        db.addBook(user_name, randint(1_000_000, 9_999_999), book["title"], book["description"]["value"], datetime.datetime.fromisoformat(
            book["created"]["value"]).year, randint(1, 5), randint(4, 18), randint(6, 18), "Sci-fi")
    except:
        db.addBook(user_name, randint(1_000_000, 9_999_999), book["title"], book["description"], datetime.datetime.fromisoformat(
            book["created"]["value"]).year, randint(1, 5), randint(4, 18), randint(6, 18), "Sci-fi")

    with open(os.path.join(os.getcwd(), f"src\\assets\\uploads\\{book['title']}.png"), "wb+") as img:
        img.write(requests.get(
            f"https://covers.openlibrary.org/b/id/{book['covers'][0]}-L.jpg").content)

for i in horror:
    book = requests.get(f"https://openlibrary.org/{i['key']}.json").json()
    try:
        db.addBook(user_name, randint(1_000_000, 9_999_999), book["title"], book["description"]["value"], datetime.datetime.fromisoformat(
            book["created"]["value"]).year, randint(1, 5), randint(4, 18), randint(6, 18), "Sci-fi")
    except:
        db.addBook(user_name, randint(1_000_000, 9_999_999), book["title"], book["description"], datetime.datetime.fromisoformat(
            book["created"]["value"]).year, randint(1, 5), randint(4, 18), randint(6, 18), "Sci-fi")

    with open(os.path.join(os.getcwd(), f"src\\assets\\uploads\\{book['title']}.png"), "wb+") as img:
        img.write(requests.get(
            f"https://covers.openlibrary.org/b/id/{book['covers'][0]}-L.jpg").content)
