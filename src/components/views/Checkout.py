from email.mime import text
import math
from time import sleep
import flet as ft

from database import ORM

from random import randint
import datetime


class Checkout(ft.UserControl):
    def did_mount(self):
        self.book_id = self.page.route.removeprefix("/checkout/")
        self.bookdetails = self.db.getBook(self.book_id)
        self.content.append(
            ft.Card(
                content=ft.Container(
                    content=ft.Column(
                        controls=[
                            ft.Image(src=f"src\\assets\\uploads\\{self.bookdetails[0][1]}.png", border_radius=ft.BorderRadius(
                                top_left=20, top_right=20, bottom_right=20, bottom_left=20), fit=ft.ImageFit.COVER, height=403, width=230),
                            ft.Text(
                                value=f"Book Name      :\t\t\t{self.bookdetails[0][1]}", font_family="Bookerly", size=30),
                            ft.Text(
                                value=f"Quantity           : 1", font_family="Bookerly", size=30),
                            ft.Text(
                                value=f"Book Price        :\t\t\tRs.  {self.bookdetails[0][8]} * (1)", font_family="Bookerly", size=30),
                            ft.Text(
                                value=f"Discount           : \t\t\t0% (Rs. 0)", font_family="Bookerly", size=30),
                            ft.Text(
                                value=f"GST                      : \t\t\tRs. {(self.bookdetails[0][8])*(0.18)}", font_family="Bookerly", size=30),
                            ft.Text(
                                value=f"Final Amount :\t\t\tRs. {(self.bookdetails[0][8])*(0.18)+(self.bookdetails[0][8])}", font_family="Bookerly", size=30),
                            ft.ElevatedButton(
                                text="Confirm Purchase", width=330, on_click=self.confirm),
                            ft.Row(
                                controls=[ft.Text("For further inquiry contact us at:"), ft.TextButton(text="here", url="https://www.youtube.com/video/dQw4w9WgXcQ?autoplay=1&disablekb=1")])
                        ]
                    ),
                    padding=10
                ),
                elevation=10,
                shadow_color="black",
                surface_tint_color="#4f4f4f",
                margin=20,
            )
        ),

        print(self.bookdetails)

        self.update()
        return super().did_mount()

    def build(self):
        self.db = ORM()
        self.books = self.db.getAllBooks()
        self.dialog = ft.AlertDialog(
            title=ft.Text("Thank you!!"), on_dismiss=lambda e: self.page.go("/"),
            content=ft.Image(src="\\assets\\images\\rickroll-roll.gif"),
        )

        self.content = [self.dialog]
        return self.content

    def confirm(self, e):
        self.dialog.open = True
        if (self.bookdetails[0][6] == 1):
            self.db.delBook(self.book_id)
        else:
            stock = self.bookdetails[0][6] - 1
            self.db.updateBook(self.book_id, stock)
        self.update()
