import flet as ft
import datetime
from collections import defaultdict
import calendar
from components.navbar import get_navbar

def get_analysis_screen(page: ft.Page, on_notification: callable, transactions: list) -> ft.Container:
    # --- Cores e Estilos da UI ---
    GOLD = "#FFD700"
    SOFT_GOLD = "#F7D679"  # Corrigido
    DARK_BG = "#121212"
    CARD_BG = "#1A1A1A"
    ICON_BG = "#262626"
    TEXT_COLOR = "#FFFFFF"
    GREEN = "#00D47E"
    RED = "#FF3E3E"
    BLUE = "#3E83FF"

    # --- Estado e Configuração ---
    current_filter = ["Mês"]

    # --- Funções de construção de componentes ---
    def _build_header():
        """Cria o cabeçalho padrão da tela."""
        return ft.Row(
            [
                ft.IconButton(icon=ft.icons.ARROW_BACK, icon_color=SOFT_GOLD, icon_size=22, on_click=lambda e: page.go("/home")),
                ft.Container(
                    ft.Text("Análise", size=20, weight=ft.FontWeight.BOLD, color=SOFT_GOLD),
                    padding=ft.padding.symmetric(horizontal=16, vertical=30),
                ),
                ft.IconButton(icon=ft.icons.NOTIFICATIONS_NONE, icon_color=SOFT_GOLD, icon_size=22, on_click=lambda e: on_notification()),
            ],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
        )

    # --- Processamento de Dados ---
    def parse_transactions(trans):
        parsed = []
        for t in trans:
            try:
                t['value'] = float(t.get('value', 0))
                t['date'] = datetime.datetime.strptime(t.get('date', ''), '%d/%m/%Y %H:%M')
                parsed.append(t)
            except (ValueError, TypeError):
                print(f"Aviso: Ignorando transação com dados inválidos: {t}")
                continue
        return parsed

    all_transactions = parse_transactions(transactions)

    # --- Componentes da UI ---
    summary_income_text = ft.Text("R$ 0,00", size=18, weight=ft.FontWeight.BOLD, color=GREEN)
    summary_expense_text = ft.Text("R$ 0,00", size=18, weight=ft.FontWeight.BOLD, color=RED)
    summary_balance_text = ft.Text("R$ 0,00", size=18, weight=ft.FontWeight.BOLD, color=BLUE)

    charts_title = ft.Text("Resultados do Mês", size=18, weight=ft.FontWeight.BOLD, color=SOFT_GOLD)
    bar_chart = ft.BarChart(height=220, expand=True)
    pie_chart_container = ft.Row(
        alignment=ft.MainAxisAlignment.CENTER,
        vertical_alignment=ft.CrossAxisAlignment.CENTER,
        height=180,
    )

    # --- Lógica Principal ---
    def update_view(e=None):
        filter_type = current_filter[0]

        now = datetime.datetime.now()
        if filter_type == "Mês":
            start_period = now.replace(day=1, hour=0, minute=0, second=0, microsecond=0)
            _, last_day = calendar.monthrange(now.year, now.month)
            end_period = now.replace(day=last_day, hour=23, minute=59, second=59)
        else:  # Ano
            start_period = now.replace(month=1, day=1, hour=0, minute=0, second=0, microsecond=0)
            end_period = now.replace(month=12, day=31, hour=23, minute=59, second=59)
        
        filtered_transactions = [t for t in all_transactions if start_period <= t['date'] <= end_period]

        total_income = sum(t['value'] for t in filtered_transactions if t['type'] == 'receita')
        total_expense = sum(t['value'] for t in filtered_transactions if t['type'] == 'despesa')
        balance = total_income - total_expense

        summary_income_text.value = f"R$ {total_income:,.2f}"
        summary_expense_text.value = f"R$ {total_expense:,.2f}"
        summary_balance_text.value = f"R$ {balance:,.2f}"
        summary_balance_text.color = BLUE if balance >= 0 else GOLD

        update_bar_chart(filtered_transactions, filter_type)
        update_pie_chart(filtered_transactions)

        charts_title.value = f"Resultados do {filter_type}"
        for btn in filter_buttons.controls:
            is_active = btn.text == filter_type
            btn.style.bgcolor = SOFT_GOLD if is_active else CARD_BG
            btn.style.color = DARK_BG if is_active else TEXT_COLOR
            btn.style.border = ft.border.all(1, ft.colors.WHITE24) if not is_active else None

        page.update()

    def update_bar_chart(data, filter_type):
        income_by_period = defaultdict(float)
        expense_by_period = defaultdict(float)

        if filter_type == "Mês":
            for t in data:
                period = t['date'].day
                if t['type'] == 'receita': income_by_period[period] += t['value']
                else: expense_by_period[period] += t['value']
            now = datetime.datetime.now()
            _, last_day = calendar.monthrange(now.year, now.month)
            all_periods = list(range(1, last_day + 1))
            get_label = lambda p: str(p) if p % 5 == 0 or p == 1 or p == last_day else ""
            labels = [ft.ChartAxisLabel(value=p, label=ft.Text(get_label(p), size=10, color=ft.colors.WHITE54)) for p in all_periods]
        else:  # Ano
            for t in data:
                period = t['date'].month
                if t['type'] == 'receita': income_by_period[period] += t['value']
                else: expense_by_period[period] += t['value']
            all_periods = list(range(1, 13))
            get_label = lambda p: calendar.month_abbr[p][:3]
            labels = [ft.ChartAxisLabel(value=p, label=ft.Text(get_label(p), size=10, color=ft.colors.WHITE54)) for p in all_periods]

        bar_chart.bar_groups = [
            ft.BarChartGroup(x=p, bar_rods=[
                ft.BarChartRod(from_y=0, to_y=income_by_period.get(p, 0), width=5, color=GREEN, tooltip=f"Receita: R${income_by_period.get(p, 0):.2f}"),
                ft.BarChartRod(from_y=0, to_y=expense_by_period.get(p, 0), width=5, color=RED, tooltip=f"Despesa: R${expense_by_period.get(p, 0):.2f}"),
            ]) for p in all_periods
        ]
        bar_chart.bottom_axis = ft.ChartAxis(labels=labels, labels_size=40)
        bar_chart.max_y = max(list(income_by_period.values()) + list(expense_by_period.values()) + [100])

    def update_pie_chart(data):
        expense_by_category = defaultdict(float)
        expenses = [t for t in data if t['type'] == 'despesa']
        total_expense = sum(t['value'] for t in expenses)

        pie_chart_container.controls.clear()

        if not expenses:
            pie_chart_container.controls.append(ft.Text("Sem despesas no período", color=SOFT_GOLD, text_align=ft.TextAlign.CENTER))
            return

        for t in expenses:
            expense_by_category[t.get('category', 'Outros')] += t['value']
        
        colors = ["#FF6B6B", "#FFD166", "#06D6A0", "#118AB2", "#073B4C", "#EE6C4D", "#293241"]
        pie_sections = [
            ft.PieChartSection(
                value=(amount / total_expense) * 100 if total_expense else 0,
                title=f"{(amount / total_expense) * 100:.0f}%",
                title_style=ft.TextStyle(size=10, color=ft.colors.BLACK, weight=ft.FontWeight.BOLD),
                color=colors[i % len(colors)],
                radius=55,
            ) for i, (category, amount) in enumerate(expense_by_category.items())
        ]
        legend_items = [
            ft.Row([
                ft.Container(width=12, height=12, bgcolor=colors[i % len(colors)], border_radius=6),
                ft.Text(f"{cat} ({(amt / total_expense) * 100:.0f}%)", color=TEXT_COLOR, size=11)
            ], spacing=8) for i, (cat, amt) in enumerate(expense_by_category.items())
        ]
        legend = ft.Column(controls=legend_items, spacing=4, alignment=ft.MainAxisAlignment.CENTER)

        pie_chart = ft.PieChart(sections=pie_sections, sections_space=1, center_space_radius=30, expand=True)
        
        pie_chart_container.controls.extend([
            ft.Column([pie_chart], expand=1, horizontal_alignment=ft.CrossAxisAlignment.CENTER),
            ft.Column([legend], expand=1, horizontal_alignment=ft.CrossAxisAlignment.START),
        ])

    # --- Handlers de Eventos ---
    def handle_filter_change(e):
        current_filter[0] = e.control.text
        update_view()

    # --- Layout da UI ---
    month_button = ft.TextButton("Mês", on_click=handle_filter_change, style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=8)))
    year_button = ft.TextButton("Ano", on_click=handle_filter_change, style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=8)))
    filter_buttons = ft.Row([month_button, year_button], alignment=ft.MainAxisAlignment.CENTER)
    
    update_view()

    return ft.Container(
        width=400, height=830, bgcolor=DARK_BG, border_radius=35,
        padding=ft.padding.only(left=20, right=20, top=15, bottom=5),
        content=ft.Stack([
            ft.Column([
                _build_header(),
                ft.Container(height=10),
                filter_buttons,
                ft.Container(height=10),
                ft.Container(
                    padding=ft.padding.symmetric(vertical=15, horizontal=20), bgcolor=CARD_BG, border_radius=15,
                    content=ft.Row([
                        ft.Column([ft.Text("Receitas", color=TEXT_COLOR, size=12), summary_income_text], horizontal_alignment=ft.CrossAxisAlignment.CENTER, expand=True),
                        ft.Column([ft.Text("Despesas", color=TEXT_COLOR, size=12), summary_expense_text], horizontal_alignment=ft.CrossAxisAlignment.CENTER, expand=True),
                        ft.Column([ft.Text("Saldo", color=TEXT_COLOR, size=12), summary_balance_text], horizontal_alignment=ft.CrossAxisAlignment.CENTER, expand=True),
                    ], alignment=ft.MainAxisAlignment.SPACE_AROUND)
                ),
                ft.Container(height=15),
                ft.Container(
                    padding=15, bgcolor=CARD_BG, border_radius=15, expand=True,
                    content=ft.Column([
                        charts_title,
                        ft.Text("Comparativo de receitas e despesas", size=12, color=ft.colors.WHITE54),
                        bar_chart,
                        ft.Divider(height=15, color=ft.colors.WHITE24),
                        ft.Text("Distribuição de Despesas por Categoria", size=14, weight=ft.FontWeight.BOLD, color=SOFT_GOLD),
                        pie_chart_container,
                    ], spacing=5, horizontal_alignment=ft.CrossAxisAlignment.CENTER)
                ),
                ft.Container(height=80),
            ], scroll=ft.ScrollMode.HIDDEN, expand=True),
            get_navbar(page, active_index=1),
        ]),
    )