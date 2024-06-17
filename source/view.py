import flet as ft

class View(ft.View):
    page = None
    title = 'MathRush'
    title_padding = 20
    content_controls = []
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.drawer = self.page.drawer
        self.controls = self.generate_main_content()

    def on_pre_view(self, e):
        pass

    def generate_main_content(self):
        return [
            Title(self.title, self.title_padding),
            ft.Container(
                alignment=ft.alignment.center,
                expand=True,
                content=ft.Column(
                    alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    width=self.page.window_width,
                    controls=self.content_controls
                )
            ),
            ft.Container(
                alignment=ft.alignment.bottom_center,
                content=ft.Column(
                    alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    controls=[
                        ft.TextButton(
                            content=ft.Text(
                                '@felifelps.dev',
                                text_align=ft.TextAlign.CENTER,
                            ),
                            url="https://www.instagram.com/felifelps.dev/",
                        ),
                        
                    ]
                )
            )
        ]

class Title(ft.Container):
    def __init__(self, title, title_padding, **kwargs):
        super().__init__(**kwargs)
        self.content = ft.Row(
            alignment=ft.MainAxisAlignment.CENTER,
            controls=[
                ft.Container(
                    expand=True,
                    alignment=ft.alignment.center,
                    padding=ft.padding.all(title_padding),
                    content=ft.Row(
                        alignment=ft.MainAxisAlignment.CENTER,
                        controls=[
                            ft.Text(
                                title,
                                size=40,
                            ),
                        ]
                    ),
                    bgcolor=ft.colors.INVERSE_PRIMARY
                )
            ]
        )
        self.alignment = ft.alignment.top_center
