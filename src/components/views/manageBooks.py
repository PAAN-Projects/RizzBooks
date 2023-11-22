import flet as ft

from database import ORM


class manageBooks(ft.UserControl):
    def build(self):
        self.db = ORM()
        self.books = self.db.getAllBooks()
        self.genre = self.db.getGenre()
        self.BookRow = ft.Row(scroll=ft.ScrollMode.ALWAYS, alignment=ft.MainAxisAlignment.START,
                              vertical_alignment=ft.CrossAxisAlignment.START)
        self.BookColumn = []

        for j in self.genre:
            self.BookColumn.append(ft.Text(
                value=f"| {j[0]}", weight=ft.FontWeight.W_600, text_align=ft.TextAlign.END, size=28))
            for i in self.books:
                if i[7] == j[0]:
                    self.BookRow.controls.append(
                        ft.Column(
                            controls=[
                                ft.Image(src=f"\\assets\\uploads\\{i[1]}.png", height=260, width=170,
                                         fit=ft.ImageFit.COVER, border_radius=ft.BorderRadius(10, 10, 10, 10), ),
                                ft.Text(value=self.books[self.books.index(
                                    i)][1], size=18, weight=ft.FontWeight.W_500, text_align=ft.TextAlign.START, width=170),
                                ft.Row(controls=[
                                    ft.IconButton(icon=ft.icons.DELETE, style=ft.ButtonStyle(color=ft.colors.RED_400), on_click=lambda e, book_id=i[0]: self.deleteBook(e, book_id)), ft.IconButton(icon=ft.icons.EDIT, style=ft.ButtonStyle(color=ft.colors.AMBER_400), on_click=lambda e, book_id=i[0]: self.goToBook(e, book_id))]),
                                ft.Text(value=" ", size=18, weight=ft.FontWeight.W_500,
                                        text_align=ft.TextAlign.START, width=170, max_lines=1)
                            ]

                        )
                    )

            self.BookColumn.append(self.BookRow)
            self.BookRow = ft.Row(scroll=ft.ScrollMode.ALWAYS, alignment=ft.MainAxisAlignment.START,
                                  vertical_alignment=ft.CrossAxisAlignment.START)

        self.BookShelf = ft.Column(controls=self.BookColumn, alignment=ft.MainAxisAlignment.START,
                                   horizontal_alignment=ft.CrossAxisAlignment.START)
        self.BookContainer = ft.Container(
            content=self.BookShelf, padding=0, margin=ft.Margin(left=12, top=0, right=12, bottom=0), alignment=ft.alignment.center_left)
        return self.BookContainer

    def goToBook(self, e, book_id):
        self.page.go(f"/book/edit/{book_id}")

    def deleteBook(self, e, book_id):
        self.page.db.delBook(book_id)
        self.page.snack_bar.open = True

        # Refreshes view to get new books
        self.page.go("/book/")
        self.page.go("/books/edit")
