import flet as ft
from components.navbar import get_navbar

def get_notification_screen(page: ft.Page, on_back: callable) -> ft.Container:
    # Definindo cores personalizadas
    DARK_BG = "#121212"
    SOFT_GOLD = "#F7D679"
    CARD_BG = "#1A1A1A"
    ICON_BG = "#262626"

    def handle_back(e):
        on_back()

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
                                    "Notificações",
                                    size=24,
                                    weight=ft.FontWeight.BOLD,
                                    color=SOFT_GOLD,
                                ),
                                ft.IconButton(
                                    icon=ft.icons.ARROW_BACK,
                                    icon_color=SOFT_GOLD,
                                    on_click=handle_back,
                                ),
                            ],
                            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                        ),
                        
                        ft.Container(height=20),
                        
                        # Lista de Notificações
                        ft.Column(
                            [
                                # Notificação 1
                                ft.Container(
                                    content=ft.Row(
                                        [
                                            ft.Container(
                                                content=ft.Icon(
                                                    ft.icons.ACCOUNT_BALANCE_WALLET,
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
                                                        "Saldo Atualizado",
                                                        size=16,
                                                        weight=ft.FontWeight.W_500,
                                                        color=SOFT_GOLD,
                                                    ),
                                                    ft.Text(
                                                        "Seu saldo foi atualizado com sucesso",
                                                        size=12,
                                                        color="#666666",
                                                    ),
                                                ],
                                                spacing=2,
                                            ),
                                            ft.Container(
                                                content=ft.Text(
                                                    "10:30",
                                                    size=12,
                                                    color="#666666",
                                                ),
                                            ),
                                        ],
                                    ),
                                    bgcolor=CARD_BG,
                                    padding=15,
                                    border_radius=15,
                                    margin=ft.margin.only(bottom=10),
                                ),
                                
                                # Notificação 2
                                ft.Container(
                                    content=ft.Row(
                                        [
                                            ft.Container(
                                                content=ft.Icon(
                                                    ft.icons.ATTACH_MONEY,
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
                                                        "Meta Atingida",
                                                        size=16,
                                                        weight=ft.FontWeight.W_500,
                                                        color=SOFT_GOLD,
                                                    ),
                                                    ft.Text(
                                                        "Parabéns! Você atingiu sua meta de economia",
                                                        size=12,
                                                        color="#666666",
                                                    ),
                                                ],
                                                spacing=2,
                                            ),
                                            ft.Container(
                                                content=ft.Text(
                                                    "Ontem",
                                                    size=12,
                                                    color="#666666",
                                                ),
                                            ),
                                        ],
                                    ),
                                    bgcolor=CARD_BG,
                                    padding=15,
                                    border_radius=15,
                                    margin=ft.margin.only(bottom=10),
                                ),
                                
                                # Notificação 3
                                ft.Container(
                                    content=ft.Row(
                                        [
                                            ft.Container(
                                                content=ft.Icon(
                                                    ft.icons.WARNING,
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
                                                        "Alerta de Gastos",
                                                        size=16,
                                                        weight=ft.FontWeight.W_500,
                                                        color=SOFT_GOLD,
                                                    ),
                                                    ft.Text(
                                                        "Você está próximo do limite de gastos mensais",
                                                        size=12,
                                                        color="#666666",
                                                    ),
                                                ],
                                                spacing=2,
                                            ),
                                            ft.Container(
                                                content=ft.Text(
                                                    "2 dias",
                                                    size=12,
                                                    color="#666666",
                                                ),
                                            ),
                                        ],
                                    ),
                                    bgcolor=CARD_BG,
                                    padding=15,
                                    border_radius=15,
                                ),
                            ],
                            scroll=ft.ScrollMode.AUTO,
                        ),
                    ],
                ),
            ],
        ),
    )
