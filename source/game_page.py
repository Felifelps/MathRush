import flet as ft

from .view import View

class GamePage(View):
    title = 'Game'
    title_padding = 5
    content_controls = [
        ft.Stack(
            expand=True,
            alignment=ft.alignment.center,
            controls=[
                ft.IconButton(
                    'arrow_back',
                    left=0
                ),
                ft.Column(
                    expand=True,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    controls=[
                        ft.Text(
                            'Nível 1',
                            size=30,
                            text_align=ft.TextAlign.CENTER,
                        ),
                        ft.Container(
                            expand=True,
                            border=ft.border.all(2, ft.colors.PRIMARY),
                            padding=ft.padding.all(20),
                            bgcolor=ft.colors.ON_PRIMARY,
                            content=ft.Text(
                                '1 + 1 = ?'
                            )
                        )
                    ]
                )
            ]
        ),
        
    ]