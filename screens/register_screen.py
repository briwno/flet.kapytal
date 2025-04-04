import flet as ft

def get_register_screen(page: ft.Page, on_register: callable, switch_to_login: callable) -> ft.Container:
    """
    Retorna o layout da tela de registro.
    :param on_register: Função chamada ao clicar no botão "Registrar".
    :param switch_to_login: Função chamada ao clicar no botão "Voltar para Login".
    """
    return ft.Container(
        width=400,
        height=830,
        bgcolor="#000000",  # Fundo preto
        border_radius=ft.border_radius.all(40),
        padding=ft.padding.all(20),
        content=ft.Column(
            [
                ft.Text(
                    "Registrar",
                    size=28,
                    weight=ft.FontWeight.BOLD,
                    color=ft.colors.WHITE,
                    text_align=ft.TextAlign.CENTER,
                ),
                ft.TextField(
                    hint_text="Nome",
                    border_color="#e4b849",
                    border_radius=ft.border_radius.all(20),
                    text_style=ft.TextStyle(color=ft.colors.WHITE),
                ),
                ft.TextField(
                    hint_text="Email",
                    border_color="#e4b849",
                    border_radius=ft.border_radius.all(20),
                    text_style=ft.TextStyle(color=ft.colors.WHITE),
                ),
                ft.TextField(
                    hint_text="Senha",
                    password=True,
                    border_color="#e4b849",
                    border_radius=ft.border_radius.all(20),
                    text_style=ft.TextStyle(color=ft.colors.WHITE),
                ),
                ft.ElevatedButton(
                    "Registrar",
                    bgcolor="#e4b849",
                    color=ft.colors.BLACK,
                    on_click=lambda _: on_register(),
                    width=300,
                    height=50,
                    style=ft.ButtonStyle(
                        shape=ft.RoundedRectangleBorder(radius=30),
                    ),
                ),
                ft.TextButton(
                    "Voltar para Login",
                    on_click=lambda _: switch_to_login(),
                    style=ft.ButtonStyle(color="#e4b849"),
                ),
            ],
            spacing=15,
            alignment=ft.MainAxisAlignment.CENTER,
        )
    )