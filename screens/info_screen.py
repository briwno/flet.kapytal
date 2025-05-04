import flet as ft
from components.navbar import get_navbar

def get_info_screen(page: ft.Page, on_back: callable, on_logout: callable) -> ft.Container:
    # Definindo cores personalizadas
    GOLD = "#FFD700"
    SOFT_GOLD = "#F7D679"
    DARK_BG = "#121212"
    CARD_BG = "#1A1A1A"
    ICON_BG = "#262626"
    
    def handle_back():
        page.go("/profile")
        
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
                                        on_click=lambda _: handle_back(),
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

                        # Sobre o aplicativo
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
                                            ft.icons.INFO,
                                            color=SOFT_GOLD,
                                            size=40,
                                        ),
                                    ),
                                    ft.Text(
                                        "Sobre o Aplicativo",
                                        size=20,
                                        weight=ft.FontWeight.BOLD,
                                        color=SOFT_GOLD,
                                    ),
                                    ft.Text(
                                        "Este aplicativo fornece informações financeiras em tempo real, incluindo cotações de moedas e notícias econômicas.",
                                        size=14,
                                        color=SOFT_GOLD,
                                        text_align=ft.TextAlign.CENTER,
                                    ),
                                ],
                            ),
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
