import flet as ft
from components.navbar import get_navbar
from storage.data.user_data import get_user_credentials

def get_profile_screen(page: ft.Page, on_back: callable, on_logout: callable, user_id: str) -> ft.Container:
    
    # Definindo cores personalizadas
    GOLD = "#FFD700"
    SOFT_GOLD = "#F7D679"
    DARK_BG = "#121212"
    CARD_BG = "#1A1A1A"
    ICON_BG = "#262626"

    user_credentials = get_user_credentials(user_id)
    nome, email, senha = user_credentials[0], user_credentials[1], user_credentials[2]

    def handle_logout(e):
        on_logout()

    return ft.Container(
        width=400,
        height=830,
        bgcolor=DARK_BG,
        border_radius=ft.border_radius.all(35),
        content=ft.Stack(
            controls=[
                ft.Column(
                    controls=[
                        # Cabeçalho
                        ft.Container(
                            padding=ft.padding.symmetric(horizontal=16, vertical=30),
                            content=ft.Row(
                                controls=[
                                    ft.IconButton(
                                        icon=ft.icons.ARROW_BACK,
                                        icon_color=SOFT_GOLD,
                                        on_click=on_back(),
                                        icon_size=20,
                                    ),
                                    ft.Text(
                                        "Perfil",
                                        size=20,
                                        weight=ft.FontWeight.BOLD,
                                        color=SOFT_GOLD,
                                    ),
                                    ft.IconButton(
                                        icon=ft.icons.NOTIFICATIONS_NONE,
                                        icon_color=SOFT_GOLD,
                                        on_click=lambda _: page.go("/notifications"),
                                        icon_size=20,
                                    ),
                                ],
                                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                                vertical_alignment=ft.CrossAxisAlignment.CENTER,
                            ),
                        ),

                        # Imagem de perfil e nome
                        ft.Container(
                            alignment=ft.alignment.center,
                            padding=ft.padding.only(top=10, bottom=20),
                            content=ft.Column(
                                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                spacing=10,
                                controls=[
                                    ft.CircleAvatar(
                                        radius=40,
                                        bgcolor=ICON_BG,
                                        content=ft.Icon(
                                            ft.icons.PERSON,
                                            color=SOFT_GOLD,
                                            size=40,
                                        ),
                                    ),
                                    ft.Text(
                                        nome,
                                        size=18,
                                        weight=ft.FontWeight.BOLD,
                                        color=SOFT_GOLD,
                                    ),
                                    ft.Text(
                                        f"ID: {user_id}",
                                        size=12,
                                        color="#666666",
                                    ),
                                ],
                            ),
                        ),

                        # Lista de opções
                        ft.Column(
                            controls=[
                                profile_option(ft.icons.EDIT, "Editar Dados", SOFT_GOLD, ICON_BG, on_click=lambda _: page.go("/edit_profile")),
                                profile_option(ft.icons.SETTINGS, "Configurações", SOFT_GOLD, ICON_BG, on_click=lambda _: page.go("/settings")),
                                profile_option(ft.icons.INFO, "Sobre", SOFT_GOLD, ICON_BG, on_click=lambda _: page.go("/info")),
                                profile_option(ft.icons.LOGOUT, "Sair", SOFT_GOLD, ICON_BG, on_click=handle_logout),
                            ],
                            spacing=8,
                            alignment=ft.MainAxisAlignment.CENTER,
                        ),

                        ft.Container(height=80),  # Espaço para a navbar
                    ],
                    alignment=ft.MainAxisAlignment.START,
                    spacing=0,
                ),
                # Navbar fixa
                get_navbar(page, active_index=4),
            ]
        ),
    )

# Função auxiliar para criar opções de perfil
def profile_option(icon, text, color, bgcolor, on_click=None):
    return ft.Container(
        content=ft.Row(
            controls=[
                ft.Container(
                    content=ft.IconButton(
                        icon=icon,
                        icon_color=color,
                        icon_size=24,
                        on_click=on_click
                    ),
                    bgcolor=bgcolor,
                    padding=8,
                    border_radius=12,
                ),
                ft.Text(
                    text,
                    size=16,
                    color=color,
                    weight=ft.FontWeight.W_500,
                ),
            ],
            spacing=10,
        ),
        padding=12,
        border_radius=12,
        margin=ft.margin.symmetric(vertical=4, horizontal=20),
    )
