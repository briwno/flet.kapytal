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
    GREEN = "#00FF00"

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
                                ft.IconButton(
                                    icon=ft.icons.ARROW_BACK,
                                    icon_color=SOFT_GOLD,
                                    icon_size=22,
                                ),
                                ft.Text(
                                    "Análise",
                                    size=20,
                                    weight=ft.FontWeight.BOLD,
                                    color=SOFT_GOLD,
                                ),
                                ft.IconButton(
                                    icon=ft.icons.NOTIFICATIONS_NONE,
                                    icon_color=SOFT_GOLD,
                                    icon_size=22,
                                    on_click=handle_notification,
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
                                    ft.Row(
                                        [
                                            ft.Text("R$ 20.000,00", color=SOFT_GOLD, size=12, opacity=0.8),
                                            ft.Text(
                                                "30% das suas despesas, muito bom!",
                                                color=SOFT_GOLD,
                                                size=14,
                                                weight=ft.FontWeight.W_500,
                                            ),
                                        ],
                                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                                    ),
                                ],
                                spacing=4,
                            ),
                        ),
                        
                        ft.Container(height=20),
                        
                        # Botões de Filtro
                        ft.Container(
                            bgcolor=CARD_BG,
                            border_radius=ft.border_radius.all(12),
                            padding=ft.padding.all(10),
                            content=ft.Row(
                                [
                                    ft.TextButton(
                                        "Diário",
                                        style=ft.ButtonStyle(
                                            color=TEXT_COLOR,
                                            bgcolor=SOFT_GOLD,
                                            shape=ft.RoundedRectangleBorder(radius=8),
                                        ),
                                    ),
                                    ft.TextButton(
                                        "Semanal",
                                        style=ft.ButtonStyle(
                                            color="#666666",
                                            shape=ft.RoundedRectangleBorder(radius=8),
                                        ),
                                    ),
                                    ft.TextButton(
                                        "Mensal",
                                        style=ft.ButtonStyle(
                                            color="#666666",
                                            shape=ft.RoundedRectangleBorder(radius=8),
                                        ),
                                    ),
                                    ft.TextButton(
                                        "Anual",
                                        style=ft.ButtonStyle(
                                            color="#666666",
                                            shape=ft.RoundedRectangleBorder(radius=8),
                                        ),
                                    ),
                                ],
                                alignment=ft.MainAxisAlignment.SPACE_AROUND,
                            ),
                        ),
                        
                        ft.Container(height=15),
                        
                        # Gráfico de Barras
                        ft.Container(
                            bgcolor=CARD_BG,
                            border_radius=ft.border_radius.all(12),
                            padding=ft.padding.all(15),
                            content=ft.Column(
                                [
                                    ft.Row(
                                        [
                                            ft.Text(
                                                "Receitas e Despesas",
                                                size=16,
                                                weight=ft.FontWeight.BOLD,
                                                color=SOFT_GOLD,
                                            ),
                                            ft.IconButton(
                                                icon=ft.icons.SEARCH,
                                                icon_color=SOFT_GOLD,
                                                icon_size=20,
                                            ),
                                            ft.IconButton(
                                                icon=ft.icons.CALENDAR_TODAY,
                                                icon_color=SOFT_GOLD,
                                                icon_size=20,
                                            ),
                                        ],
                                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                                    ),
                                    ft.BarChart(
                                        bar_groups=[
                                            ft.BarChartGroup(
                                                x=0,
                                                bar_rods=[
                                                    ft.BarChartRod(
                                                        from_y=0,
                                                        to_y=4000,
                                                        width=20,
                                                        color=GREEN,
                                                        tooltip="Receitas - Segunda",
                                                    ),
                                                    ft.BarChartRod(
                                                        from_y=0,
                                                        to_y=2000,
                                                        width=20,
                                                        color=BLUE,
                                                        tooltip="Despesas - Segunda",
                                                    ),
                                                ],
                                            ),
                                            ft.BarChartGroup(
                                                x=1,
                                                bar_rods=[
                                                    ft.BarChartRod(
                                                        from_y=0,
                                                        to_y=3000,
                                                        width=20,
                                                        color=GREEN,
                                                        tooltip="Receitas - Terça",
                                                    ),
                                                    ft.BarChartRod(
                                                        from_y=0,
                                                        to_y=1500,
                                                        width=20,
                                                        color=BLUE,
                                                        tooltip="Despesas - Terça",
                                                    ),
                                                ],
                                            ),
                                            ft.BarChartGroup(
                                                x=2,
                                                bar_rods=[
                                                    ft.BarChartRod(
                                                        from_y=0,
                                                        to_y=5000,
                                                        width=20,
                                                        color=GREEN,
                                                        tooltip="Receitas - Quarta",
                                                    ),
                                                    ft.BarChartRod(
                                                        from_y=0,
                                                        to_y=2500,
                                                        width=20,
                                                        color=BLUE,
                                                        tooltip="Despesas - Quarta",
                                                    ),
                                                ],
                                            ),
                                            ft.BarChartGroup(
                                                x=3,
                                                bar_rods=[
                                                    ft.BarChartRod(
                                                        from_y=0,
                                                        to_y=4500,
                                                        width=20,
                                                        color=GREEN,
                                                        tooltip="Receitas - Quinta",
                                                    ),
                                                    ft.BarChartRod(
                                                        from_y=0,
                                                        to_y=3000,
                                                        width=20,
                                                        color=BLUE,
                                                        tooltip="Despesas - Quinta",
                                                    ),
                                                ],
                                            ),
                                            ft.BarChartGroup(
                                                x=4,
                                                bar_rods=[
                                                    ft.BarChartRod(
                                                        from_y=0,
                                                        to_y=6000,
                                                        width=20,
                                                        color=GREEN,
                                                        tooltip="Receitas - Sexta",
                                                    ),
                                                    ft.BarChartRod(
                                                        from_y=0,
                                                        to_y=3500,
                                                        width=20,
                                                        color=BLUE,
                                                        tooltip="Despesas - Sexta",
                                                    ),
                                                ],
                                            ),
                                            ft.BarChartGroup(
                                                x=5,
                                                bar_rods=[
                                                    ft.BarChartRod(
                                                        from_y=0,
                                                        to_y=2000,
                                                        width=20,
                                                        color=GREEN,
                                                        tooltip="Receitas - Sábado",
                                                    ),
                                                    ft.BarChartRod(
                                                        from_y=0,
                                                        to_y=1000,
                                                        width=20,
                                                        color=BLUE,
                                                        tooltip="Despesas - Sábado",
                                                    ),
                                                ],
                                            ),
                                            ft.BarChartGroup(
                                                x=6,
                                                bar_rods=[
                                                    ft.BarChartRod(
                                                        from_y=0,
                                                        to_y=3000,
                                                        width=20,
                                                        color=GREEN,
                                                        tooltip="Receitas - Domingo",
                                                    ),
                                                    ft.BarChartRod(
                                                        from_y=0,
                                                        to_y=1500,
                                                        width=20,
                                                        color=BLUE,
                                                        tooltip="Despesas - Domingo",
                                                    ),
                                                ],
                                            ),
                                        ],
                                        max_y=7000,
                                        height=200,
                                        width=350,
                                    ),
                                ],
                            ),
                        ),
                        
                        ft.Container(height=20),
                        
                        # Metas
                        ft.Text(
                            "Minhas Metas",
                            size=16,
                            weight=ft.FontWeight.BOLD,
                            color=SOFT_GOLD,
                        ),
                    ],
                ),
                get_navbar(page, active_index=1),
            ]
        ),
    )