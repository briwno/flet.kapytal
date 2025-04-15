import flet as ft

def get_navbar(page: ft.Page, active_index: int = 0) -> ft.Container:
    # Definindo cores personalizadas
    DARK_BG = "#121212"
    SOFT_GOLD = "#F7D679"
    
    def handle_nav(e, index):
        if index == 0:  # Home
            page.go("/home")
        elif index == 1:  # Análise
            page.go("/analysis")
        elif index == 2:  # Transações
            page.go("/transactions")
        elif index == 3:  # Carteira
            page.go("/wallet")
        elif index == 4:  # Perfil
            page.go("/profile")
            
    return ft.Container(
        content=ft.Container(
            content=ft.Row(
                [
                    ft.IconButton(
                        icon=ft.icons.HOME,
                        icon_color=DARK_BG,
                        icon_size=22,
                        opacity=1.0 if active_index == 0 else 0.5,
                        on_click=lambda e: handle_nav(e, 0),
                    ),
                    ft.IconButton(
                        icon=ft.icons.INSERT_CHART_OUTLINED,
                        icon_color=DARK_BG,
                        icon_size=22,
                        opacity=1.0 if active_index == 1 else 0.5,
                        on_click=lambda e: handle_nav(e, 1),
                    ),
                    ft.Container(
                        content=ft.IconButton(
                            icon=ft.icons.SWAP_HORIZ,
                            icon_color=DARK_BG,
                            icon_size=22,
                            opacity=1.0 if active_index == 2 else 0.5,
                            on_click=lambda e: handle_nav(e, 2),
                        ),
                        bgcolor=SOFT_GOLD,
                        shape=ft.BoxShape.CIRCLE,
                        border=ft.border.all(2, DARK_BG) if active_index == 2 else None,
                    ),
                    ft.IconButton(
                        icon=ft.icons.ACCOUNT_BALANCE_WALLET,
                        icon_color=DARK_BG,
                        icon_size=22,
                        opacity=1.0 if active_index == 3 else 0.5,
                        on_click=lambda e: handle_nav(e, 3),
                    ),
                    ft.IconButton(
                        icon=ft.icons.PERSON,
                        icon_color=DARK_BG,
                        icon_size=22,
                        opacity=1.0 if active_index == 4 else 0.5,
                        on_click=lambda e: handle_nav(e, 4),
                    ),
                ],
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            ),
            bgcolor=SOFT_GOLD,
            padding=ft.padding.symmetric(horizontal=25, vertical=10),
            border_radius=30,
            width=280,
        ),
        margin=ft.margin.only(top=700),
        alignment=ft.alignment.center,
    ) 