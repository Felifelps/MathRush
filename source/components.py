import flet as ft

class Message(ft.SnackBar):
    colors = {
        'default': ft.colors.GREY_800,
        'success': ft.colors.GREEN,
        'error': ft.colors.RED
    }
    def __init__(self, page, **kwargs):
        super().__init__(
            content=ft.Text(
                'Default message',
                color=ft.colors.GREY_100
            ),
            **kwargs
        )
        self.page = page

    def message(self, text, color='default'):
        self.content.value = text
        self.bgcolor = self.colors[color]
        self.open = True
        self.page.update()


class CustomButton(ft.FilledButton):
    def __init__(self, text, **kwargs):
        super().__init__(
            content=ft.Text(
                text,
            ),
            style=ft.ButtonStyle(
                shape=ft.RoundedRectangleBorder(
                    radius=10,
                ),
                bgcolor=ft.colors.INVERSE_PRIMARY,
            ),
            **kwargs
        )

class MathSymbolButton(ft.Container):
    size = 100
    def __init__(self, symbol, operation, **kwargs):
        self.operation = operation
        super().__init__(
            content=ft.IconButton(
                style=ft.ButtonStyle(
                    shape=ft.RoundedRectangleBorder(radius=0)
                ),
                content=ft.Text(
                    symbol,
                    size=35,
                    text_align=ft.VerticalAlignment.CENTER
                ),
                on_click=self.on_click_event
            ),
            width=self.size,
            height=self.size,
            bgcolor=ft.colors.INVERSE_PRIMARY,
            **kwargs
        )

    def on_click_event(self, e):
        e.page.client_storage.set(
            'operation', self.operation
        )
        e.page.go('/game')
