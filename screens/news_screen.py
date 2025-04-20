import flet as ft
from components.navbar import get_navbar

def get_news_screen(page: ft.Page, on_notification: callable) -> ft.Container:
    # Definindo cores personalizadas
    GOLD = "#FFD700"
    SOFT_GOLD = "#F7D679"
    DARK_BG = "#121212"
    CARD_BG = "#1A1A1A"
    ICON_BG = "#262626"
    TEXT_COLOR = "#FFFFFF"

    def handle_notification(e):
        on_notification()

    def create_news_card(title, description, date):
        return ft.Container(
            content=ft.Column(
                [
                    ft.Text(title, size=16, weight=ft.FontWeight.BOLD, color=SOFT_GOLD),
                    ft.Text(description, size=14, color=TEXT_COLOR, opacity=0.8),
                    ft.Text(date, size=12, color="#666666"),
                ],
                spacing=5,
            ),
            bgcolor=CARD_BG,
            padding=15,
            border_radius=15,
            margin=ft.margin.only(bottom=10),
        )

    # Conteúdo das abas
    general_news = ft.Column(
        [
            create_news_card(
                "Meu pau cresceu 2 cm",
                "rola aumentou",
                "20 de Abril, 2025",
            ),
            create_news_card(
                "cucucuucuc",
                "rolas",
                "20 de Abril, 2025",
            ),
        ],
        scroll=ft.ScrollMode.AUTO,
    )

    stock_news = ft.Column(
        [
            create_news_card(
                "Ibovespa em Alta",
                "O índice Ibovespa subiu 1,8% no pregão de hoje.",
                "20 de Abril, 2025",
            ),
            create_news_card(
                "Ações da Petrobras",
                "As ações da Petrobras valorizaram 3% após anúncio de novos investimentos.",
                "20 de Abril, 2025",
            ),
        ],
        scroll=ft.ScrollMode.AUTO,
    )

    currency_news = ft.Column(
        [
            create_news_card(
                "Dólar em Queda",
                "O dólar caiu 1,5% em relação ao real, fechando a R$ 4,80.",
                "20 de Abril, 2025",
            ),
            create_news_card(
                "Euro Estável",
                "O euro manteve-se estável em relação ao real, cotado a R$ 5,20.",
                "20 de Abril, 2025",
            ),
        ],
        scroll=ft.ScrollMode.AUTO,
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
                                ft.Text(
                                    "Notícias Econômicas",
                                    size=20,
                                    weight=ft.FontWeight.BOLD,
                                    color=SOFT_GOLD,
                                ),
                                ft.IconButton(
                                    icon=ft.icons.NOTIFICATIONS_NONE,
                                    icon_color=SOFT_GOLD,
                                    on_click=handle_notification,
                                ),
                            ],
                            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                        ),
                        ft.Container(height=20),
                        # Abas
                        ft.Tabs(
                            selected_index=0,
                            label_color=TEXT_COLOR,
                            indicator_color=SOFT_GOLD,
                            tabs=[
                                ft.Tab(
                                    text="Notícias Gerais",
                                    content=general_news,
                                    
                                ),
                                ft.Tab(
                                    text="Bolsa",
                                    content=stock_news,
                                    
                                ),
                                ft.Tab(
                                    text="Moedas",
                                    content=currency_news,
                                    
                                ),
                            ],
                            expand=1,
                        ),
                    ],
                    scroll=ft.ScrollMode.AUTO,
                ),
                # Navbar fixa
                get_navbar(page, active_index=3),
            ]
        ),
    )