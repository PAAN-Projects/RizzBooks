import flet as ft

from random import randint


class bookAdd(ft.UserControl):
    def build(self):
        self.selected_files = ft.Text(weight=ft.FontWeight.W_500, size=24)
        self.book_cover = ft.Image(
            visible=False, height=340, border_radius=ft.border_radius.all(10), fit=ft.ImageFit.CONTAIN
        )
        self.file_picker = ft.Row(controls=[
            ft.FilledButton(
                "Add cover image",
                icon=ft.icons.UPLOAD_FILE,
                on_click=self.handlePickFiles,

            ),
            self.selected_files,
        ])

        self.book_name = ft.TextField(label="Name")
        self.book_desc = ft.TextField(label="Description", multiline=True)
        self.book_year = ft.TextField(label="Publish year")
        self.book_age_rating = ft.TextField(label="Age rating")
        self.book_genre = ft.TextField(label="Genre")
        self.book_stock = ft.TextField(label="Stock")

        self.add_book_button = ft.FilledButton(
            "Add book", icon=ft.icons.ADD_ROUNDED, on_click=self.addBookDb)

        self.warningSnackBar = ft.SnackBar(
            ft.Text("Something went wrong"))
        return ft.Container(content=ft.Column(controls=[
            self.book_cover,
            self.file_picker,
            self.book_name,
            self.book_desc,
            self.book_year,
            self.book_age_rating,
            self.book_genre,
            self.book_stock,
            self.add_book_button,
            self.warningSnackBar
        ], alignment=ft.MainAxisAlignment.CENTER), alignment=ft.alignment.center, padding=50)

    def handlePickFiles(self, e):
        self.page.pick_files_dialog.on_result = self.pick_files_result
        self.page.pick_files_dialog.pick_files(
            allow_multiple=False,
            allowed_extensions=['png']
        ),

    def pick_files_result(self, e: ft.FilePickerResultEvent):
        self.selected_files.value = f"{e.files[0].name} - {e.files[0].size / 1000}kb"
        self.book_cover.src = e.files[0].path
        self.book_cover.visible = True

        self.book_cover.update()
        self.selected_files.update()

    def upload_files(self):
        upload_list = []
        if self.page.pick_files_dialog.result != None and self.page.pick_files_dialog.result.files != None:
            for f in self.page.pick_files_dialog.result.files:
                upload_list.append(
                    ft.FilePickerUploadFile(
                        f.name,
                        upload_url=self.page.get_upload_url(
                            f"{self.book_name.value}.png", 600),
                        method="PUT"
                    )
                )
            self.page.pick_files_dialog.upload(upload_list)

    def addBookDb(self, e):
        self.warningSnackBar.content = ft.Text("Something went wrong")
        if self.page.session.get("current_user") == None:
            self.warningSnackBar.content = ft.Text("Please login.")
            self.warningSnackBar.open = True
            self.update()
        elif self.book_name.value == "" or self.book_desc.value == "" or self.book_year.value == "" or self.book_age_rating.value == "" or self.book_genre.value == "" or self.book_stock.value == "":
            self.warningSnackBar.open = True
            self.update()
            return
        else:
            try:
                book_id = randint(1_000_000, 9_999_999)
                self.page.db.addBook(self.page.session.get("current_user"), book_id, self.book_name.value, self.book_desc.value, int(
                    self.book_year.value), 0, int(self.book_age_rating.value), int(self.book_stock.value), self.book_genre.value)
                self.upload_files()

                self.warningSnackBar.content = ft.Text(
                    "Book added successfully!")
                self.warningSnackBar.open = True
                self.update()
            except:
                print("ERR")
                self.warningSnackBar.open = True
                self.update()
