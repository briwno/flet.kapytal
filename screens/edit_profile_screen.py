import flet as ft
from components.navbar import get_navbar
from storage.data.user_data import get_user_credentials, update_user

def get_edit_profile_screen(page: ft.Page, on_back: callable, on_logout: callable, user_id: str) -> ft.Container:
    # Definindo cores personalizadas
    GOLD = "#FFD700"
    SOFT_GOLD = "#F7D679"
    DARK_BG = "#121212"
    CARD_BG = "#1A1A1A"
    ICON_BG = "#262626"

    user_credentials = get_user_credentials(user_id)
    nome, email, senha = user_credentials[0], user_credentials[1], user_credentials[2]

    def handle_back(e):
        if len(page.views) > 1:
            page.views.pop()
            page.update()

    def handle_logout(e):
        on_logout()

    def handle_save(e):
        if name_input.value and email_input.value and password_input.value:
            success, message = update_user(
                user_id,
                name=name_input.value,
                email=email_input.value,
                password=password_input.value,
            )
            if success:
                print("Dados atualizados com sucesso!")
                page.go("/profile")
            else:
                print(f"Erro: {message}")
        else:
            print("Preencha todos os campos.")

    # Campos de entrada para edição de perfil
    name_input = ft.TextField(
        label="Nome", value=nome, bgcolor=CARD_BG, border_radius=10, color=SOFT_GOLD
    )
    email_input = ft.TextField(
        label="E-mail", value=email, bgcolor=CARD_BG, border_radius=10, color=SOFT_GOLD
    )
    password_input = ft.TextField(
        label="Senha", value=senha, bgcolor=CARD_BG, border_radius=10, color=SOFT_GOLD, password=True
    )

    return ft.Container(
        width=400,
        height=830,
        bgcolor=DARK_BG,
        border_radius=ft.border_radius.all(35),
        padding=ft.padding.only(left=20, right=20),
        content=ft.Stack(
            [
                ft.Column(
                    [
                        ft.Container(height=45),  # Espaço superior
                        # Cabeçalho
                        ft.Row(
                            [
                                ft.IconButton(
                                    icon=ft.icons.ARROW_BACK,
                                    icon_color=SOFT_GOLD,
                                    on_click=handle_back,
                                ),
                                ft.Text(
                                    "Editar Perfil",
                                    size=20,
                                    weight=ft.FontWeight.BOLD,
                                    color=SOFT_GOLD,
                                ),
                                ft.IconButton(
                                    icon=ft.icons.LOGOUT,
                                    icon_color=SOFT_GOLD,
                                    on_click=handle_logout,
                                ),
                            ],
                            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                        ),
                        ft.Container(height=20),
                        # Formulário de edição
                        ft.Container(
                            content=ft.Column(
                                [
                                    name_input,
                                    ft.Container(height=10),
                                    email_input,
                                    ft.Container(height=10),
                                    password_input,
                                    ft.Container(height=20),
                                    ft.ElevatedButton(
                                        "Salvar",
                                        on_click=handle_save,
                                        bgcolor=SOFT_GOLD,
                                        color=DARK_BG,
                                        width=300,
                                    ),
                                ],
                                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                            ),
                            bgcolor=CARD_BG,
                            padding=20,
                            border_radius=15,
                        ),
                    ],
                    scroll=ft.ScrollMode.AUTO,
                    expand=True,
                ),
                # Navbar fixa
                get_navbar(page, active_index=4),
            ],
        ),
    )


