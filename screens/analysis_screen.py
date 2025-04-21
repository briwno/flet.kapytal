import flet as ft
from components.navbar import get_navbar

def get_analysis_screen(page: ft.Page, on_notification: callable) -> ft.Container:
    # Definindo cores personalizadas
    GOLD = "#FFD700"
    SOFT_GOLD = "#F7D679"
    DARK_BG = "#121212"
    CARD_BG = "#1A1A1A"
    ICON_BG = "#262626"
    TEXT_COLOR = "#FFFFFF"
    BLUE = "#3E83FF"

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
                        
                        ft.Row(
                            [
                                ft.TextButton(
                                    "Diario",
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
                                ft.TextButton(
                                    "Mensal",
                                    style=ft.ButtonStyle(
                                        color="#666666",
                                    ),
                                ),
                                ft.TextButton(
                                    "Anual",
                                    style=ft.ButtonStyle(
                                        color="#666666",
                                        
                                    ),
                                ),
                            ],
                            alignment=ft.MainAxisAlignment.SPACE_AROUND,
                        ),
                        ft.Container(height=15),
                        
                        # Gráfico de Barras
                        ft.BarChart(
                            bar_groups=[
                                ft.BarChartGroup(
                                    x=0,
                                    bar_rods=[
                                        ft.BarChartRod(
                                            from_y=0,
                                            to_y=2000,  # Substituir 'y' por 'to_y'
                                            width=40,
                                            color=SOFT_GOLD,
                                            tooltip="Janeiro",
                                        ),
                                    ],
                                ),
                                ft.BarChartGroup(
                                    x=1,
                                    bar_rods=[
                                        ft.BarChartRod(
                                            from_y=0,
                                            to_y=3000,  # Substituir 'y' por 'to_y'
                                            width=40,
                                            color=SOFT_GOLD,
                                            tooltip="Fevereiro",
                                        ),
                                    ],
                                ),
                            ],
                            max_y=3500,
                            height=200,
                            width=350,
                        ),
                    ],
                ),
                get_navbar(page, active_index=1),
            ]
        ),
    )