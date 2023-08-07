import math
from time import sleep
import flet as ft
from utils.password import checkStrength
from database import ORM

from random import randint
import datetime


class signUpView(ft.UserControl):
    def build(self):
        self.userNameInput = ft.TextField(label="Name")
        self.userAgeInput = ft.TextField(
            label="Age", keyboard_type=ft.KeyboardType.NUMBER, error_text="", on_change=self.check_int_age)
        self.userPasswordInput = ft.TextField(
            label="Password", password=True, can_reveal_password=True, on_change=self.check_pass_strength)
        self.passowordStrengthBar = ft.ProgressBar(value=0)
        self.passowordStrengthText = ft.Text("")
        self.submitButton = ft.FilledTonalButton(
            text="Sign Up", icon=ft.icons.ARROW_FORWARD_ROUNDED, on_click=self.add_user)
        self.warningText = "Please enter a valid password"
        self.warningSnackBar = ft.SnackBar(ft.Text(self.warningText))
        return ft.Container(content=ft.Column(controls=[
            self.userNameInput,
            self.userAgeInput,
            self.userPasswordInput,
            self.passowordStrengthBar,
            self.passowordStrengthText,
            self.submitButton,
            self.warningSnackBar
        ], width=640), alignment=ft.alignment.center, padding=50)

    def check_int_age(self, e):
        try:
            self.userAgeInput.error_text = ""
            temp_int = int(e.control.value)
        except:
            self.userAgeInput.error_text = "Please enter a valid age"
        self.update()

    def check_int_year(self, e):
        try:
            self.userYearInput.error_text = ""
            temp_int = int(e.control.value)
        except:
            self.userYearInput.error_text = "Please enter a valid year"
        self.update()

    def check_pass_strength(self, e):
        try:
            st = checkStrength(e.control.value)
            if len(st["suggestion"]) > 0:
                self.passowordStrengthText.value = f"Tip: {st['suggestion'][0]}"
            else:
                self.passowordStrengthText.value = ''
            if st["strength"] >= 3:
                self.passowordStrengthBar.color = ft.colors.GREEN
            elif st['strength'] == 2:
                self.passowordStrengthBar.color = ft.colors.AMBER
            elif st['strength'] <= 1:
                self.passowordStrengthBar.color = ft.colors.RED
            self.passowordStrengthBar.value = st["strength"] / 4
            self.update()
        except:
            self.passowordStrengthBar.value = 0
            self.update()

    def add_user(self, e):
        try:
            user_id = randint(1_000_000, 9_999_999)
            currentDate = datetime.date.today()
            if self.passowordStrengthBar.value * 4 >= 2:
                self.page.db.addUser(user_id=user_id, user_name=self.userNameInput.value, user_year=currentDate.year,
                                     user_age=self.userAgeInput.value, user_pass=self.userPasswordInput.value)

                self.warningSnackBar.content = ft.Text("User Added!")
                self.warningSnackBar.open = True
                self.update()
            else:
                self.warningSnackBar.content = ft.Text(
                    "Please enter a valid password")
                self.warningSnackBar.open = True
                self.update()
        except:
            pass
