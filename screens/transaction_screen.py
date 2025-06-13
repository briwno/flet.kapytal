import flet as ft
from components.navbar import get_navbar
from storage.data.user_data import load_transactions, load_recurring_transactions, deactivate_recurring_transaction

def get_transaction_screen(page: ft.Page, on_back: callable, user_id: str) -> ft.Container:
    """
    Cria a tela que exibe o histórico de transações e as transações recorrentes ativas.
    """
    transactions = load_transactions(user_id)
    recurring_transactions = load_recurring_transactions(user_id)

    # --- Cores e Estilos ---
    DARK_BG = "#121212"
    SOFT_GOLD = "#F7D679"
    CARD_BG = "#1A1A1A"
    ICON_BG = "#262626"
    GREEN = "#00D47E"
    RED = "#FF3E3E"

    # --- Handlers de Eventos ---
    def handle_back(e):
        on_back()

    def handle_add_transaction(e):
        page.go("/add_transaction")

    def handle_deactivate_recurring(item_id: int):
        """
        Lida com a desativação de uma transação recorrente e atualiza a tela.
        """
        success, message = deactivate_recurring_transaction(item_id)
        if success:
            # Recarrega a tela para refletir a mudança
            page.go("/transactions")
        else:
            page.snack_bar = ft.SnackBar(
                content=ft.Text(f"Erro ao desativar: {message}"),
                bgcolor=ft.colors.RED
            )
            page.snack_bar.open = True
            page.update()

    # --- Componentes de Item ---
    def create_transaction_item(icon, title, date, category, value, is_expense=False):
        return ft.Container(
            content=ft.Row(
                [
                    ft.Container(
                        content=ft.Icon(icon, color=SOFT_GOLD, size=22),
                        bgcolor=ICON_BG, padding=8, border_radius=10,
                    ),
                    ft.Container(width=15),
                    ft.Column(
                        [
                            ft.Text(title, size=16, weight=ft.FontWeight.W_500, color=SOFT_GOLD),
                            ft.Text(date, size=12, color="#666666"),
                        ],
                        spacing=2, expand=True,
                    ),
                    ft.Text(category, size=12, color="#666666"),
                    ft.Container(width=15),
                    ft.Text(f"{'-' if is_expense else '+'} R$ {abs(value):.2f}", size=16, weight=ft.FontWeight.W_500, color=RED if is_expense else GREEN),
                ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            ),
            bgcolor=CARD_BG, padding=15, border_radius=15, margin=ft.margin.only(bottom=10),
        )

    def create_recurring_transaction_item(item_id, icon, title, frequency, value, is_expense=False):
        return ft.Container(
            content=ft.Row(
                [
                    ft.Container(content=ft.Icon(icon, color=SOFT_GOLD, size=22), bgcolor=ICON_BG, padding=8, border_radius=10),
                    ft.Container(width=15),
                    ft.Column(
                        [
                            ft.Text(title, size=16, weight=ft.FontWeight.W_500, color=SOFT_GOLD),
                            ft.Text(f"Frequência: {frequency.capitalize()}", size=12, color="#666666"),
                        ],
                        spacing=2, expand=True,
                    ),
                    ft.Text(f"{'-' if is_expense else '+'} R$ {abs(value):.2f}", size=16, weight=ft.FontWeight.W_500, color=RED if is_expense else GREEN),
                    ft.IconButton(icon=ft.icons.CANCEL_OUTLINED, icon_color=RED, on_click=lambda e: handle_deactivate_recurring(item_id), tooltip="Desativar recorrência"),
                ],
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            ),
            bgcolor=CARD_BG, padding=15, border_radius=15, margin=ft.margin.only(bottom=10),
        )

    # --- Lógica de Conteúdo ---
    list_content = []
    if recurring_transactions:
        list_content.append(ft.Text("Transações Recorrentes", size=18, weight=ft.FontWeight.BOLD, color=SOFT_GOLD))
        for r in recurring_transactions:
            list_content.append(create_recurring_transaction_item(r["id"], ft.icons.AUTORENEW, r["description"], r["frequency"], float(r["value"]), is_expense=(r["type"] == "despesa")))

    if transactions:
        list_content.append(ft.Text("Histórico de Transações", size=18, weight=ft.FontWeight.BOLD, color=SOFT_GOLD))
        for t in transactions:
            list_content.append(create_transaction_item(ft.icons.WORK if t["type"] == "receita" else ft.icons.SHOPPING_BAG, t["description"], t["date"], t["category"], float(t["value"]), is_expense=(t["type"] == "despesa")))

    final_content = ft.Column(controls=list_content) if list_content else ft.Text("Adicione uma nova transação clicando no botão acima.", size=14, color=SOFT_GOLD, text_align=ft.TextAlign.CENTER)

    # --- Layout da Tela ---
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
                        ft.Container(height=45),
                        ft.Row(
                            [
                                ft.IconButton(icon=ft.icons.ARROW_BACK, icon_color=SOFT_GOLD, on_click=handle_back),
                                ft.Text("Transações", size=20, weight=ft.FontWeight.BOLD, color=SOFT_GOLD),
                                ft.IconButton(icon=ft.icons.NOTIFICATIONS_NONE, icon_color=SOFT_GOLD, icon_size=22, on_click=lambda _: page.go("/notifications")),
                            ],
                            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                        ),
                        ft.Container(
                            content=ft.IconButton(icon=ft.icons.ADD, icon_color=DARK_BG, icon_size=24, on_click=handle_add_transaction),
                            bgcolor=SOFT_GOLD, shape=ft.BoxShape.CIRCLE, width=50, height=50, alignment=ft.alignment.center,
                            margin=ft.margin.symmetric(vertical=20),
                        ),
                        final_content,
                        ft.Container(height=80), # Espaço para a navbar
                    ],
                    expand=True,
                    scroll=ft.ScrollMode.AUTO,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER
                ),
                get_navbar(page, active_index=2),
            ],
        ),
    )