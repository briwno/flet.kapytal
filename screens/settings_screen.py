import flet as ft
from components.navbar import get_navbar

def get_settings_screen(page: ft.Page, on_back: callable, on_logout: callable) -> ft.Container:
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

                        # Configurações do aplicativo
                        ft.Container(
                            alignment=ft.alignment.center,
                            padding=ft.padding.only(top=10, bottom=20),
                            content=ft.Column(
                                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                spacing=10,
                                controls=[
                                    ft.Text(
                                        "Configurações do Aplicativo",
                                        size=20,
                                        weight=ft.FontWeight.BOLD,
                                        color=SOFT_GOLD,
                                    ),
                                    ft.Text(
                                        "Gerencie suas preferências e configurações.",
                                        size=14,
                                        color="#FFFFFF",
                                    ),
                                ],
                            ),
                        ),
                        
                        # Opções de configuração
                        ft.Container(
                            bgcolor=DARK_BG,
                            padding=ft.padding.all(20),
                            border_radius=ft.border_radius.all(20),
                            content=ft.Column(
                                spacing=10,
                                controls=[
                                    settings_option(
                                        icon=ft.icons.PASSWORD,
                                        text="Senha",
                                        color=SOFT_GOLD,
                                        bgcolor=ICON_BG,
                                        on_click=lambda _: page.go("/change_password"),
                                    ),
                                    settings_option(
                                        icon=ft.icons.NOTIFICATIONS,
                                        text="Notificações",
                                        color=SOFT_GOLD,
                                        bgcolor=ICON_BG,
                                        on_click=lambda _: page.go("/notifications_settings"),
                                    ),
                                    settings_option(
                                        icon=ft.icons.CONTRAST,
                                        text="Tema",
                                        color=SOFT_GOLD,
                                        bgcolor=ICON_BG,
                                        on_click=lambda _: page.go("/theme_settings"),
                                    ),
                                    settings_option(
                                        icon=ft.icons.LOGOUT,
                                        text="Sair",
                                        color=SOFT_GOLD,
                                        bgcolor=ICON_BG,
                                        on_click=on_logout,
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
    
    # Função auxiliar para criar opções de configuração
def settings_option(icon, text, color, bgcolor, on_click=None):
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
