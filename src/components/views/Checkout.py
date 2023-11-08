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
                            ft.Image(src=f"src\\assets\\uploads\\{self.bookdetails[0][1]}.png", border_radius=ft.BorderRadius(top_left=10, top_right=10, bottom_right=10, bottom_left=10), fit=ft.ImageFit.COVER),
                            ft.Text(value=f"Book Name:\t\t\t{self.bookdetails[0][1]}", font_family="Bookerly", size=30),
                            ft.Text(value=f"Book Price:\t\t\t{self.bookdetails[0][8]}", font_family="Bookerly",size=30),
                            ft.Text(value=f"GST:\t\t\t{(self.bookdetails[0][8])*(0.18)}", font_family="Bookerly",size=30),
                            ft.Text(value=f"Final Amount:\t\t\t{(self.bookdetails[0][8])*(0.18)+(self.bookdetails[0][8])}", font_family="Bookerly",size=30),
                            ft.ElevatedButton(text="Confirm Purchase", width=330)
                        ]
                    )
                ),
                elevation=10,
                shadow_color="black"
            )
        )
                    
        print(self.bookdetails)
        
        self.update()
        return super().did_mount()
    
    def build(self):
        self.db=ORM()
        self.books=self.db.getAllBooks()

        self.content=[]
        return self.content