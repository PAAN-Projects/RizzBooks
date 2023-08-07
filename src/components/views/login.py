import math
from time import sleep
import flet as ft
from utils.password import checkStrength
from database import ORM

from random import randint
import datetime


class login(ft.UserControl):
    def build(self):
        self.loggedIn = False
        self.header = ft.Text(
            "Login", weight=ft.FontWeight.W_200, size=50)
        self.userNameInput = ft.TextField(label="User Name")
        self.userPassInput = ft.TextField(
            label="User Password", password=True, can_reveal_password=True)
        self.warningSnackBar = ft.SnackBar(
            ft.Text("Wrong username or password"))
        self.loginBtn = ft.FilledTonalButton(
            "Login", icon=ft.icons.ARROW_FORWARD_ROUNDED, on_click=self.login)

        return ft.Container(content=ft.Column(controls=[
            self.header,
            self.userNameInput,
            self.userPassInput,
            self.loginBtn,
            self.warningSnackBar

        ], width=640), alignment=ft.alignment.center, padding=50)

    def login(self, e):
        self.warningSnackBar.open = False
        self.warningSnackBar.content = ft.Text("Wrong username or password")
        self.update()
        try:
            req = self.page.db.getUser(user_name=self.userNameInput.value, )
            if req[4] == self.userPassInput.value:
                self.page.session.set("current-user", req[1])
                self.warningSnackBar.content = ft.Text(
                    f"Logged in as {req[1]}")
                self.warningSnackBar.open = True
            else:
                self.warningSnackBar.open = True
        except:
            self.warningSnackBar.open = True
            pass
        self.update()

    def hideLogin(self):
        self.header.visible = False
        self.userNameInput.visible = False
        self.userPassInput.visible = False
        self.loginBtn.visible = False
