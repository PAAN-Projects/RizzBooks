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

        self.BookRow = ft.Row(scroll="ALWAYS ON", alignment=ft.MainAxisAlignment.CENTER,
                              vertical_alignment=ft.CrossAxisAlignment.CENTER)
        self.BookGenre = ft.Text(
            value="Genre", size=30, weight=ft.FontWeight.BOLD, text_align=ft.TextAlign.CENTER)

        for i in self.books:
            self.BookRow.controls.append(
                ft.Column(
                    controls=[
                        ft.Image(
                            src=f"/assets/uploads/{i[1]}.png", height=260, width=170, fit=ft.ImageFit.COVER, border_radius=ft.BorderRadius(10, 10, 10, 10)),
                        ft.Text(
                            value=self.books[self.books.index(i)][1], size=18, weight=ft.FontWeight.W_500, text_align=ft.TextAlign.CENTER)
                    ]
                )
            )
        return self.BookRow

# ye Alag file me homepage ka bana ke choda hai, main views me dalna nahi aa raha error aa raha hai
