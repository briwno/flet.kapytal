import flet as ft
from components.navbar import get_navbar
from storage.data.user_data import load_transactions

def get_transaction_screen(page: ft.Page, on_back: callable) -> ft.Container:
    # Definindo cores personalizadas
    DARK_BG = "#121212"
    SOFT_GOLD = "#F7D679"
    CARD_BG = "#1A1A1A"
    ICON_BG = "#262626"
    GREEN = "#00D47E"
    BLUE = "#3E83FF"
    RED = "#FF3E3E"

    def handle_back(e):
        on_back()

    def handle_add_transaction(e):
        page.go("/add")  # Redireciona para a tela de adicionar transações

    # Carregar transações reais
    transactions = load_transactions()

    def create_transaction_item(icon, title, date, category, value, is_expense=False):
        return ft.Container(
            content=ft.Row(
                [
                    ft.Container(
                        content=ft.Icon(
                            icon,
                            color=SOFT_GOLD,
                            size=22,
                        ),
                        bgcolor=ICON_BG,
                        padding=8,
                        border_radius=10,
                    ),
                    ft.Container(width=15),
                    ft.Column(
                        [
                            ft.Text(
                                title,
                                size=16,
                                weight=ft.FontWeight.W_500,
                                color=SOFT_GOLD,
                            ),
                            ft.Text(
                                date,
                                size=12,
                                color="#666666",
                            ),
                        ],
                        spacing=2,
                        expand=True,
                    ),
                    ft.Text(
                        category,
                        size=12,
                        color="#666666",
                    ),
                    ft.Container(width=15),
                    ft.Text(
                        f"{'-' if is_expense else '+'} R$ {abs(value):.2f}",
                        size=16,
                        weight=ft.FontWeight.W_500,
                        color=RED if is_expense else GREEN,
                    ),
                ],
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            ),
            bgcolor=CARD_BG,
            padding=15,
            border_radius=15,
            margin=ft.margin.only(bottom=10),
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
                        ft.Row(
                            [
                                ft.IconButton(
                                    icon=ft.icons.ARROW_BACK,
                                    icon_color=SOFT_GOLD,
                                    on_click=handle_back,
                                ),
                                ft.Text(
                                    "Transações",
                                    size=20,
                                    weight=ft.FontWeight.BOLD,
                                    color=SOFT_GOLD,
                                ),
                                ft.IconButton(
                                    icon=ft.icons.NOTIFICATIONS_NONE,
                                    icon_color=SOFT_GOLD,
                                    icon_size=22,
                                    on_click=lambda _: page.go("/notifications"),
                                ),
                            ],
                            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                        ),
                        ft.Container(height=20),
                        ft.Column(
                            [
                                create_transaction_item(
                                    ft.icons.WORK if t["type"] == "receita" else ft.icons.SHOPPING_BAG,
                                    t["description"],
                                    t["date"],
                                    t["category"],
                                    t["value"],
                                    is_expense=(t["type"] == "despesa"),
                                )
                                for t in transactions
                            ],
                            scroll=ft.ScrollMode.AUTO,
                            spacing=0,
                        ),
                        ft.Container(
                            content=ft.Container(
                                content=ft.IconButton(
                                    icon=ft.icons.ADD,
                                    icon_color=DARK_BG,
                                    icon_size=24,
                                    on_click=handle_add_transaction,
                                ),
                                bgcolor=SOFT_GOLD,
                                shape=ft.BoxShape.CIRCLE,
                                width=50,
                                height=50,
                                alignment=ft.alignment.center,
                            ),
                            margin=ft.margin.only(bottom=80),
                            alignment=ft.alignment.center,
                        ),
                    ],
                    expand=True,
                ),
                # Navbar fixa
                get_navbar(page, active_index=2),
            ],
        ),
    )