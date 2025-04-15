import flet as ft
from components.navbar import get_navbar

def get_profile_screen(page: ft.Page, on_back: callable, on_logout: callable) -> ft.Container:
    # Definindo cores personalizadas
    GOLD = "#FFD700"
    SOFT_GOLD = "#F7D679"
    DARK_BG = "#121212"
    CARD_BG = "#1A1A1A"
    ICON_BG = "#262626"
    BLUE = "#3E83FF"
    
    def handle_back(e):
        on_back()

    def handle_logout(e):
        on_logout()

    return ft.Container(
        width=400,
        height=830,
        bgcolor=DARK_BG,
        border_radius=ft.border_radius.all(35),
        padding=ft.padding.all(20),
        content=ft.Column(
            [
                # Cabeçalho
                ft.Row(
                    [
                        ft.IconButton(
                            icon=ft.icons.ARROW_BACK,
                            icon_color=SOFT_GOLD,
                            on_click=handle_back,
                        ),
                        ft.Text(
                            "Perfil",
                            size=24,
                            weight=ft.FontWeight.BOLD,
                            color=SOFT_GOLD,
                        ),
                        ft.IconButton(
                            icon=ft.icons.NOTIFICATIONS_NONE,
                            icon_color=SOFT_GOLD,
                            on_click=lambda _: page.go("/notifications"),
                        ),
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                ),
                ft.Container(height=20),
                
                # Foto e informações do usuário
                ft.Column(
                    [
                        ft.CircleAvatar(
                            radius=50,
                            bgcolor=ICON_BG,
                            content=ft.Text(
                                "JS",
                                size=24,
                                weight=ft.FontWeight.BOLD,
                                color=SOFT_GOLD,
                            ),
                        ),
                        ft.Text(
                            "John Smith",
                            size=20,
                            weight=ft.FontWeight.BOLD,
                            color=SOFT_GOLD,
                        ),
                        ft.Text(
                            "ID: 25030024",
                            size=14,
                            color="#666666",
                        ),
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                ),
                ft.Container(height=30),

                # Opções do perfil
                ft.Column(
                    [
                        ft.Row(
                            [
                                ft.Icon(
                                    ft.icons.EDIT,
                                    color=SOFT_GOLD,
                                    size=24,
                                ),
                                ft.Text(
                                    "Editar Perfil",
                                    size=16,
                                    color=SOFT_GOLD,
                                ),
                            ],
                            spacing=10,
                        ),
                        ft.Row(
                            [
                                ft.Icon(
                                    ft.icons.SECURITY,
                                    color=SOFT_GOLD,
                                    size=24,
                                ),
                                ft.Text(
                                    "Segurança",
                                    size=16,
                                    color=SOFT_GOLD,
                                ),
                            ],
                            spacing=10,
                        ),
                        ft.Row(
                            [
                                ft.Icon(
                                    ft.icons.SETTINGS,
                                    color=SOFT_GOLD,
                                    size=24,
                                ),
                                ft.Text(
                                    "Configurações",
                                    size=16,
                                    color=SOFT_GOLD,
                                ),
                            ],
                            spacing=10,
                        ),
                        ft.Row(
                            [
                                ft.Icon(
                                    ft.icons.HELP,
                                    color=SOFT_GOLD,
                                    size=24,
                                ),
                                ft.Text(
                                    "Ajuda",
                                    size=16,
                                    color=SOFT_GOLD,
                                ),
                            ],
                            spacing=10,
                        ),
                        ft.Row(
                            [
                                ft.Icon(
                                    ft.icons.LOGOUT,
                                    color=SOFT_GOLD,
                                    size=24,
                                ),
                                ft.TextButton(
                                    "Sair",
                                    on_click=handle_logout,
                                    style=ft.ButtonStyle(color=SOFT_GOLD),
                                ),
                            ],
                            spacing=10,
                        ),
                    ],
                    spacing=15,
                ),
                ft.Container(height=30),

                # Navbar
                get_navbar(page, active_index=3),
            ],
            alignment=ft.MainAxisAlignment.START,
        ),
    )



