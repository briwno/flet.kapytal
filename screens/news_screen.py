import flet as ft
from components.navbar import get_navbar
from api.api_code import get_brazil_news, get_currency_rates
from datetime import date, timedelta
import re
from html import unescape  # Para decodificar entidades HTML

def get_news_screen(page: ft.Page, on_notification: callable, news_data, currency_data) -> ft.Container:
    # Definindo cores personalizadas
    GOLD = "#FFD700"
    SOFT_GOLD = "#F7D679"
    DARK_BG = "#121212"
    CARD_BG = "#1A1A1A"
    ICON_BG = "#262626"
    TEXT_COLOR = "#FFFFFF"

    def handle_notification(e):
        on_notification()

    def create_news_card(title, description, date, link=None):
        return ft.Container(
            content=ft.Column(
                [
                    ft.Text(title, size=16, weight=ft.FontWeight.BOLD, color=SOFT_GOLD),
                    ft.Text(description, size=14, color=TEXT_COLOR, opacity=0.8),
                    ft.Text(date, size=12, color="#666666"),
                    ft.TextButton(
                        "Leia mais",
                        on_click=lambda e: page.launch_url(link) if link else None,
                        icon=ft.icons.LINK,
                        visible=link is not None,
                    ),
                ],
                spacing=5,
            ),
            bgcolor=CARD_BG,
            padding=15,
            border_radius=15,
            margin=ft.margin.only(bottom=10),
        )

    # Criando os cards de notícias
    general_news = ft.Column(
        [
            create_news_card(
                title=item.get('title', 'Título não disponível'),
                description=item.get('description', 'Conteúdo não disponível'),
                date=item.get('publishedAt', 'Data não disponível'),
                link=item.get('url', '#'),
            )
            for item in news_data
        ],
        scroll=ft.ScrollMode.AUTO,
    )

    # Criando os cards de cotações de moedas
    if isinstance(currency_data, dict) and "error" not in currency_data:
        print(currency_data)
        currency_news = ft.Column(
            [
                create_news_card(
                    "Cotação do Dólar (USD)",
                    f"Compra: R$ {currency_data['USD']['compra']:.2f}, Venda: R$ {currency_data['USD']['venda']:.2f}",
                    currency_data['USD']['data'],
                ),
                create_news_card(
                    "Cotação do Euro (EUR)",
                    f"Compra: R$ {currency_data['EUR']['compra']:.2f}, Venda: R$ {currency_data['EUR']['venda']:.2f}",
                    currency_data['EUR']['data'],
                ),
                create_news_card(
                    "Cotação do Bitcoin (BTC)",
                    f"Compra: R$ {currency_data['BTC']['compra']:.2f}, Venda: R$ {currency_data['BTC']['venda']:.2f}",
                    currency_data['BTC']['data'],
                ),
            ],
            scroll=ft.ScrollMode.AUTO,
        )
    else:
        currency_news = ft.Column(
            [
                create_news_card(
                    "Erro ao buscar cotações",
                    currency_data.get("error", "Formato de dados inválido") if isinstance(currency_data, dict) else "Dados indisponíveis",
                    "N/A",
                )
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