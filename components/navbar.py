import flet as ft

def get_navbar(page: ft.Page, active_index: int = 0) -> ft.Container:
    # Definindo cores personalizadas
    DARK_BG = "#121212"
    SOFT_GOLD = "#F7D679"
    
    return ft.Container(
        content=ft.Container(
            content=ft.Row(
                [
                    ft.IconButton(
                        icon=ft.icons.HOME,
                        icon_color=DARK_BG,
                        icon_size=22,
                        opacity=1.0 if active_index == 0 else 0.5,
                    ),
                    ft.IconButton(
                        icon=ft.icons.SEARCH,
                        icon_color=DARK_BG,
                        icon_size=22,
                        opacity=1.0 if active_index == 1 else 0.5,
                    ),
                    ft.IconButton(
                        icon=ft.icons.SWAP_HORIZ,
                        icon_color=DARK_BG,
                        icon_size=22,
                        opacity=1.0 if active_index == 2 else 0.5,
                    ),
                    ft.IconButton(
                        icon=ft.icons.ACCOUNT_BALANCE_WALLET,
                        icon_color=DARK_BG,
                        icon_size=22,
                        opacity=1.0 if active_index == 3 else 0.5,
                    ),
                    ft.IconButton(
                        icon=ft.icons.PERSON,
                        icon_color=DARK_BG,
                        icon_size=22,
                        opacity=1.0 if active_index == 4 else 0.5,
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