import flet as ft

def get_register_screen(page: ft.Page, on_register: callable, switch_to_login: callable) -> ft.Container:
    """
    Retorna o layout da tela de registro.
    :param on_register: Função chamada ao clicar no botão "Registrar".
    :param switch_to_login: Função chamada ao clicar no botão "Já tem uma conta? Logar".
    """
    return ft.Container(
        width=400,
        height=830,
        bgcolor="#000000",  # Fundo preto
        border_radius=ft.border_radius.all(40),
        padding=ft.padding.all(0),
        content=ft.Stack(
            [
                # Cabeçalho dourado no fundo
                ft.Container(
                    width=400,
                    height=220,
                    bgcolor="#e4b849",  # Dourado
                    border_radius=ft.BorderRadius(
                        top_left=40,
                        top_right=40,
                        bottom_left=0,
                        bottom_right=0,
                    ),
                    content=ft.Column(
                        [
                            ft.Text(
                                "Criar Conta",
                                size=28,
                                weight=ft.FontWeight.BOLD,
                                color=ft.colors.BLACK,
                                text_align=ft.TextAlign.CENTER,
                            ),
                            ft.Text(
                                "Por favor, preencha os dados abaixo",
                                size=18,
                                color=ft.colors.BLACK,
                                text_align=ft.TextAlign.CENTER,
                            ),
                        ],
                        spacing=15,
                        alignment=ft.MainAxisAlignment.CENTER,
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    )
                ),
                # Container dos campos de registro sobreposto
                ft.Container(
                    width=400,
                    height=730,
                    bgcolor="#1c1c1c",  # Fundo escuro
                    border_radius=ft.border_radius.all(40),
                    padding=ft.padding.all(20),
                    content=ft.Column(
                        [
                            ft.Text(
                                "Nome Completo",
                                size=14,
                                color=ft.colors.WHITE,
                            ),
                            ft.TextField(
                                hint_text="Digite seu nome completo",
                                border_color="#e4b849",  # Dourado
                                border_radius=ft.border_radius.all(20),
                                text_style=ft.TextStyle(color=ft.colors.WHITE),
                            ),
                            ft.Text(
                                "Email",
                                size=14,
                                color=ft.colors.WHITE,
                            ),
                            ft.TextField(
                                hint_text="exemplo@exemplo.com",
                                border_color="#e4b849",  # Dourado
                                border_radius=ft.border_radius.all(20),
                                text_style=ft.TextStyle(color=ft.colors.WHITE),
                            ),
                            ft.Text(
                                "Senha",
                                size=14,
                                color=ft.colors.WHITE,
                            ),
                            ft.TextField(
                                hint_text="●●●●●●●●",
                                password=True,
                                border_color="#e4b849",  # Dourado
                                border_radius=ft.border_radius.all(20),
                                text_style=ft.TextStyle(color=ft.colors.WHITE),
                            ),
                            ft.Text(
                                "Confirmar Senha",
                                size=14,
                                color=ft.colors.WHITE,
                            ),
                            ft.TextField(
                                hint_text="●●●●●●●●",
                                password=True,
                                border_color="#e4b849",  # Dourado
                                border_radius=ft.border_radius.all(20),
                                text_style=ft.TextStyle(color=ft.colors.WHITE),
                            ),
                            ft.ElevatedButton(
                                "Registrar",
                                bgcolor="#e4b849",  # Dourado
                                color=ft.colors.BLACK,
                                on_click=lambda _: on_register(),
                                width=300,
                                height=50,
                                style=ft.ButtonStyle(
                                    shape=ft.RoundedRectangleBorder(radius=30),
                                ),
                            ),
                            ft.Row(
                                [
                                    ft.Text(
                                        "Já tem uma conta?",
                                        color=ft.colors.WHITE,
                                    ),
                                    ft.TextButton(
                                        "Logar",
                                        on_click=lambda _: switch_to_login(),
                                        style=ft.ButtonStyle(color="#e4b849"),
                                    ),
                                ],
                                alignment=ft.MainAxisAlignment.CENTER,
                            ),
                        ],
                        spacing=15,
                        alignment=ft.MainAxisAlignment.CENTER,
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    ),
                    margin=ft.margin.only(top=200),  # Ajusta a sobreposição do container
                ),
            ]
        ),
    )
