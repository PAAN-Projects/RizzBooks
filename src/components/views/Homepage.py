from email.mime import text
import math
from time import sleep
import flet as ft

from database import ORM

from random import randint
import datetime


class HomePage(ft.UserControl):

    def build(self):
        self.db = ORM()
        self.books = self.db.getAllBooks()
        self.genre = self.db.getGenre()
        self.BookRow = ft.Row(scroll=ft.ScrollMode.ALWAYS, alignment=ft.MainAxisAlignment.START,
                              vertical_alignment=ft.CrossAxisAlignment.START)
        self.BookColumn = []

        for j in self.genre:
            self.BookColumn.append(ft.Text(
                value=f"| {j[0]}", weight=ft.FontWeight.W_600, text_align=ft.TextAlign.END, size=28))
            for i in self.books:
                if i[7] == j[0]:
                    self.BookRow.controls.append(
                        ft.Column(
                            controls=[
                                ft.Image(src=f"\\assets\\uploads\\{i[1]}.png", height=260, width=170,
                                         fit=ft.ImageFit.COVER, border_radius=ft.BorderRadius(10, 10, 10, 10)),
                                ft.Text(value=self.books[self.books.index(i)][1], size=18, weight=ft.FontWeight.W_500, text_align=ft.TextAlign.START, width=170, max_lines=1),
                                ft.OutlinedButton(
                                    text="Buy", on_click=lambda _:self.page.go(f"/book/buy/")),
                                ft.Text(value=" ", size=18, weight=ft.FontWeight.W_500,
                                        text_align=ft.TextAlign.START, width=170, max_lines=1)
                            ]

                        )
                    )

            self.BookColumn.append(self.BookRow)
            self.BookRow = ft.Row(scroll=ft.ScrollMode.ALWAYS, alignment=ft.MainAxisAlignment.START,
                                  vertical_alignment=ft.CrossAxisAlignment.START)

        self.BookShelf = ft.Column(controls=self.BookColumn, alignment=ft.MainAxisAlignment.START,
                                   horizontal_alignment=ft.CrossAxisAlignment.START)
        self.BookContainer = ft.Container(
            content=self.BookShelf, padding=0, margin=ft.Margin(left=12, top=0, right=12, bottom=0), alignment=ft.alignment.center_left)
        return self.BookContainer