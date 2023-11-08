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
                        ft.TextButton(
                            content=ft.Column(controls=[
                                ft.Image(src=f"\\assets\\uploads\\{i[1]}.png", height=260,
                                         fit=ft.ImageFit.COVER, border_radius=ft.BorderRadius(10, 10, 10, 10)),
                                ft.Row(controls=[
                                    ft.Icon(name=ft.icons.CURRENCY_RUPEE_ROUNDED), ft.Text(
                                        value=i[8], size=18,  weight=ft.FontWeight.W_700),], spacing=0, alignment=ft.MainAxisAlignment.START),
                                ft.Text(value=i[1], size=18, weight=ft.FontWeight.W_500,
                                        text_align=ft.TextAlign.START),
                            ], alignment=ft.MainAxisAlignment.CENTER), style=ft.ButtonStyle(bgcolor="#f0f0f0", color="black", shape={
                                ft.MaterialState.DEFAULT: ft.RoundedRectangleBorder(radius=10),
                            }, padding=15), on_click=lambda e, book_id=i[0]: self.goToBook(e, book_id), width=190)
                    )

            self.BookColumn.append(self.BookRow)
            self.BookRow = ft.Row(scroll=ft.ScrollMode.ALWAYS, alignment=ft.MainAxisAlignment.START,
                                  vertical_alignment=ft.CrossAxisAlignment.START)

        self.BookShelf = ft.Column(controls=self.BookColumn, alignment=ft.MainAxisAlignment.START,
                                   horizontal_alignment=ft.CrossAxisAlignment.START)
        self.BookContainer = ft.Container(
            content=self.BookShelf, padding=0, margin=ft.Margin(left=12, top=0, right=12, bottom=0), alignment=ft.alignment.center_left)
        return self.BookContainer

    def goToBook(self, e, book_id):
        self.page.go(f"/book/buy/{book_id}")
