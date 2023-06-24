import flet as ft


class signUpView(ft.UserControl):
    def build(self):
        self.userNameInput = ft.TextField(label="Name")
        self.userAgeInput = ft.TextField(
            label="Age", keyboard_type=ft.KeyboardType.NUMBER, error_text="", on_change=self.check_int_age)
        self.userYearInput = ft.TextField(
            label="Year of Birth", keyboard_type=ft.KeyboardType.NUMBER, error_text="", on_change=self.check_int_year)
        self.userPasswordInput = ft.TextField(
            label="Password", password=True, can_reveal_password=True)
        self.submitButton = ft.ElevatedButton(
            text="Sign Up", icon=ft.icons.ARROW_FORWARD_ROUNDED)
        return ft.Container(content=ft.Column(controls=[
            self.userNameInput,
            self.userAgeInput,
            self.userYearInput,
            self.userPasswordInput,
            self.submitButton
        ], width=640), alignment=ft.alignment.center, padding=50)

    def check_int_age(self, e):
        try:
            self.userAgeInput.error_text = ""
            self.temp_int = int(e.control.value)
        except:
            self.userAgeInput.error_text = "Please enter a valid age"
        self.update()

    def check_int_year(self, e):
        try:
            self.userYearInput.error_text = ""
            self.temp_int = int(e.control.value)
        except:
            self.userYearInput.error_text = "Please enter a valid year"
        self.update()
