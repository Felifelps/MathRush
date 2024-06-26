import flet as ft

from .components import Message
from .game_page import GamePage
from .menu_page import MenuPage
from .score_page import ScorePage
from .view import View

def main(page: ft.Page):
    page.title = "MathRush"
    page.theme = ft.Theme(color_scheme_seed='green')
    page.snack_bar = Message(page)

    View.page = page

    page.views.extend([
        GamePage(route="/game"),
        ScorePage(route="/score"),
        MenuPage(route="/"),
    ])

    page.on_error = lambda e: print(e.name, e.control, e.data)

    def on_route_change(e):
        page.views.sort(key=lambda view: view.route == page.route)
        page.views[-1].on_pre_view(e)
        page.update()

    page.on_route_change = on_route_change
    page.go('/')
