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
                            ft.Card(content=ft.Image(
                                src=f"src\\assets\\uploads\\{self.book[0][1]}.png", height=464, width=290, border_radius=ft.BorderRadius(top_left=10, top_right=10, bottom_right=10, bottom_left=10), fit=ft.ImageFit.COVER),
                                elevation=10, shadow_color="black"
                            ),
                            ft.Column(
                                controls=[
                                    ft.Text(
                                        value=self.book[0][1], size=54, weight=ft.FontWeight.W_600, width=1000, font_family="Bookerly"),
                                    ft.Row(controls=[
                                        ft.Icon(name=ft.icons.CURRENCY_RUPEE_ROUNDED), ft.Text(
                                            value=self.book[0][8], size=18,  weight=ft.FontWeight.W_700),], spacing=0, alignment=ft.MainAxisAlignment.CENTER),
                                    ft.Container(content=ft.Markdown(
                                        value=self.book[0][2], selectable=True,
                                        extension_set="gitHubWeb",
                                    ), width=900),
                                    ft.Text(
                                        value=f"Genre: {self.book[0][7]}", size=16, width=800, color="#414141",  weight=ft.FontWeight.W_600),
                                    ft.Text(
                                        value=f"Publish Year: {self.book[0][3]}", size=16, width=800, color="#414141", weight=ft.FontWeight.W_600),
                                    ft.Text(
                                        value=f"Rating: {self.book[0][4]}", size=16, width=800, color="#414141",  weight=ft.FontWeight.W_600),
                                    ft.Text(
                                        value=f"Minimum Age: {self.book[0][5]}", size=16, width=800, color="#414141",  weight=ft.FontWeight.W_600),
                                    ft.Text(
                                        value=f"Currently only {self.book[0][6]} books left", size=20, width=800, color="#914141",  weight=ft.FontWeight.W_700),
                                    ft.FilledButton(
                                        content=ft.Text("Buy", size=18), on_click=lambda e, book_id=self.page.route.removeprefix("/book/buy/"): self.goToBill(e, book_id), height=40, width=100)
                                ],
                                scroll=ft.ScrollMode.ALWAYS, height=620
                            )
                        ], alignment=ft.MainAxisAlignment.START, vertical_alignment=ft.CrossAxisAlignment.START
                    ),
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
        self.page.go(f"/checkout/{book_id}")
