from email.mime import text
import math
from time import sleep
import flet as ft

from database import ORM

from random import randint
import datetime

class buyBook(ft.UserControl):
    def build(self):
        self.db=ORM()
        self.books=self.db.getAllBooks()

        for i in self.books:
            if i[1] == self.BookName:
                self.BookDesc=i[3]
                break

        self.BookDetails = ft.Column(
            controls=[
                ft.Image(src=f"\\assets\\uploads\\{self.BookName}.png"),
                ft.Text(value=self.BookName, size=24, weight=ft.FontWeight.W_600),
                ft.Text(value=self.BookDesc)
            ]
        )
        return self.BookDetails