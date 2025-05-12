import flet as ft
from components.navbar import get_navbar
import datetime

def get_analysis_screen(page: ft.Page, on_notification: callable, transactions: list) -> ft.Container:
    # Definindo cores personalizadas
    GOLD = "#FFD700"
    SOFT_GOLD = "#F7D679"
    DARK_BG = "#121212"
    CARD_BG = "#1A1A1A"
    ICON_BG = "#262626"
    TEXT_COLOR = "#FFFFFF"
    BLUE = "#3E83FF"
    GREEN = "#00FF00"
    RED = "#FF3E3E"
    
    #calculos
    total_income = sum(t["value"] for t in transactions if t["type"] == "receita")
    total_expense = sum(t["value"] for t in transactions if t["type"] == "despesa")
    balance = total_income - total_expense
    percent_expense = (total_expense / (total_income + total_expense)) if (total_income + total_expense) > 0 else 0
    
    # Dias da semana em português
    dias_semana = ["Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado", "Domingo"]

    # Inicializa os valores
    receitas_por_dia = [0] * 7
    despesas_por_dia = [0] * 7

    for t in transactions:
        try:
            data = datetime.datetime.strptime(t["date"], "%d/%m/%Y")
            idx = (data.weekday())  # 0=Segunda, 6=Domingo
            if t["type"] == "receita":
                receitas_por_dia[idx] += t["value"]
            elif t["type"] == "despesa":
                despesas_por_dia[idx] += t["value"]
        except Exception:
            pass  # Ignora datas inválidas

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
                                            f"R$ {total_income - total_expense:.2f}",
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
                                            f"R$ {total_expense:.2f}",
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
                                        f"{(total_expense / (total_income + total_expense) * 100):.0f}% Das Suas Despesas"
                                        
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
                                                x=i,
                                                bar_rods=[
                                                    ft.BarChartRod(
                                                        from_y=0,
                                                        to_y=receitas_por_dia[i],
                                                        width=20,
                                                        color=GREEN,
                                                        tooltip=f"Receitas - {dias_semana[i]}",
                                                    ),
                                                    ft.BarChartRod(
                                                        from_y=0,
                                                        to_y=despesas_por_dia[i],
                                                        width=20,
                                                        color=RED,
                                                        tooltip=f"Despesas - {dias_semana[i]}",
                                                    ),
                                                ],
                                            )
                                            for i in range(7)
                                        ],
                                        max_y=max(receitas_por_dia + despesas_por_dia + [1]),  # Evita max_y=0
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
                    scroll=ft.ScrollMode.AUTO,
                ),
                get_navbar(page, active_index=1),
            ]
        ),
    )