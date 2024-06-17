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

class MathSymbolButton(ft.Container):
    size = 100
    def __init__(self, operation, **kwargs):
        self.operation = operation
        super().__init__(
            content=ft.FilledButton(
                content=ft.Text(
                    operation,
                    size=24,
                    text_align=ft.TextAlign.CENTER
                ),
                style=ft.ButtonStyle(
                    shape=ft.RoundedRectangleBorder(radius=0),
                    bgcolor=ft.colors.INVERSE_PRIMARY,
                    color=ft.colors.WHITE
                ),
                on_click=self.on_click_event
            ),
            width=self.size,
            height=self.size,
            bgcolor=ft.colors.TRANSPARENT,
            **kwargs
        )

    def on_click_event(self, e):
        e.page.client_storage.set(
            'operation', self.operation
        )
        e.page.go('/game')
