import flet as ft

from .questions import QuestionGenerator as qg
from .view import View

class ScorePage(View):
    score_text = ft.Text(
        f'Pontuação Final\n{1} de {1}\nOperação: {"+"}',
        size=20,
        text_align=ft.TextAlign.CENTER
    )
    back_to_menu = ft.FilledButton('Voltar ao menu')
    content_controls = [
        ft.Container(
            bgcolor=ft.colors.ON_PRIMARY,
            border=ft.border.all(
                2, ft.colors.PRIMARY
            ),
            padding=ft.padding.all(10),
            content=ft.Column(
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                controls=[
                    score_text,
                    back_to_menu
                ]
            )
        ),
    ]

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.back_to_menu.on_click = lambda e: e.page.go('/menu')

    def on_pre_view(self, e):
        score = e.page.client_storage.get('score')
        current_level = e.page.client_storage.get('current_level')
        operation = qg.operations.get(
            e.page.client_storage.get('operation')
        )
        self.score_text.value = f'Pontuação Final\n{score} de {current_level}\nOperação: {operation}'
