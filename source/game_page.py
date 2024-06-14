import flet as ft

from .questions import QuestionGenerator as qg
from .view import View

class GamePage(View):
    __current_level = 1
    __score = 0
    answer = 2
    operation = '+'
    back_button = ft.IconButton('arrow_back')
    level_counter = ft.Text(
        f'Nível {__current_level}',
        size=30,
        text_align=ft.TextAlign.CENTER,
    )
    score_counter = ft.Text(
        f'Pontuação: {__score}'
    )
    question = ft.Text(
        '1 + 1 = ?',
        size=20
    )
    answer_field = ft.TextField(
        label="Digite a resposta",
        input_filter=ft.NumbersOnlyInputFilter(),
        width=300,
        autofocus=True
    )
    verify_button = ft.FilledButton('Verificar')
    content_controls = [
        ft.Stack([
            ft.Container(
                alignment=ft.alignment.bottom_left,
                content=back_button
            ),
            ft.Row(
                alignment=ft.MainAxisAlignment.CENTER,
                controls=[level_counter]
            )
        ]),
        score_counter,
        ft.Column(
            expand=True,
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                ft.Container(
                    bgcolor=ft.colors.ON_PRIMARY,
                    border=ft.border.all(
                        2, ft.colors.PRIMARY
                    ),
                    padding=ft.padding.all(10),
                    content=question
                ),
                answer_field,
                verify_button
            ]
        )
    ]

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.back_button.on_click = self.show_score
        self.answer_field.on_submit = self.verify
        self.verify_button.on_click = self.verify

    @property
    def current_level(self):
        return self.__current_level

    @current_level.setter
    def current_level(self, value):
        self.__current_level = value
        self.level_counter.value = f'Nível {self.current_level}'

    @property
    def score(self):
        return self.__score

    @score.setter
    def score(self, value):
        self.__score = value
        self.score_counter.value = f'Pontuação: {self.__score}'

    def new_question(self):
        self.question.value, self.answer = qg.gen_question(self.operation)
        self.answer_field.value = ""

    def verify(self, e):
        if not self.answer_field.value:
            return None
        if int(self.answer_field.value) == self.answer:
            self.score += 1
            e.page.snack_bar.message(
                'Resposta correta!',
                'success'
            )
        else:
            e.page.snack_bar.message(
                f'Resposta errada. A correta é: {self.answer}',
                'error'
            )
        self.current_level += 1
        self.new_question()
        e.page.update()
        try:
            self.answer_field.focus()
            # The line above may show an assertion error,
            # but this doesn't change the user experience at all
        except AssertionError:
            pass

    def on_pre_view(self, e):
        self.current_level = 1
        self.score = 0
        self.operation = e.page.client_storage.get('operation')
        self.new_question()

    def show_score(self, e):
        data = {
            'score': self.score,
            'current_level': self.current_level,
            'operation': self.operation
        }
        for key, value in data.items():
            e.page.client_storage.set(
                key, value
            )
        e.page.go('/score')
