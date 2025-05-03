import flet as ft
from datetime import datetime

def get_add_transaction_screen(page: ft.Page, on_save: callable, user_id: str) -> ft.Container:
    # Definindo cores personalizadas
    DARK_BG = "#121212"
    SOFT_GOLD = "#F7D679"
    CARD_BG = "#1A1A1A"
    
    # Variáveis para armazenar os valores dos campos
    transaction_type = ft.Dropdown(
        label="Tipo",
        options=[
            ft.dropdown.Option("receita", "Receita"),
            ft.dropdown.Option("despesa", "Despesa"),
        ],
        value="despesa",
        width=300,
        color=SOFT_GOLD,
        border_color=SOFT_GOLD,
    )

    value_field = ft.TextField(
        label="Valor",
        prefix_text="R$ ",
        width=300,
        color=SOFT_GOLD,
        border_color=SOFT_GOLD,
    )
    
    category_field = ft.Dropdown(
        label="Categoria",
        options=[
            ft.dropdown.Option("alimentacao", "Alimentação"),
            ft.dropdown.Option("transporte", "Transporte"),
            ft.dropdown.Option("moradia", "Moradia"),
            ft.dropdown.Option("lazer", "Lazer"),
            ft.dropdown.Option("salario", "Salário"),
            ft.dropdown.Option("outros", "Outros"),
        ],
        width=300,
        color=SOFT_GOLD,
        border_color=SOFT_GOLD,
    )
    
    description_field = ft.TextField(
        label="Descrição",
        multiline=True,
        min_lines=2,
        max_lines=3,
        width=300,
        color=SOFT_GOLD,
        border_color=SOFT_GOLD,
    )

    # Configuração do DatePicker
    date_picker = ft.DatePicker(
        first_date=datetime(2020, 1, 1),
        last_date=datetime(2030, 12, 31),
    )
    
    page.overlay.append(date_picker)

    def open_date_picker():
        date_picker.open = True
        page.update()
    
    # Botão para abrir o DatePicker
    date_button = ft.ElevatedButton(
        "Selecionar Data",
        icon=ft.icons.CALENDAR_MONTH,
        on_click=lambda _: open_date_picker(),
        bgcolor=SOFT_GOLD,
        color=DARK_BG,
        width=300,
    )
    
    # Texto para mostrar a data selecionada
    selected_date = ft.Text(
        "Data: " + datetime.now().strftime("%d/%m/%Y"),
        color=SOFT_GOLD,
    )
    
    def handle_date_change(e):
        selected_date.value = f"Data: {e.control.value.strftime('%d/%m/%Y')}"
        page.update()
    
    date_picker.on_change = handle_date_change
    
    def save_transaction(e):
        if all([transaction_type.value, value_field.value, category_field.value, description_field.value]):
            try:
                transaction_data = {
                    "user_id": user_id,  # Usa o ID do usuário passado como argumento
                    "type": transaction_type.value,
                    "value": float(value_field.value.replace("R$ ", "").replace(",", ".")),
                    "category": category_field.value,
                    "description": description_field.value,
                    "date": date_picker.value.strftime("%d/%m/%Y") if date_picker.value else datetime.now().strftime("%d/%m/%Y")
                }
                on_save(transaction_data)  # Chama a função de salvar
                page.go("/transactions")  # Redireciona para a tela de transações
            except ValueError:
                print("Erro: Valor inválido.")
        else:
            print("Erro: Preencha todos os campos.")
    
    return ft.Container(
        width=400,
        height=830,
        bgcolor=DARK_BG,
        border_radius=ft.border_radius.all(35),
        padding=ft.padding.only(left=20, right=20),
        content=ft.Column(
            [
                ft.Container(height=45),  # Espaço superior
                
                # Cabeçalho
                ft.Row(
                    [
                        ft.Text(
                            "Nova Transação",
                            size=24,
                            weight=ft.FontWeight.BOLD,
                            color=SOFT_GOLD,
                        ),
                        ft.IconButton(
                            icon=ft.icons.CLOSE,
                            icon_color=SOFT_GOLD,
                            on_click=lambda _: page.go("/transactions"),
                        ),
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                ),
                
                ft.Container(height=20),
                
                # Formulário
                ft.Container(
                    content=ft.Column(
                        [
                            transaction_type,
                            ft.Container(height=10),
                            value_field,
                            ft.Container(height=10),
                            category_field,
                            ft.Container(height=10),
                            description_field,
                            ft.Container(height=10),
                            selected_date,
                            date_button,
                            ft.Container(height=20),
                            ft.ElevatedButton(
                                "Salvar",
                                on_click=save_transaction,
                                bgcolor=SOFT_GOLD,
                                color=DARK_BG,
                                width=300,
                            ),
                        ],
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    ),
                    bgcolor=CARD_BG,
                    padding=20,
                    border_radius=15,
                ),
            ],
            scroll=ft.ScrollMode.AUTO,
        ),
    )