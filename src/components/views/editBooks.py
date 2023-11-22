import flet as ft

from database import ORM


class editBooks(ft.UserControl):
    def did_mount(self):
        self.book_id = self.page.route.removeprefix("/book/edit/")
        self.book = self.db.getBook(self.book_id)

        self.book_stock = ft.TextField(label="Stock", value=self.book[0][6])
        self.updateButton = ft.FilledButton(
            text="Update", on_click=self.updateStock)
        self.warn = ft.SnackBar(content=ft.Text(
            "Updated Stock!"), bgcolor="green")
        self.layout = ft.Column(
            controls=[self.book_stock, self.updateButton, self.warn])

        self.content.append(self.layout)
        self.update()
        return super().did_mount()

    def build(self):
        self.db = ORM()
        self.books = self.db.getAllBooks()

        self.content = []
        return self.content

    def updateStock(self, e):
        self.page.db.updateBook(self.book_id, self.book_stock.value)
        self.warn.open = True
        self.update()
