import flet as ft

from components.navbar import get_navbar


def get_news_screen(page: ft.Page, on_notification: callable) -> ft.Container:
    
    GOLD = "#FFD700"
    SOFT_GOLD = "#F7D679"
    DARK_BG = "#121212"
    CARD_BG = "#1A1A1A"
    ICON_BG = "#262626"
    BLUE = "#3E83FF"
    print(f"Colors defined: GOLD={GOLD}, SOFT_GOLD={SOFT_GOLD}, DARK_BG={DARK_BG}, CARD_BG={CARD_BG}, ICON_BG={ICON_BG}, BLUE={BLUE}")  # Added usage of color variables
    BLUE = "#3E83FF"
    def handle_notification(e):
        on_notification()
        print(f"Notification handled with event: {e}")  # Added usage of 'e'
    def handle_notification(e):
        on_notification() 
        
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
                        ft.Container(height=45),
                        ft.Row(
                            [
                                ft.TextButton(
                                    "Notícias",
                                    style=ft.ButtonStyle(
                                        color="#666666",
                                    )
                                ),
                                ft.TextButton(
                                    "Moedas",
                                    style=ft.ButtonStyle(
                                        color="#666666",
                                    )
                                ),
                                ft.TextButton(
                                    "Bolsa",
                                    style=ft.ButtonStyle(
                                        color="#666666",
                                    )
                                ),
                            ],
                            alignment=ft.MainAxisAlignment.SPACE_AROUND,
                        )
                    ]
                ),
                get_navbar(page, active_index=5),
            ]
        )
    )