import flet as ft
from components.navbar import get_navbar

def get_profile_screen(page: ft.Page, on_back: callable, on_logout: callable) -> ft.Container:
    # Definindo cores personalizadas
    GOLD = "#FFD700"
    SOFT_GOLD = "#F7D679"
    DARK_BG = "#121212"
    CARD_BG = "#1A1A1A"
    ICON_BG = "#262626"

    def handle_back(e):
        on_back()

    def handle_logout(e):
        on_logout()

    return ft.Container(
        width=400,
        height=830,
        bgcolor=DARK_BG,
        border_radius=ft.border_radius.all(35),
        content=ft.Stack(
            [
                ft.Column(
                    [
                        # Cabeçalho
                        ft.Container(
                            padding=ft.padding.symmetric(horizontal=16, vertical=30),  # Adiciona espaçamento interno
                            content=ft.Row(
                                [
                                    ft.IconButton(
                                        icon=ft.icons.ARROW_BACK,
                                        icon_color=SOFT_GOLD,
                                        on_click=handle_back,
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
                                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,  # Garante espaçamento entre os itens
                                vertical_alignment=ft.CrossAxisAlignment.CENTER,  # Centraliza verticalmente os itens
                            ),
                        ),
                        
                        ft.Container(height=10),

                        # Foto e informações do usuário
                        ft.Column(
                            [
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
                                    "Bruno Mito",
                                    size=18,
                                    weight=ft.FontWeight.BOLD,
                                    color=SOFT_GOLD,
                                ),
                                ft.Text(
                                    "ID: 1",
                                    size=12,
                                    color="#666666",
                                ),
                            ],
                            alignment=ft.MainAxisAlignment.CENTER,
                        ),
                        ft.Container(height=20),

                        # Opções do perfil
                        ft.Column(
                            [
                                ft.Container(
                                    content=ft.Row(
                                        [
                                            ft.Container(
                                                content=ft.IconButton(
                                                    icon=ft.icons.EDIT,
                                                    icon_color=SOFT_GOLD,
                                                    icon_size=24,
                                                ),
                                                bgcolor=ICON_BG,
                                                padding=8,
                                                border_radius=12,
                                            ),
                                            ft.Text(
                                                "Editar Perfil",
                                                size=16,
                                                color=SOFT_GOLD,
                                                weight=ft.FontWeight.W_500,
                                            ),
                                        ],
                                        spacing=10,
                                    ),
                                    bgcolor=CARD_BG,
                                    padding=12,
                                    border_radius=12,
                                    margin=ft.margin.symmetric(vertical=4),
                                ),
                                ft.Container(
                                    content=ft.Row(
                                        [
                                            ft.Container(
                                                content=ft.IconButton(
                                                    icon=ft.icons.SECURITY,
                                                    icon_color=SOFT_GOLD,
                                                    icon_size=24,
                                                ),
                                                bgcolor=ICON_BG,
                                                padding=8,
                                                border_radius=12,
                                            ),
                                            ft.Text(
                                                "Segurança",
                                                size=16,
                                                color=SOFT_GOLD,
                                                weight=ft.FontWeight.W_500,
                                            ),
                                        ],
                                        spacing=10,
                                    ),
                                    bgcolor=CARD_BG,
                                    padding=12,
                                    border_radius=12,
                                    margin=ft.margin.symmetric(vertical=4),
                                ),
                                ft.Container(
                                    content=ft.Row(
                                        [
                                            ft.Container(
                                                content=ft.IconButton(
                                                    icon=ft.icons.SETTINGS,
                                                    icon_color=SOFT_GOLD,
                                                    icon_size=24,
                                                ),
                                                bgcolor=ICON_BG,
                                                padding=8,
                                                border_radius=12,
                                            ),
                                            ft.Text(
                                                "Configurações",
                                                size=16,
                                                color=SOFT_GOLD,
                                                weight=ft.FontWeight.W_500,
                                            ),
                                        ],
                                        spacing=10,
                                    ),
                                    bgcolor=CARD_BG,
                                    padding=12,
                                    border_radius=12,
                                    margin=ft.margin.symmetric(vertical=4),
                                ),
                                ft.Container(
                                    content=ft.Row(
                                        [
                                            ft.Container(
                                                content=ft.IconButton(
                                                    icon=ft.icons.HELP,
                                                    icon_color=SOFT_GOLD,
                                                    icon_size=24,
                                                ),
                                                bgcolor=ICON_BG,
                                                padding=8,
                                                border_radius=12,
                                            ),
                                            ft.Text(
                                                "Ajuda",
                                                size=16,
                                                color=SOFT_GOLD,
                                                weight=ft.FontWeight.W_500,
                                            ),
                                        ],
                                        spacing=10,
                                    ),
                                    bgcolor=CARD_BG,
                                    padding=12,
                                    border_radius=12,
                                    margin=ft.margin.symmetric(vertical=4),
                                ),
                                ft.Container(
                                    content=ft.Row(
                                        [
                                            ft.Container(
                                                content=ft.IconButton(
                                                    icon=ft.icons.LOGOUT,
                                                    icon_color=SOFT_GOLD,
                                                    icon_size=24,
                                                ),
                                                bgcolor=ICON_BG,
                                                padding=8,
                                                border_radius=12,
                                            ),
                                            ft.Text(
                                                "Sair",
                                                size=16,
                                                color=SOFT_GOLD,
                                                weight=ft.FontWeight.W_500,
                                            ),
                                        ],
                                        spacing=10,
                                    ),
                                    bgcolor=CARD_BG,
                                    padding=12,
                                    border_radius=12,
                                    margin=ft.margin.symmetric(vertical=4),
                                ),
                            ],
                            spacing=8,
                        ),
                    ],
                ),
                get_navbar(page, active_index=4),
            ],
        ),
    )



