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

thriller = requests.get(
    "https://openlibrary.org/subjects/thriller.json").json()["works"][:10]

user_name = "Prayag"

# print(len(scifi_books))
# db.delAllBooks()

for i in scifi:
    book = requests.get(f"https://openlibrary.org/{i['key']}.json").json()
    try:
        with open(os.path.join(os.getcwd(), f"src\\assets\\uploads\\{book['title']}.png"), "wb+") as img:
            img.write(requests.get(
                f"https://covers.openlibrary.org/b/id/{book['covers'][0]}-L.jpg").content)
    except:
        print("Skipping this book")
        continue
    try:
        db.addBook(user_name, randint(1_000_000, 9_999_999), book["title"], book["description"]["value"], datetime.datetime.fromisoformat(
            book["created"]["value"]).year, randint(1, 5), randint(4, 18), randint(6, 18), randint(300, 850), "Sci-fi")
    except:
        try:
            db.addBook(user_name, randint(1_000_000, 9_999_999), book["title"], book["description"], datetime.datetime.fromisoformat(
                book["created"]["value"]).year, randint(1, 5), randint(4, 18), randint(6, 18), randint(300, 850), "Sci-fi")
        except:
            print("Skipping this book")

for i in fiction:
    book = requests.get(f"https://openlibrary.org/{i['key']}.json").json()
    try:
        with open(os.path.join(os.getcwd(), f"src\\assets\\uploads\\{book['title']}.png"), "wb+") as img:
            img.write(requests.get(
                f"https://covers.openlibrary.org/b/id/{book['covers'][0]}-L.jpg").content)
    except:
        print("Skipping this book")
        continue
    try:
        db.addBook(user_name, randint(1_000_000, 9_999_999), book["title"], book["description"]["value"], datetime.datetime.fromisoformat(
            book["created"]["value"]).year, randint(1, 5), randint(4, 18), randint(6, 18), randint(140, 850), "Fiction")
    except:
        try:
            db.addBook(user_name, randint(1_000_000, 9_999_999), book["title"], book["description"], datetime.datetime.fromisoformat(
                book["created"]["value"]).year, randint(1, 5), randint(4, 18), randint(6, 18), randint(140, 850), "Fiction")
        except:
            print("Skipping this book")

for i in fantasy:
    book = requests.get(f"https://openlibrary.org/{i['key']}.json").json()
    try:
        with open(os.path.join(os.getcwd(), f"src\\assets\\uploads\\{book['title']}.png"), "wb+") as img:
            img.write(requests.get(
                f"https://covers.openlibrary.org/b/id/{book['covers'][0]}-L.jpg").content)
    except:
        print("Skipping this book")
        continue
    try:
        db.addBook(user_name, randint(1_000_000, 9_999_999), book["title"], book["description"]["value"], datetime.datetime.fromisoformat(
            book["created"]["value"]).year, randint(1, 5), randint(4, 18), randint(6, 18), randint(220, 850), "Fantasy")
    except:
        try:
            db.addBook(user_name, randint(1_000_000, 9_999_999), book["title"], book["description"], datetime.datetime.fromisoformat(
                book["created"]["value"]).year, randint(1, 5), randint(4, 18), randint(6, 18), randint(220, 850), "Fantasy")
        except:
            print("Skipping this book")


for i in horror:
    book = requests.get(f"https://openlibrary.org/{i['key']}.json").json()
    try:
        with open(os.path.join(os.getcwd(), f"src\\assets\\uploads\\{book['title']}.png"), "wb+") as img:
            img.write(requests.get(
                f"https://covers.openlibrary.org/b/id/{book['covers'][0]}-L.jpg").content)
    except:
        print("Skipping this book")
        continue
    try:
        db.addBook(user_name, randint(1_000_000, 9_999_999), book["title"], book["description"]["value"], datetime.datetime.fromisoformat(
            book["created"]["value"]).year, randint(1, 5), randint(4, 18), randint(6, 18), randint(100, 850), "Horror")
    except:
        try:
            db.addBook(user_name, randint(1_000_000, 9_999_999), book["title"], book["description"], datetime.datetime.fromisoformat(
                book["created"]["value"]).year, randint(1, 5), randint(4, 18), randint(6, 18), randint(100, 850), "Horror")
        except:
            print("Skipping this book")

for i in thriller:
    book = requests.get(f"https://openlibrary.org/{i['key']}.json").json()
    try:
        with open(os.path.join(os.getcwd(), f"src\\assets\\uploads\\{book['title']}.png"), "wb+") as img:
            img.write(requests.get(
                f"https://covers.openlibrary.org/b/id/{book['covers'][0]}-L.jpg").content)
    except:
        print("Skipping this book")
        continue
    try:
        db.addBook(user_name, randint(1_000_000, 9_999_999), book["title"], book["description"]["value"], datetime.datetime.fromisoformat(
            book["created"]["value"]).year, randint(1, 5), randint(4, 18), randint(6, 18), randint(240, 850), "Thriller")
    except:
        try:
            db.addBook(user_name, randint(1_000_000, 9_999_999), book["title"], book["description"], datetime.datetime.fromisoformat(
                book["created"]["value"]).year, randint(1, 5), randint(4, 18), randint(6, 18), randint(240, 850), "Thriller")
        except:
            print("Skipping this book")
