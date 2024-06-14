import flet as ft

from .components import MathSymbolButton
from .view import View


class MenuPage(View):
    content_controls = [
        ft.Container(
            expand=True,
            expand_loose=True,
            width=MathSymbolButton.size * 2,
            height=MathSymbolButton.size * 3.1,
            image_src="menu.png",
            content=ft.GridView(
                controls=[
                    MathSymbolButton('+'),
                    MathSymbolButton('-'),
                    MathSymbolButton('x'),
                    MathSymbolButton('/'),
                    MathSymbolButton('^'),
                    MathSymbolButton('√'),
                ],
                runs_count=2,
                child_aspect_ratio=1.0,
                spacing=10,
                run_spacing=10,
            )
        )
        
    ]