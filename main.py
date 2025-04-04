import flet as ft
import threading  # Para usar o Timer
from screens.login_screen import get_login_screen  # Importa a tela de login

def create_iphone_layout(content: ft.Control) -> ft.Stack:
    """
    Cria o layout do iPhone com moldura e conteúdo interativo.
    A moldura é exibida na frente, mas não bloqueia interações.
    """
    return ft.Stack(
        [
            content,  # Conteúdo interativo
            ft.TransparentPointer(  # Permite que eventos de clique passem através da moldura
                content=ft.Image(
                    src="assets/iphone-moldure.png",
                    width=430,
                    height=932,
                    fit=ft.ImageFit.CONTAIN,
        
                ),
            ),
        ],
        alignment=ft.alignment.center,
        expand=True,
    )



def create_initial_screen() -> ft.Container:
    """
    Cria a tela inicial do aplicativo.
    :return: Um ft.Container representando a tela inicial.
    """
    return ft.Container(
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
    # Criação das telas
    initial_screen = create_initial_screen()
    login_screen = get_login_screen(on_login=lambda: print("Login realizado com sucesso!"))

    # Layout inicial com moldura
    iphone_layout = create_iphone_layout(initial_screen)
    page.add(ft.Row([iphone_layout], alignment=ft.MainAxisAlignment.CENTER))

    # Função para trocar para a tela de logi
    def switch_to_login():
        page.clean()
        iphone_layout_login = create_iphone_layout(login_screen)
        page.add(ft.Row([iphone_layout_login], alignment=ft.MainAxisAlignment.CENTER))
        page.update()

    # Troca para a tela de login após 3 segundos
    threading.Timer(0.1, switch_to_login).start()


# Inicializa o aplicativo
ft.app(target=main)