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
<<<<<<< HEAD

        self.BookRow = ft.Row(scroll=ft.ScrollMode.ALWAYS, alignment=ft.MainAxisAlignment.CENTER,
                              vertical_alignment=ft.CrossAxisAlignment.CENTER)
=======
        self.BookRow = ft.Row(scroll=ft.ScrollMode.ALWAYS, alignment=ft.MainAxisAlignment.START,
                              vertical_alignment=ft.CrossAxisAlignment.START)
>>>>>>> 4506c6fb49d1dee4f863f8ee73f4ac650d337695
        self.BookColumn = []

        for j in self.genre:
            self.BookColumn.append(ft.Text(
<<<<<<< HEAD
                value=j[0], weight=ft.FontWeight.W_500, text_align=ft.TextAlign.CENTER, size=30))
=======
                value=f"| {j[0]}", weight=ft.FontWeight.W_600, text_align=ft.TextAlign.END, size=28))
>>>>>>> 4506c6fb49d1dee4f863f8ee73f4ac650d337695
            for i in self.books:
                if i[7] == j[0]:
                    self.BookRow.controls.append(
                        ft.Column(
                            controls=[
                                ft.Image(src=f"\\assets\\uploads\\{i[1]}.png", height=260, width=170,
                                         fit=ft.ImageFit.COVER, border_radius=ft.BorderRadius(10, 10, 10, 10)),
<<<<<<< HEAD
                                ft.Column(
                                    controls=[
                                        ft.Text(value=i[1], size=18, weight=ft.FontWeight.W_500,
                                                text_align=ft.TextAlign.START, width=170, max_lines=1),
                                        ft.OutlinedButton(text="Buy", on_click=lambda nm=i[1]: self.page.go(f"/book/buy/{nm}"), data=i[1]),
                                        ft.Text(value=" ", size=18, weight=ft.FontWeight.W_500,
                                                text_align=ft.TextAlign.CENTER, width=170, max_lines=1)
                                    ]
                                ),
=======
                                ft.Text(value=self.books[self.books.index(
                                    i)][1], size=18, weight=ft.FontWeight.W_500, text_align=ft.TextAlign.START, width=170, max_lines=1),
                                ft.OutlinedButton(
                                    text="Buy", on_click=lambda _:self.buyBook()),
                                ft.Text(value=" ", size=18, weight=ft.FontWeight.W_500,
                                        text_align=ft.TextAlign.START, width=170, max_lines=1)
>>>>>>> 4506c6fb49d1dee4f863f8ee73f4ac650d337695
                            ]

                        )
                    )

            self.BookColumn.append(self.BookRow)
<<<<<<< HEAD
            self.BookRow = ft.Row(scroll=ft.ScrollMode.ALWAYS, alignment=ft.MainAxisAlignment.CENTER,
                                  vertical_alignment=ft.CrossAxisAlignment.CENTER)

        self.BookShelf = ft.Column(controls=self.BookColumn, alignment=ft.MainAxisAlignment.CENTER,
                                   horizontal_alignment=ft.CrossAxisAlignment.CENTER)
        self.BookContainer = ft.Container(content=self.BookShelf, padding=25)
        return self.BookContainer
=======
            self.BookRow = ft.Row(scroll=ft.ScrollMode.ALWAYS, alignment=ft.MainAxisAlignment.START,
                                  vertical_alignment=ft.CrossAxisAlignment.START)

        self.BookShelf = ft.Column(controls=self.BookColumn, alignment=ft.MainAxisAlignment.START,
                                   horizontal_alignment=ft.CrossAxisAlignment.START)
        self.BookContainer = ft.Container(
            content=self.BookShelf, padding=0, margin=ft.Margin(left=12, top=0, right=12, bottom=0), alignment=ft.alignment.center_left)
        return self.BookContainer

    def buyBook(self):
        self.page.go("/book/")
>>>>>>> 4506c6fb49d1dee4f863f8ee73f4ac650d337695
