import math
from time import sleep
import flet as ft
import sqlite3 as sql

from random import randint
import datetime

def main(page: ft.Page):
    page.theme_mode = "light"
    page.title = "DEEZ Books"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.scroll = "ALWAYS"

    sqlConnection=sql.connect("database.db")
    sqlCursor=sql.Cursor(sqlConnection)
    sqlCursor.execute("SELECT BookName FROM Books")
    BookName=sqlCursor.fetchall()
    sqlCursor.close()
    sqlConnection.close()

    BookRow=ft.Row(scroll="ALWAYS ON", alignment=ft.MainAxisAlignment.CENTER, vertical_alignment=ft.CrossAxisAlignment.CENTER)
    BookGenre=ft.Text(value="Genre", size=30, weight=ft.FontWeight.BOLD, text_align=ft.TextAlign.CENTER)

    for i in BookName:
        BookRow.controls.append(
            ft.Column(
                controls=[
                    ft.Image(src=f"C:\\Users\\Neev\\DeezBooks\\src\\uploads\\{i[0]}.png",height=200, width=131),
                    ft.Text(value=BookName[BookName.index(i)][0], size=15)
                ]
            )
        )
    page.add(BookGenre, BookRow)
ft.app(target=main)

# ye Alag file me homepage ka bana ke choda hai, main views me dalna nahi aa raha error aa raha hai

    

