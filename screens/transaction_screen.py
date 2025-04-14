import flet as ft
from datetime import datetime
from components.navbar import get_navbar

def get_transaction_screen(page: ft.Page, on_back: callable) -> ft.Container:
    # Definindo cores personalizadas
    DARK_BG = "#121212"
    SOFT_GOLD = "#F7D679"
    CARD_BG = "#1A1A1A"
    ICON_BG = "#262626"
    GREEN = "#00D47E"
    BLUE = "#3E83FF"

    # Estado inicial
    current_month = "Abril"
    total_balance = 7783.00
    total_income = 4120.00
    total_expense = 1187.40

    def handle_back(e):
        on_back()
        
    def handle_add_transaction(e):
        page.go("/add")

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
                        color=BLUE if is_expense else GREEN,
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
                        
                        # Cabeçalho com botão de voltar
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
                        
                        # Card de Saldo Total
                        ft.Container(
                            content=ft.Column(
                                [
                                    ft.Text(
                                        "Saldo Total",
                                        size=14,
                                        color=SOFT_GOLD,
                                        text_align=ft.TextAlign.CENTER,
                                    ),
                                    ft.Text(
                                        f"R$ {total_balance:.2f}",
                                        size=24,
                                        weight=ft.FontWeight.BOLD,
                                        color=SOFT_GOLD,
                                        text_align=ft.TextAlign.CENTER,
                                    ),
                                ],
                                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                spacing=5,
                            ),
                            bgcolor=CARD_BG,
                            padding=ft.padding.all(20),
                            border_radius=15,
                            width=400,
                        ),
                        
                        ft.Container(height=20),
                        
                        # Cards de Receita e Despesa
                        ft.Row(
                            [
                                ft.Container(
                                    content=ft.Column(
                                        [
                                            ft.Row(
                                                [
                                                    ft.Icon(
                                                        ft.icons.ARROW_UPWARD,
                                                        color=GREEN,
                                                        size=20,
                                                    ),
                                                    ft.Text(
                                                        "Receitas",
                                                        color=SOFT_GOLD,
                                                        size=14,
                                                    ),
                                                ],
                                                spacing=5,
                                            ),
                                            ft.Text(
                                                f"R$ {total_income:.2f}",
                                                size=18,
                                                weight=ft.FontWeight.BOLD,
                                                color=GREEN,
                                            ),
                                        ],
                                        spacing=5,
                                    ),
                                    bgcolor=CARD_BG,
                                    padding=15,
                                    border_radius=15,
                                    expand=True,
                                ),
                                ft.Container(width=10),
                                ft.Container(
                                    content=ft.Column(
                                        [
                                            ft.Row(
                                                [
                                                    ft.Icon(
                                                        ft.icons.ARROW_DOWNWARD,
                                                        color=BLUE,
                                                        size=20,
                                                    ),
                                                    ft.Text(
                                                        "Despesas",
                                                        color=SOFT_GOLD,
                                                        size=14,
                                                    ),
                                                ],
                                                spacing=5,
                                            ),
                                            ft.Text(
                                                f"R$ {total_expense:.2f}",
                                                size=18,
                                                weight=ft.FontWeight.BOLD,
                                                color=BLUE,
                                            ),
                                        ],
                                        spacing=5,
                                    ),
                                    bgcolor=CARD_BG,
                                    padding=15,
                                    border_radius=15,
                                    expand=True,
                                ),
                            ],
                        ),
                        
                        ft.Container(height=20),
                        
                        # Mês atual
                        ft.Row(
                            [
                                ft.Text(
                                    current_month,
                                    size=20,
                                    weight=ft.FontWeight.BOLD,
                                    color=SOFT_GOLD,
                                ),
                                ft.IconButton(
                                    icon=ft.icons.CALENDAR_TODAY,
                                    icon_color=SOFT_GOLD,
                                    icon_size=20,
                                ),
                            ],
                            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                        ),
                        
                        ft.Container(height=10),
                        
                        # Lista de Transações
                        ft.Column(
                            [
                                create_transaction_item(
                                    ft.icons.WORK,
                                    "Salário",
                                    "18:27 - 30 Abril",
                                    "Mensal",
                                    4000.00,
                                    is_expense=False
                                ),
                                create_transaction_item(
                                    ft.icons.SHOPPING_BAG,
                                    "Mercado",
                                    "17:00 - 24 Abril",
                                    "Alimentação",
                                    100.00,
                                    is_expense=True
                                ),
                                create_transaction_item(
                                    ft.icons.HOME,
                                    "Aluguel",
                                    "8:30 - 15 Abril",
                                    "Moradia",
                                    674.40,
                                    is_expense=True
                                ),
                                create_transaction_item(
                                    ft.icons.DIRECTIONS_BUS,
                                    "Transporte",
                                    "7:30 - 08 Abril",
                                    "Combustível",
                                    4.13,
                                    is_expense=True
                                ),
                                create_transaction_item(
                                    ft.icons.RESTAURANT,
                                    "Alimentação",
                                    "19:30 - 31 Março",
                                    "Jantar",
                                    70.40,
                                    is_expense=True
                                ),
                            ],
                            scroll=ft.ScrollMode.AUTO,
                            spacing=0,
                        ),
                    ],
                    scroll=ft.ScrollMode.AUTO,
                ),
                
                # Botão Flutuante de Adicionar
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
                
                # Navbar
                get_navbar(page, active_index=2),
            ],
        ),
    ) 