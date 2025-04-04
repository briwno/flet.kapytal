import flet as ft
import threading
from screens.login_screen import get_login_screen
from screens.register_screen import get_register_screen
from layout import create_iphone_layout


def main(page: ft.Page):
    """
    Função principal do aplicativo.
    :param page: A página principal do Flet.
    """
    # Configurações iniciais da página
    page.title = "Simulação iPhone"
    page.window_width = 430
    page.window_height = 932
    page.bgcolor = ft.colors.BLACK
    page.update()

    # Funções de troca de tela
    def switch_to_login():
        login_screen = get_login_screen(
            page,
            on_login=lambda: print("Login clicado!"),
            switch_to_register=switch_to_register
        )
        page.clean()
        page.add(ft.Row([create_iphone_layout(login_screen)], alignment=ft.MainAxisAlignment.CENTER))
        page.update()

    def switch_to_register():
        register_screen = get_register_screen(
            page,
            on_register=lambda: print("Registrar clicado!"),
            switch_to_login=switch_to_login
        )
        page.clean()
        page.add(ft.Row([create_iphone_layout(register_screen)], alignment=ft.MainAxisAlignment.CENTER))
        page.update()

    # Tela inicial
    initial_screen = ft.Container(
        width=390,
        height=844,
        bgcolor=ft.colors.WHITE70,
        border_radius=ft.border_radius.all(50),
        padding=ft.padding.all(10),
        content=ft.Column(
            [
                ft.Text(
                    "Bem-vindo ao App!",
                    size=30,
                    color=ft.colors.BLACK,
                    text_align=ft.TextAlign.CENTER
                ),
                ft.Text(
                    "Esta é uma simulação de iPhone.",
                    size=20,
                    color=ft.colors.BLACK,
                    text_align=ft.TextAlign.CENTER
                ),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        )
    )

    # Exibe a tela inicial e troca para login após 0.1 segundos
    page.add(ft.Row([create_iphone_layout(initial_screen)], alignment=ft.MainAxisAlignment.CENTER))
    threading.Timer(0.1, switch_to_login).start()


# Inicializa o aplicativo
ft.app(target=main)