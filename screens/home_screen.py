import flet as ft
from components.navbar import get_navbar
from storage.data.user_data import load_transactions

def get_home_screen(page: ft.Page, on_logout: callable, on_notification: callable, user_name: str, transactions: list) -> ft.Container:
    # Definindo cores personalizadas
    GOLD = "#FFD700"
    SOFT_GOLD = "#F7D679"
    DARK_BG = "#121212"
    CARD_BG = "#1A1A1A"
    ICON_BG = "#262626"
    BLUE = "#3E83FF"
    RED = "#FF3E3E"

    def handle_logout(e):
        on_logout()
        
    def handle_notification(e):
        on_notification()

    def create_transaction_item(transaction):
        return ft.Container(
            content=ft.Row(
                [
                    ft.Container(
                        content=ft.Icon(
                            ft.icons.WORK if transaction["type"] == "receita" else ft.icons.SHOPPING_BAG,
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
                                transaction["description"],
                                size=16,
                                weight=ft.FontWeight.W_500,
                                color=SOFT_GOLD,
                            ),
                            ft.Text(
                                transaction["date"],
                                size=12,
                                color="#666666",
                            ),
                        ],
                        spacing=2,
                        expand=True,
                    ),
                    ft.Text(
                        f"{'-' if transaction['type'] == 'despesa' else '+'} R$ {transaction['value']:.2f}",
                        size=16,
                        weight=ft.FontWeight.W_500,
                        color=RED if transaction["type"] == "despesa" else BLUE,
                    ),
                ],
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            ),
            bgcolor=CARD_BG,
            padding=15,
            border_radius=15,
            margin=ft.margin.only(bottom=10),
        )

    # Calcular resumo
    total_income = sum(t["value"] for t in transactions if t["type"] == "receita")
    total_expense = sum(t["value"] for t in transactions if t["type"] == "despesa")
    balance = total_income - total_expense
    
    opnion = "Você está indo muito bem!" if total_expense < total_income else "Cuidado com seus gastos!"
    

    # Lista de transações
    transaction_list = ft.Column(
        [create_transaction_item(t) for t in transactions],
        spacing=10,
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
                                ft.Column(
                                    [
                                        ft.Text(
                                            f"Olá, Bem-vindo de volta {user_name}!",
                                            size=20,
                                            weight=ft.FontWeight.BOLD,
                                            color=SOFT_GOLD,
                                        ),
                                        ft.Text(
                                            "Bom dia",
                                            size=14,
                                            color=SOFT_GOLD,
                                            opacity=0.8,
                                        ),
                                    ],
                                    spacing=2,
                                ),
                                ft.Row(
                                    [
                                        ft.IconButton(
                                            icon=ft.icons.NOTIFICATIONS_NONE,
                                            icon_color=SOFT_GOLD,
                                            icon_size=22,
                                            on_click=handle_notification,
                                        ),
                                    ],
                                    spacing=5,
                                ),
                            ],
                            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                        ),
                        ft.Container(height=25),
                        
                        # Saldo e Despesas
                        ft.Row(
                            [
                                ft.Column(
                                    [
                                        ft.Text("Saldo Total", size=14, color=SOFT_GOLD, opacity=0.8),
                                        ft.Text(
                                            f"R$ {balance:.2f}",
                                            size=26,
                                            weight=ft.FontWeight.BOLD,
                                            color=SOFT_GOLD if balance >= 0 else RED,                                    ),
                                    ],
                                    spacing=4,
                                ),
                                ft.Column(
                                    [
                                        ft.Text("Despesas Totais", size=14, color=SOFT_GOLD, opacity=0.8),
                                        ft.Text(
                                            f"- R$ {total_expense:.2f}",
                                            size=26,
                                            weight=ft.FontWeight.BOLD,
                                            color=RED,
                                        ),
                                    ],
                                    spacing=4,
                                ),
                            ],
                            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                        ),
                        
                        ft.Container(height=20),
                        
                        # Barra de Progresso
                        ft.Container(
                            content=ft.Column(
                                [
                                    ft.ProgressBar(
                                        value=(total_expense / (total_income + total_expense)) if (total_income + total_expense) > 0 else 0,
                                        bgcolor=ICON_BG,
                                        color=SOFT_GOLD,
                                        height=8,
                                        border_radius=4,
                                    ),
                                    ft.Container(height=5),
                                    ft.Text(f"R$ {total_income + total_expense:.2f}", color=SOFT_GOLD, size=12, opacity=0.8),
                                    ft.Text(
                                        f"{(total_expense / (total_income + total_expense) * 100):.0f}% Das Suas Despesas, {opnion}"
                                        
                                        if (total_income + total_expense) > 0 else "Sem dados suficientes",
                                        color=SOFT_GOLD,
                                        size=14,
                                        weight=ft.FontWeight.W_500,
                                    ),
                                ],
                                spacing=4,
                            ),
                        ),
                        
                        ft.Container(height=20),
                        
                        # Lista de transações
                        transaction_list,
                    ],
                    scroll=ft.ScrollMode.AUTO,
                    expand=True,
                    alignment=ft.MainAxisAlignment.START,
                ),
                # Navbar fixa
                get_navbar(page, active_index=0),
            ],
        ),
    )
