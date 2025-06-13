import flet as ft
from components.navbar import get_navbar
from storage.data.user_data import get_user_by_id

def get_edit_profile_screen(page: ft.Page, on_back: callable, on_save: callable, user_id: str) -> ft.Container:
    # Definindo cores personalizadas
    SOFT_GOLD = "#F7D679"
    DARK_BG = "#121212"
    CARD_BG = "#1A1A1A"

    # Busca os dados do usuário de forma consistente com o cache
    user_data = get_user_by_id(user_id)
    if not user_data:
        return ft.Container(content=ft.Text("Usuário não encontrado.", color="red"))

    nome = user_data.get("name", "")
    email = user_data.get("email", "")
    phone = user_data.get("phone", "")

    def handle_save(e):
        # Chama a função de salvar passada como parâmetro
        on_save(name_input.value, email_input.value, phone_input.value)

    # Campos de entrada para edição de perfil
    name_input = ft.TextField(
        label="Nome", value=nome, bgcolor=CARD_BG, border_radius=10, color=SOFT_GOLD
    )
    email_input = ft.TextField(
        label="E-mail", value=email, bgcolor=CARD_BG, border_radius=10, color=SOFT_GOLD
    )
    phone_input = ft.TextField(
        label="Telefone", value=phone or "", hint_text="+55 41 99861 9866", bgcolor=CARD_BG, border_radius=10, color=SOFT_GOLD
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
                                ft.IconButton(
                                    icon=ft.icons.ARROW_BACK,
                                    icon_color=SOFT_GOLD,
                                    on_click=lambda _: on_back(),
                                ),
                                ft.Text(
                                    "Editar Perfil",
                                    size=20,
                                    weight=ft.FontWeight.BOLD,
                                    color=SOFT_GOLD,
                                ),
                                # Espaço para manter o alinhamento do título
                                ft.Container(width=40),
                            ],
                            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                        ),
                        ft.Container(height=20),
                        # Formulário de edição
                        ft.Container(
                            content=ft.Column(
                                [
                                    name_input,
                                    ft.Container(height=10),
                                    email_input,
                                    ft.Container(height=10),
                                    phone_input,
                                    ft.Container(height=20),
                                    ft.ElevatedButton(
                                        "Salvar",
                                        on_click=handle_save,
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
                    expand=True,
                ),
                # Navbar fixa
                get_navbar(page, active_index=4),
            ],
        ),
    )