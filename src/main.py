from xmlrpc.client import Boolean
import flet as ft
import sqlite3 as sql

from components.views.Homepage import HomePage
from components.views.signUpUser import signUpView
from components.views.bookAdd import bookAdd
from components.views.login import login
from components.views.bookBuy import buyBook
from components.views.manageBooks import manageBooks
from components.views.editBooks import editBooks
from components.views.search import search
from components.views.Checkout import Checkout

from database import ORM


def main(page: ft.Page):
    page.theme_mode = "light"
    page.title = "DEEZ Books"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.scroll = "ALWAYS"
    page.pick_files_dialog = ft.FilePicker()
    page.overlay.append(page.pick_files_dialog)
    page.db = ORM()
    page.searchQuery = ""
    page.snack_bar = ft.SnackBar(content=ft.Text("Book Deleted"), open=False)
    # page.add(page.snack_bar)
    page.fonts = {
        "Bookerly Bold": "https://cdn.jsdelivr.net/gh/PAAN-Projects/DeezBooks@master/src/assets/fonts/Bookerly-Bold.ttf",
        "Bookerly Italic": "https://cdn.jsdelivr.net/gh/PAAN-Projects/DeezBooks@master/src/assets/fonts/Bookerly Italic.ttf",
        "Bookerly": "https://cdn.jsdelivr.net/gh/PAAN-Projects/DeezBooks@master/src/assets/fonts/Bookerly.ttf"
    }

    def openSignUp(e):
        page.go("/signup")

    def openLogin(e):
        page.go("/login")

    def openEdit(e):
        page.go("/books/edit")

    homePage = HomePage()
    signup = signUpView()
    addbook = bookAdd()
    loginpage = login()
    buybook = buyBook()
    managebooks = manageBooks()
    editbooks = editBooks()
    searchRoute = search()
    checkout=Checkout()

    def setSearchQuery(e):
        page.searchQuery = e.control.value
        page.update()

    def goToSearch(e):
        if (len(page.searchQuery) > 0):
            page.go("/home")
            page.go("/search")
            # page.searchQuery = searchBar.value
        # print(page.searchQuery)

    def routeChange(route):
        page.views.clear()
        page.views.append(
            ft.View(
                "/",
                [
                    ft.AppBar(
                        leading=ft.Icon(ft.icons.BOOK_ROUNDED),
                        leading_width=40,
                        title=ft.Text(
                            "DEEZ Books", font_family="Bookerly", size=32),
                        center_title=False,
                        bgcolor=ft.colors.SURFACE_VARIANT,
                        actions=[
                            ft.IconButton(
                                ft.icons.ADD, on_click=lambda _: page.go("/book/add")),
                            ft.TextField(
                                filled=True,
                                hint_text="Search here",
                                border_width=0,
                                border_radius=0,
                                on_change=setSearchQuery,
                            ),
                            ft.IconButton(ft.icons.SEARCH_ROUNDED,
                                          on_click=goToSearch),
                            ft.PopupMenuButton(
                                items=[
                                    ft.PopupMenuItem(
                                        text="Login", on_click=openLogin),
                                    ft.PopupMenuItem(
                                        text="Sign Up", on_click=openSignUp),
                                    ft.PopupMenuItem(
                                        text="Edit Books", on_click=openEdit)
                                ],
                                icon=ft.icons.ACCOUNT_CIRCLE_ROUNDED
                            )
                        ],
                    ),
                    homePage
                ],
                scroll="ALWAYS",
                padding=0
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
                    signup],
                scroll="ALWAYS"

            ))
        elif page.route == "/login":
            page.views.append(ft.View(
                "/login",
                [
                    ft.AppBar(
                        title=ft.Text("Login",
                                      font_family="Bookerly"),
                        bgcolor=ft.colors.SURFACE_VARIANT,
                    ),
                    loginpage],
                scroll="ALWAYS"

            ))
        elif page.route == "/book/add":
            page.views.append(ft.View(
                "/book/add",
                [
                    ft.AppBar(
                        title=ft.Text("Add Book",
                                      font_family="Bookerly"),
                        bgcolor=ft.colors.SURFACE_VARIANT,
                    ),
                    addbook],
                scroll="ALWAYS"
            ))
        elif "/book/buy/" in page.route:
            print(page.route)
            page.views.append(ft.View(
                page.route,
                [
                    ft.AppBar(
                        title=ft.Text("Book Details",
                                      font_family="Bookerly"),
                        bgcolor=ft.colors.SURFACE_VARIANT,
                    ),
                    buybook
                ]
            ))
        elif "/checkout" in page.route:
            page.views.append(ft.View(
                page.route,
                [
                    ft.AppBar(
                        title=ft.Text("Checkout",
                                      font_family="Bookerly"),
                        bgcolor=ft.colors.SURFACE_VARIANT,
                    ),
                    checkout
                ]
            ))
        elif "/book/edit" in page.route:
            page.views.append(ft.View(
                page.route,
                [
                    ft.AppBar(
                        title=ft.Text("Edit Book Stock",
                                      font_family="Bookerly"),
                        bgcolor=ft.colors.SURFACE_VARIANT,
                    ),
                    editbooks],
                scroll="ALWAYS"
            ))
        elif page.route == "/books/edit":
            page.views.append(ft.View(
                "/books/edit",
                [
                    ft.AppBar(
                        title=ft.Text("Edit Books",
                                      font_family="Bookerly"),
                        bgcolor=ft.colors.SURFACE_VARIANT,
                    ),
                    managebooks],
                padding=0,
                scroll="ALWAYS"
            ))
        elif page.route == "/search":
            page.views.append(ft.View(
                "/search",
                [
                    ft.AppBar(
                        leading=ft.Icon(ft.icons.BOOK_ROUNDED),
                        leading_width=40,
                        title=ft.Text(
                            "DEEZ Books", font_family="Bookerly", size=32),
                        center_title=False,
                        bgcolor=ft.colors.SURFACE_VARIANT,
                        actions=[
                            ft.IconButton(
                                ft.icons.HOME, on_click=lambda _:page.go("/home")),
                            ft.IconButton(
                                ft.icons.ADD, on_click=lambda _: page.go("/book/add")),
                            ft.TextField(
                                filled=True,
                                hint_text="Search here",
                                border_width=0,
                                border_radius=0,
                                on_change=setSearchQuery,
                                value=page.searchQuery
                            ),
                            ft.IconButton(ft.icons.SEARCH_ROUNDED,
                                          on_click=goToSearch),
                            ft.PopupMenuButton(
                                items=[
                                    ft.PopupMenuItem(
                                        text="Login", on_click=openLogin),
                                    ft.PopupMenuItem(
                                        text="Sign Up", on_click=openSignUp),
                                    ft.PopupMenuItem(
                                        text="Edit Books", on_click=openEdit)
                                ],
                                icon=ft.icons.ACCOUNT_CIRCLE_ROUNDED
                            )
                        ],
                    ),
                    searchRoute],
                padding=0,
                scroll="ALWAYS"
            ))
        page.padding = 0
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


ft.app(target=main, assets_dir="assets",
       upload_dir="assets/uploads", view=ft.WEB_BROWSER)
