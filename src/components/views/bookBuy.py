from email.mime import text
import math
from time import sleep
import flet as ft

from database import ORM

from random import randint
import datetime


class buyBook(ft.UserControl):
    def did_mount(self):
        self.book_id = self.page.route.removeprefix("/book/buy/")
        self.content.append(ft.Text(value=self.book_id))
        self.book = self.db.getBook(self.book_id)
        print(self.book)

        self.update()
        return super().did_mount()

    def build(self):
        self.db = ORM()
        self.books = self.db.getAllBooks()

        self.content = []
        return self.content
