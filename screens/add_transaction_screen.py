import flet as ft
import datetime

# Definindo cores personalizadas
DARK_BG = "#121212"
SOFT_GOLD = "#F7D679"
CARD_BG = "#1A1A1A"
TEXT_COLOR = "#FFFFFF"
INPUT_BG = "#2A2A2A"
BUTTON_COLOR = SOFT_GOLD
RED = "#FF3E3E"
GREEN = "#00D47E"

def get_add_transaction_screen(page: ft.Page, on_save: callable, on_save_recurring: callable, on_back: callable, user_id: str) -> ft.Container:
    """
    Cria a tela para adicionar uma nova transação (receita ou despesa),
    incluindo a opção para transações recorrentes.
    """

    # --- Controles da UI ---
    description_input = ft.TextField(
        label="Descrição",
        label_style=ft.TextStyle(color=SOFT_GOLD, size=14),
        border_color=SOFT_GOLD,
        border_width=1,
        border_radius=10,
        text_style=ft.TextStyle(color=TEXT_COLOR),
        bgcolor=INPUT_BG,
    )

    value_input = ft.TextField(
        label="Valor (R$)",
        label_style=ft.TextStyle(color=SOFT_GOLD, size=14),
        border_color=SOFT_GOLD,
        border_width=1,
        border_radius=10,
        text_style=ft.TextStyle(color=TEXT_COLOR),
        bgcolor=INPUT_BG,
        keyboard_type=ft.KeyboardType.NUMBER,
        prefix_text="R$ ",
    )

    category_dropdown = ft.Dropdown(
        label="Categoria",
        label_style=ft.TextStyle(color=SOFT_GOLD, size=14),
        border_color=SOFT_GOLD,
        border_width=1,
        border_radius=10,
        text_style=ft.TextStyle(color=TEXT_COLOR),
        bgcolor=INPUT_BG,
        options=[
            ft.dropdown.Option("salario", "Salário"),
            ft.dropdown.Option("freelance", "Freelance"),
            ft.dropdown.Option("investimento", "Investimento"),
            ft.dropdown.Option("presente", "Presente"),
            ft.dropdown.Option("outras_receitas", "Outras Receitas"),
            ft.dropdown.Option("alimentacao", "Alimentação"),
            ft.dropdown.Option("moradia", "Moradia"),
            ft.dropdown.Option("transporte", "Transporte"),
            ft.dropdown.Option("saude", "Saúde"),
            ft.dropdown.Option("lazer", "Lazer"),
            ft.dropdown.Option("educacao", "Educação"),
            ft.dropdown.Option("roupas", "Roupas"),
            ft.dropdown.Option("impostos", "Impostos"),
            ft.dropdown.Option("outras_despesas", "Outras Despesas"),
        ],
    )

    date_picker = ft.DatePicker(
        first_date=datetime.datetime(2023, 10, 1),
        last_date=datetime.datetime(2030, 10, 1),
        on_change=lambda e: print(f"Date changed: {date_picker.value}"),
    )
    page.overlay.append(date_picker)

    def show_date_picker(e):
        """Exibe o seletor de data."""
        date_picker.open = True
        page.update()

    date_button = ft.ElevatedButton(
        "Selecionar Data",
        icon=ft.icons.CALENDAR_MONTH,
        on_click=show_date_picker,
        style=ft.ButtonStyle(color=DARK_BG, bgcolor=SOFT_GOLD, shape=ft.RoundedRectangleBorder(radius=10)),
    )


    transaction_type_toggle = ft.Switch(
        label="Receita",
        value=True,  # True para Receita, False para Despesa
        active_color=GREEN,
        inactive_thumb_color=RED,
        on_change=lambda e: setattr(e.control, 'label', "Receita" if e.control.value else "Despesa") or page.update()
    )

    frequency_dropdown = ft.Dropdown(
        label="Frequência",
        label_style=ft.TextStyle(color=SOFT_GOLD, size=14),
        border_color=SOFT_GOLD,
        border_width=1,
        border_radius=10,
        text_style=ft.TextStyle(color=TEXT_COLOR),
        bgcolor=INPUT_BG,
        visible=False, # Começa invisível
        options=[
            ft.dropdown.Option("diario", "Diário"),
            ft.dropdown.Option("semanal", "Semanal"),
            ft.dropdown.Option("mensal", "Mensal"),
        ],
    )
    
    def toggle_recurring(e):
        is_recurring = e.control.value
        frequency_dropdown.visible = is_recurring
        page.update()

    recurring_switch = ft.Switch(
        label="Transação Recorrente",
        on_change=toggle_recurring
    )
    
    error_text = ft.Text("", color=RED, size=14, visible=False)

    # --- Funções de Manipulação de Eventos ---
    def handle_save_click(e):
        description = description_input.value
        value_str = value_input.value
        category = category_dropdown.value
        transaction_type = "receita" if transaction_type_toggle.value else "despesa"
        is_recurring = recurring_switch.value
        frequency = frequency_dropdown.value

        if not all([description, value_str, category]) or (is_recurring and not frequency):
            error_text.value = "Preencha todos os campos obrigatórios."
            error_text.visible = True
            page.update()
            return

        try:
            value = float(value_str.replace(",", "."))
        except ValueError:
            error_text.value = "O valor inserido é inválido."
            error_text.visible = True
            page.update()
            return

        transaction_data = {
            "user_id": user_id,
            "description": description,
            "value": value,
            "category": category,
            "date": date_picker.value.strftime('%Y-%m-%d') if date_picker.value else datetime.date.today().strftime('%Y-%m-%d'),
            "type": transaction_type,
        }

        if is_recurring:
            transaction_data["frequency"] = frequency
            on_save_recurring(transaction_data)
        else:
            on_save(transaction_data)

    save_button = ft.ElevatedButton(
        text="Salvar Transação",
        on_click=handle_save_click,
        style=ft.ButtonStyle(
            color=DARK_BG,
            bgcolor=BUTTON_COLOR,
            shape=ft.RoundedRectangleBorder(radius=10),
            padding=ft.padding.all(15),
        ),
    )

    # --- Layout da Tela ---
    return ft.Container(
        width=400,
        height=830,
        bgcolor=DARK_BG,
        border_radius=ft.border_radius.all(35),
        padding=ft.padding.only(left=20, right=20, top=20, bottom=20),
        content=ft.Column(
            [
                ft.Row(
                    [
                        ft.IconButton(icon=ft.icons.ARROW_BACK, icon_color=SOFT_GOLD, on_click=lambda e: on_back()),
                        ft.Text("Adicionar Transação", size=20, weight=ft.FontWeight.BOLD, color=SOFT_GOLD),
                        ft.Container(width=40),
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                ),
                ft.Divider(height=20, color="transparent"),
                description_input,
                value_input,
                category_dropdown,
                ft.Row([ft.Text("Data da Transação:", color=TEXT_COLOR), date_button]),
                ft.Row([ft.Text("Tipo:", color=TEXT_COLOR, size=16), transaction_type_toggle], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
                ft.Row([ft.Text("Transação Recorrente:", color=TEXT_COLOR, size=16), recurring_switch], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
                frequency_dropdown,
                ft.Divider(height=20, color="transparent"),
                error_text,
                ft.Row([save_button], alignment=ft.MainAxisAlignment.CENTER),
            ],
            scroll=ft.ScrollMode.AUTO,
            spacing=15,
        )
    )