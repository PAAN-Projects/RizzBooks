import math
from time import sleep
import flet as ft
from utils.password import checkStrength
from database import ORM

from random import randint
import datetime


class bookAdd(ft.UserControl):
    def build(self):
        self.loggedIn = False
        self.db = ORM()
        self.header = ft.Text(
            "Login", weight=ft.FontWeight.W_200, size=50)
        self.userNameInput = ft.TextField(label="User Name")
        self.userPassInput = ft.TextField(label="User Password")
        self.loginBtn = ft.FilledTonalButton(
            "Login", icon=ft.icons.ARROW_FORWARD_ROUNDED, on_click=self.login)

        return ft.Container(content=ft.Column(controls=[
            self.header,
            self.userNameInput,
            self.userPassInput,
            self.loginBtn,




        ], width=640), alignment=ft.alignment.center, padding=50)

    def login(self, e):
        a = self.db.getUser(user_name=self.userNameInput.value)
        print(a)
        self.update()

    def hideLogin(self):
        self.header.visible = False
        self.userNameInput.visible = False
        self.userPassInput.visible = False
        self.loginBtn.visible = False
