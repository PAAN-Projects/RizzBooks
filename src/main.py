import flet as ft


def main(page: ft.Page):
    page.theme_mode = "light"
    page.title = "DEEZ Books"

    page.fonts = {
    }

    def check_item_clicked(e):
        e.control.checked = not e.control.checked
        page.update()

    page.appbar = ft.AppBar(
        leading_width=40,
        title=ft.Text("DEEZ"),
        center_title=False,
        bgcolor=ft.colors.SURFACE_VARIANT,
        actions=[
            # ft.IconButton(ft.icons.WB_SUNNY_OUTLINED),
        ],
    )
    page.add(ft.Text("Body!"))


ft.app(target=main, assets_dir="assets")
