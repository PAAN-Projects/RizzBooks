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
        self.book = self.db.getBook(self.book_id)
        self.content.append(
            ft.Column(
                controls=[
                    ft.Row(
                        controls=[
                            ft.Image(src=f"src\\assets\\uploads\\{self.book[0][1]}.png", height=520, width=340),
                            ft.Column(
                                controls=[
                                    ft.Text(value="Book Description", size=24, weight=ft.FontWeight.BOLD),
                                    ft.Text(value=self.book[0][2])
                                ]
                            )
                        ], alignment=ft.MainAxisAlignment.START, vertical_alignment=ft.CrossAxisAlignment.START
                    ),
                    ft.FilledButton(
                        text="Buy", on_click=lambda e, book_id=self.page.route.removeprefix("/book/buy/"): self.goToBill(e, book_id))
                ]
            )
        )
        print(self.book)

        self.update()
        return super().did_mount()

    def build(self):
        self.db = ORM()
        self.books = self.db.getAllBooks()

        self.content = []
        return self.content
    
    def goToBill(self, e, book_id):
        self.page.go(f"/book/buy/checkout/{book_id}")
