from email.mime import text
import math
from time import sleep
import flet as ft

from database import ORM

from random import randint
import datetime


class search(ft.UserControl):
    def did_mount(self):
        self.book_id = self.page.route.removeprefix("/book/edit/")
        self.books = self.db.searchBook(self.page.searchQuery)

        self.layout = ft.Row(
            controls=[],
            scroll=ft.ScrollMode.ALWAYS, alignment=ft.MainAxisAlignment.START,
            vertical_alignment=ft.CrossAxisAlignment.START)

        for i in self.books:
            self.layout.controls.append(
                ft.Column(
                    controls=[
                        ft.Image(src=f"\\assets\\uploads\\{i[1]}.png", height=260, width=170,
                                 fit=ft.ImageFit.COVER, border_radius=ft.BorderRadius(10, 10, 10, 10)),
                        ft.Text(value=i[1], size=18, weight=ft.FontWeight.W_500,
                                text_align=ft.TextAlign.START, width=170, max_lines=1),
                        ft.OutlinedButton(
                            text="Buy", on_click=lambda e, book_id=i[0]:self.goToBook(e, book_id)),
                        ft.Text(value=" ", size=18, weight=ft.FontWeight.W_500,
                                text_align=ft.TextAlign.START, width=170, max_lines=1)
                    ]

                )
            )

        if len(self.books) == 0:
            self.layout.controls.append(ft.Text(value="No result"))

        self.content.content = self.layout
        self.update()
        return super().did_mount()

    def build(self):
        self.db = ORM()

        self.content = ft.Container(padding=ft.Padding(
            left=10, top=10, right=10, bottom=10))
        return self.content

    def goToBook(self, e, book_id):
        self.page.go(f"/book/buy/{book_id}")
