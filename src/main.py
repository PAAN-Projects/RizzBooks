import flet as ft

from components.views.signUpUser import signUpView


def main(page: ft.Page):
    page.theme_mode = "light"
    page.title = "DEEZ Books"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    page.fonts = {
        "Bookerly Bold": "https://cdn.jsdelivr.net/gh/PAAN-Projects/DeezBooks@master/src/assets/fonts/Bookerly-Bold.ttf",
        "Bookerly Italic": "https://cdn.jsdelivr.net/gh/PAAN-Projects/DeezBooks@master/src/assets/fonts/Bookerly Italic.ttf",
        "Bookerly": "https://cdn.jsdelivr.net/gh/PAAN-Projects/DeezBooks@master/src/assets/fonts/Bookerly.ttf"
    }

    def openSignUp(e):
        page.go("/signup")

    signup = signUpView()

    def routeChange(route):
        page.views.clear()
        page.views.append(
            ft.View(
                "/",
                [
                    ft.AppBar(
                        leading=ft.Icon(ft.icons.BOOK_ROUNDED),
                        leading_width=40,
                        title=ft.Text("DEEZ Books", font_family="Bookerly"),
                        center_title=False,
                        bgcolor=ft.colors.SURFACE_VARIANT,
                        actions=[
                            ft.TextField(
                                filled=True,
                                hint_text="Search here",
                                border_width=0,
                                border_radius=0
                            ),
                            ft.IconButton(ft.icons.SEARCH_ROUNDED),
                            ft.PopupMenuButton(
                                items=[
                                    ft.PopupMenuItem(text="Login"),
                                    ft.PopupMenuItem(
                                        text="Sign Up", on_click=openSignUp)
                                ],
                                icon=ft.icons.ACCOUNT_CIRCLE_ROUNDED
                            )
                        ],
                    ),
                    ft.Text(value="h")
                ],
            )
        )
        if page.route == "/signup":
            page.views.append(ft.View(
                "/signup",
                [
                    ft.AppBar(
                        title=ft.Text("Sign Up",
                                      font_family="Bookerly"),
                        bgcolor=ft.colors.SURFACE_VARIANT,
                    ),
                    signup]
            ))
        page.update()

    def view_pop(e):
        print("View pop:", e.view)
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = routeChange
    page.on_view_pop = view_pop
    page.padding = 10
    page.go(page.route)


ft.app(target=main, assets_dir="assets", view=ft.WEB_BROWSER)
