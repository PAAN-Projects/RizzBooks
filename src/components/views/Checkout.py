from email.mime import text
import math
from time import sleep
import flet as ft

from database import ORM

from random import randint
import datetime

class Checkout(ft.UserControl):
    def did_mount(self):
        self.book_id = self.page.route.removeprefix("/book/buy/checkout/")
        self.bookdetails = self.db.getBook(self.book_id)
        self.content.append(
                content=[
                    ft.Column(
                        controls=[
                            ft.Text(value=f"Book Name:\t\t\t{self.bookdetails[0][2]}"),
                            ft.Text(value=f"Book Price:\t\t\t{self.bookdetails[0][8]}"),
                            ft.Text(value=f"GST:\t\t\t{(self.bookdetails[0][8])*(0.18)}"),
                            ft.Text(value=f"Final Amount:\t\t\t{(self.bookdetails[0][8])*(0.18)+(self.bookdetails[0][8])}")
                        ]
                    )
                ]
            )
        print(self.book_id)
        self.update()
        return super().did_mount()
    
    def build(self):
        self.db=ORM()
        self.books=self.db.getAllBooks(self.book_id)

        self.content=[]
        return self.content