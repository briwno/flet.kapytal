import flet as ft
from components.navbar import get_navbar

def get_home_screen(page: ft.Page, on_logout: callable, on_add_transaction: callable) -> ft.Container:
    # Definindo cores personalizadas
    GOLD = "#FFD700"
    SOFT_GOLD = "#F7D679"
    DARK_BG = "#121212"
    CARD_BG = "#1A1A1A"
    ICON_BG = "#262626"
    BLUE = "#3E83FF"

    def handle_logout(e):
        on_logout()

    def handle_add_transaction(e):
        on_add_transaction()

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
                                            "Olá, Bem-vindo de volta",
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
                                            icon=ft.icons.ADD,
                                            icon_color=SOFT_GOLD,
                                            icon_size=22,
                                            on_click=handle_add_transaction,
                                        ),
                                        ft.IconButton(
                                            icon=ft.icons.NOTIFICATIONS_NONE,
                                            icon_color=SOFT_GOLD,
                                            icon_size=22,
                                        ),
                                    ],
                                    spacing=5,
                                ),
                            ],
                            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                        ),
                        
                        ft.Container(height=25),  # Espaçamento ajustado
                        
                        # Saldo e Despesas
                        ft.Row(
                            [
                                ft.Column(
                                    [
                                        ft.Text("Saldo Total", size=14, color=SOFT_GOLD, opacity=0.8),
                                        ft.Text(
                                            "R$ 7.783,00",
                                            size=26,
                                            weight=ft.FontWeight.BOLD,
                                            color=SOFT_GOLD,
                                        ),
                                    ],
                                    spacing=4,
                                ),
                                ft.Column(
                                    [
                                        ft.Text("Despesas Totais", size=14, color=SOFT_GOLD, opacity=0.8),
                                        ft.Text(
                                            "- R$ 1.187,40",
                                            size=26,
                                            weight=ft.FontWeight.BOLD,
                                            color=BLUE,
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
                                        value=0.3,
                                        bgcolor=ICON_BG,
                                        color=SOFT_GOLD,
                                        height=8,
                                        border_radius=4,
                                    ),
                                    ft.Container(height=5),
                                    ft.Text("R$ 20.000,00", color=SOFT_GOLD, size=12, opacity=0.8),
                                    ft.Text(
                                        "30% Das Suas Despesas, Muito Bom!",
                                        color=SOFT_GOLD,
                                        size=14,
                                        weight=ft.FontWeight.W_500,
                                    ),
                                ],
                                spacing=4,
                            ),
                        ),
                        
                        ft.Container(height=20),
                        
                        # Card de Economia e Alimentação
                        ft.Container(
                            bgcolor=CARD_BG,
                            border_radius=15,
                            padding=ft.padding.all(20),
                            content=ft.Column(
                                [
                                    ft.Row(
                                        [
                                            ft.Row(
                                                [
                                                    ft.Container(
                                                        content=ft.Icon(
                                                            ft.icons.DIRECTIONS_CAR,
                                                            color=SOFT_GOLD,
                                                            size=22,
                                                        ),
                                                        bgcolor=ICON_BG,
                                                        padding=8,
                                                        border_radius=10,
                                                    ),
                                                    ft.Container(width=10),
                                                    ft.Column(
                                                        [
                                                            ft.Text(
                                                                "Economia",
                                                                color=SOFT_GOLD,
                                                                size=14,
                                                                weight=ft.FontWeight.W_500,
                                                            ),
                                                            ft.Text(
                                                                "em Metas",
                                                                color=SOFT_GOLD,
                                                                size=14,
                                                                weight=ft.FontWeight.W_500,
                                                                opacity=0.8,
                                                            ),
                                                        ],
                                                        spacing=0,
                                                    ),
                                                ]
                                            ),
                                            ft.Column(
                                                [
                                                    ft.Text(
                                                        "Receita Última Semana",
                                                        color=SOFT_GOLD,
                                                        size=12,
                                                        opacity=0.8,
                                                    ),
                                                    ft.Text(
                                                        "R$ 4.000,00",
                                                        color=SOFT_GOLD,
                                                        size=16,
                                                        weight=ft.FontWeight.BOLD,
                                                    ),
                                                ],
                                                spacing=2,
                                                horizontal_alignment=ft.CrossAxisAlignment.END,
                                            ),
                                        ],
                                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                                    ),
                                    ft.Divider(
                                        color=ICON_BG,
                                        height=30,
                                        thickness=1,
                                    ),
                                    ft.Row(
                                        [
                                            ft.Row(
                                                [
                                                    ft.Container(
                                                        content=ft.Icon(
                                                            ft.icons.RESTAURANT,
                                                            color=SOFT_GOLD,
                                                            size=22,
                                                        ),
                                                        bgcolor=ICON_BG,
                                                        padding=8,
                                                        border_radius=10,
                                                    ),
                                                    ft.Container(width=10),
                                                    ft.Column(
                                                        [
                                                            ft.Text(
                                                                "Alimentação",
                                                                color=SOFT_GOLD,
                                                                size=14,
                                                                weight=ft.FontWeight.W_500,
                                                            ),
                                                            ft.Text(
                                                                "Última Semana",
                                                                color=SOFT_GOLD,
                                                                size=12,
                                                                opacity=0.8,
                                                            ),
                                                        ],
                                                        spacing=0,
                                                    ),
                                                ]
                                            ),
                                            ft.Text(
                                                "-R$ 100,00",
                                                color=SOFT_GOLD,
                                                size=16,
                                                weight=ft.FontWeight.BOLD,
                                            ),
                                        ],
                                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                                    ),
                                ],
                            ),
                        ),
                        
                        ft.Container(height=20),
                        
                        # Botões de Período
                        ft.Row(
                            [
                                ft.TextButton(
                                    "Diário",
                                    style=ft.ButtonStyle(
                                        color="#666666",
                                    ),
                                ),
                                ft.TextButton(
                                    "Semanal",
                                    style=ft.ButtonStyle(
                                        color="#666666",
                                    ),
                                ),
                                ft.Container(
                                    content=ft.Text(
                                        "Mensal",
                                        color=DARK_BG,
                                        weight=ft.FontWeight.W_500,
                                    ),
                                    bgcolor=SOFT_GOLD,
                                    padding=ft.padding.symmetric(horizontal=20, vertical=8),
                                    border_radius=15,
                                ),
                            ],
                            alignment=ft.MainAxisAlignment.SPACE_AROUND,
                        ),
                        
                        ft.Container(height=15),
                        
                        # Lista de Transações
                        ft.Column(
                            [
                                ft.Container(
                                    content=ft.Row(
                                        [
                                            ft.Container(
                                                content=ft.Icon(
                                                    ft.icons.WORK,
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
                                                        "Salário",
                                                        size=16,
                                                        weight=ft.FontWeight.W_500,
                                                        color=SOFT_GOLD,
                                                    ),
                                                    ft.Row(
                                                        [
                                                            ft.Text(
                                                                "18:27 - 30 Abril",
                                                                size=12,
                                                                color="#666666",
                                                            ),
                                                            ft.Container(width=10),
                                                            ft.Text(
                                                                "Mensal",
                                                                size=12,
                                                                color="#666666",
                                                            ),
                                                        ],
                                                    ),
                                                ],
                                                spacing=2,
                                            ),
                                            ft.Container(
                                                expand=True,
                                                content=ft.Text(
                                                    "R$ 4.000,00",
                                                    size=16,
                                                    weight=ft.FontWeight.W_500,
                                                    color=SOFT_GOLD,
                                                    text_align=ft.TextAlign.RIGHT,
                                                ),
                                            ),
                                        ],
                                    ),
                                    margin=ft.margin.only(bottom=15),
                                ),
                                ft.Container(
                                    content=ft.Row(
                                        [
                                            ft.Container(
                                                content=ft.Icon(
                                                    ft.icons.SHOPPING_BAG,
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
                                                        "Mercado",
                                                        size=16,
                                                        weight=ft.FontWeight.W_500,
                                                        color=SOFT_GOLD,
                                                    ),
                                                    ft.Row(
                                                        [
                                                            ft.Text(
                                                                "17:00 - 24 Abril",
                                                                size=12,
                                                                color="#666666",
                                                            ),
                                                            ft.Container(width=10),
                                                            ft.Text(
                                                                "Despensa",
                                                                size=12,
                                                                color="#666666",
                                                            ),
                                                        ],
                                                    ),
                                                ],
                                                spacing=2,
                                            ),
                                            ft.Container(
                                                expand=True,
                                                content=ft.Text(
                                                    "-R$ 100,00",
                                                    size=16,
                                                    weight=ft.FontWeight.W_500,
                                                    color=SOFT_GOLD,
                                                    text_align=ft.TextAlign.RIGHT,
                                                ),
                                            ),
                                        ],
                                    ),
                                    margin=ft.margin.only(bottom=15),
                                ),
                                ft.Container(
                                    content=ft.Row(
                                        [
                                            ft.Container(
                                                content=ft.Icon(
                                                    ft.icons.HOME,
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
                                                        "Aluguel",
                                                        size=16,
                                                        weight=ft.FontWeight.W_500,
                                                        color=SOFT_GOLD,
                                                    ),
                                                    ft.Row(
                                                        [
                                                            ft.Text(
                                                                "8:30 - 15 Abril",
                                                                size=12,
                                                                color="#666666",
                                                            ),
                                                            ft.Container(width=10),
                                                            ft.Text(
                                                                "Moradia",
                                                                size=12,
                                                                color="#666666",
                                                            ),
                                                        ],
                                                    ),
                                                ],
                                                spacing=2,
                                            ),
                                            ft.Container(
                                                expand=True,
                                                content=ft.Text(
                                                    "-R$ 674,40",
                                                    size=16,
                                                    weight=ft.FontWeight.W_500,
                                                    color=SOFT_GOLD,
                                                    text_align=ft.TextAlign.RIGHT,
                                                ),
                                            ),
                                        ],
                                    ),
                                ),
                            ],
                        ),
                    ],
                    scroll=ft.ScrollMode.AUTO,
                ),
                
                # Using the new navbar component
                get_navbar(page, active_index=0),
            ],
        ),
    )
