import flet as ft

def get_login_screen(page: ft.Page, on_login: callable, switch_to_register: callable) -> ft.Container:
    """
    Retorna o layout da tela de login.
    :param on_login: Função chamada ao clicar no botão "Entrar".
    :param switch_to_register: Função chamada ao clicar no botão "Registrar".
    """
    # Variáveis para armazenar os valores dos campos
    email_field = ft.TextField(
        hint_text="exemplo@exemplo.com",
        border_color="#e4b849",  # Dourado
        border_radius=ft.border_radius.all(20),
        text_style=ft.TextStyle(color=ft.colors.WHITE),
    )
    
    password_field = ft.TextField(
        hint_text="●●●●●●●●",
        password=True,
        border_color="#e4b849",  # Dourado
        border_radius=ft.border_radius.all(20),
        text_style=ft.TextStyle(color=ft.colors.WHITE),
    )
    
    def handle_login(e):
        print("Botão de login clicado")
        print(f"Email: {email_field.value}")
        print(f"Senha: {password_field.value}")
        if email_field.value and password_field.value:
            print("Campos preenchidos, chamando on_login")
            on_login(email_field.value, password_field.value)  # Passa os valores para on_login
        else:
            print("Campos não preenchidos")
    
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
                                "Bem-vindo",
                                size=28,
                                weight=ft.FontWeight.BOLD,
                                color=ft.colors.BLACK,
                                text_align=ft.TextAlign.CENTER,
                            ),
                            ft.Text(
                                "Por favor, faça login para continuar",
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
                # Container dos campos de login sobreposto
                ft.Container(
                    width=400,
                    height=730,
                    bgcolor="#1c1c1c",  # Fundo escuro
                    border_radius=ft.border_radius.all(40),
                    padding=ft.padding.all(20),
                    content=ft.Column(
                        [
                            ft.Text(
                                "Email",
                                size=14,
                                color=ft.colors.WHITE,
                            ),
                            email_field,
                            ft.Text(
                                "Senha",
                                size=14,
                                color=ft.colors.WHITE,
                            ),
                            password_field,
                            ft.Row(
                                [
                                    ft.TextButton(
                                        "Esqueceu a senha?",
                                        on_click=lambda _: print("Recuperação de senha"),
                                        style=ft.ButtonStyle(color=ft.colors.WHITE),
                                    ),
                                ],
                                alignment=ft.MainAxisAlignment.CENTER,
                            ),
                            ft.ElevatedButton(
                                "Entrar",
                                bgcolor="#e4b849",  # Dourado
                                color=ft.colors.BLACK,
                                on_click=handle_login,
                                width=300,
                                height=50,
                                style=ft.ButtonStyle(
                                    shape=ft.RoundedRectangleBorder(radius=30),
                                ),
                            ),
                            ft.ElevatedButton(
                                "Registrar",
                                bgcolor="#1c1c1c",  # Cor de fundo do painel
                                color="#e4b849",  # Dourado
                                on_click=lambda _: switch_to_register(),
                                width=300,
                                height=50,
                                style=ft.ButtonStyle(
                                    shape=ft.RoundedRectangleBorder(radius=30),
                                    side=ft.BorderSide(1, "#e4b849"),
                                ),
                            ),
                            ft.Text(
                                "",
                                color=ft.colors.WHITE,
                                size=14,
                            ),
                            ft.Row(
                                [],
                                alignment=ft.MainAxisAlignment.CENTER,
                            ),
                            ft.Row(
                                [
                                    ft.Text(
                                        "Não tem uma conta?",
                                        color=ft.colors.WHITE,
                                    ),
                                    ft.TextButton(
                                        "Registrar",
                                        on_click=lambda _: switch_to_register(),
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
