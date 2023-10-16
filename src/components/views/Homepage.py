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
        self.BookRow = ft.Row(scroll="ALWAYS ON", alignment=ft.MainAxisAlignment.START, vertical_alignment=ft.CrossAxisAlignment.CENTER)
        self.BookColumn=[]

        for j in self.genre:
            self.BookColumn.append(ft.Text(value=j[0], weight=ft.FontWeight.W_500, text_align=ft.TextAlign.START, size=30))    
=======
        self.BookRow = ft.Row(scroll=ft.ScrollMode.ALWAYS, alignment=ft.MainAxisAlignment.CENTER,
                              vertical_alignment=ft.CrossAxisAlignment.CENTER)
        self.BookColumn = []

        for j in self.genre:
            self.BookColumn.append(ft.Text(
                value=j[0], weight=ft.FontWeight.W_500, text_align=ft.TextAlign.CENTER, size=30))
>>>>>>> 3f6905a5b20d558afcb264f075fb47a18ba453b1
            for i in self.books:
                if i[7] == j[0]:
                    self.BookRow.controls.append(
                        ft.Column(
                            controls=[
<<<<<<< HEAD
                                ft.Image(src=f"\\assets\\uploads\\{i[1]}.png", height=260, width=170, fit=ft.ImageFit.COVER, border_radius=ft.BorderRadius(10, 10, 10, 10)),
                                ft.Column(
                                    controls=[
                                        ft.Text(value=self.books[self.books.index(i)][1], size=15, weight=ft.FontWeight.W_500, text_align=ft.TextAlign.START),
                                        ft.OutlinedButton(text="Buy", style=ft.ButtonStyle(shape=ft.CountinuosRectangleBorder(radius=10)))
                                    ]
                                )
                                
=======
                                ft.Image(src=f"\\assets\\uploads\\{i[1]}.png", height=260, width=170,
                                         fit=ft.ImageFit.COVER, border_radius=ft.BorderRadius(10, 10, 10, 10)),
                                ft.Text(value=self.books[self.books.index(
                                    i)][1], size=18, weight=ft.FontWeight.W_500, text_align=ft.TextAlign.CENTER, width=170, max_lines=1),
                                ft.Text(value=" ", size=18, weight=ft.FontWeight.W_500,
                                        text_align=ft.TextAlign.CENTER, width=170, max_lines=1)
>>>>>>> 3f6905a5b20d558afcb264f075fb47a18ba453b1
                            ]
                        )
                    )

            self.BookColumn.append(self.BookRow)
<<<<<<< HEAD
            self.BookRow = ft.Row(scroll="ALWAYS ON", alignment=ft.MainAxisAlignment.START, vertical_alignment=ft.CrossAxisAlignment.CENTER)


        self.BookShelf=ft.Column(controls=self.BookColumn, alignment=ft.MainAxisAlignment.CENTER, horizontal_alignment=ft.CrossAxisAlignment.START)
        self.BookContainer=ft.Container(content=self.BookShelf, padding=25)
=======
            self.BookRow = ft.Row(scroll=ft.ScrollMode.ALWAYS, alignment=ft.MainAxisAlignment.CENTER,
                                  vertical_alignment=ft.CrossAxisAlignment.CENTER)

        self.BookShelf = ft.Column(controls=self.BookColumn, alignment=ft.MainAxisAlignment.CENTER,
                                   horizontal_alignment=ft.CrossAxisAlignment.CENTER)
        self.BookContainer = ft.Container(content=self.BookShelf, padding=25)
>>>>>>> 3f6905a5b20d558afcb264f075fb47a18ba453b1
        return self.BookContainer
