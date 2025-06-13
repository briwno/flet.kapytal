import flet as ft
from components.navbar import get_navbar
from storage.data.user_data import get_user_by_id
from storage.data.user_data import update_user

def get_settings_screen(page: ft.Page, on_back: callable, on_logout: callable) -> ft.Container:
    # Definindo cores personalizadas
    GOLD = "#FFD700"
    SOFT_GOLD = "#F7D679"
    DARK_BG = "#121212"
    CARD_BG = "#1A1A1A"
    ICON_BG = "#262626"
    
    def handle_back():
        page.go("/profile")
        
    return ft.Container(
        width=400,
        height=830,
        bgcolor=DARK_BG,
        border_radius=ft.border_radius.all(35),
        content=ft.Stack(
            controls=[
                ft.Column(
                    controls=[
                        # Cabeçalho
                        ft.Container(
                            padding=ft.padding.symmetric(horizontal=16, vertical=30),
                            content=ft.Row(
                                controls=[
                                    ft.IconButton(
                                        icon=ft.icons.ARROW_BACK,
                                        icon_color=SOFT_GOLD,
                                        on_click=lambda _: handle_back(),
                                        icon_size=20,
                                    ),
                                    ft.Text(
                                        "Perfil",
                                        size=20,
                                        weight=ft.FontWeight.BOLD,
                                        color=SOFT_GOLD,
                                    ),
                                    ft.IconButton(
                                        icon=ft.icons.NOTIFICATIONS_NONE,
                                        icon_color=SOFT_GOLD,
                                        on_click=lambda _: page.go("/notifications"),
                                        icon_size=20,
                                    ),
                                ],
                                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                                vertical_alignment=ft.CrossAxisAlignment.CENTER,
                            ),
                        ),

                        # Configurações do aplicativo
                        ft.Container(
                            alignment=ft.alignment.center,
                            padding=ft.padding.only(top=10, bottom=20),
                            content=ft.Column(
                                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                spacing=10,
                                controls=[
                                    ft.Text(
                                        "Configurações do Aplicativo",
                                        size=20,
                                        weight=ft.FontWeight.BOLD,
                                        color=SOFT_GOLD,
                                    ),
                                    ft.Text(
                                        "Gerencie suas preferências e configurações.",
                                        size=14,
                                        color="#FFFFFF",
                                    ),
                                ],
                            ),
                        ),
                        
                        # Opções de configuração
                        ft.Container(
                            bgcolor=DARK_BG,
                            padding=ft.padding.all(20),
                            border_radius=ft.border_radius.all(20),
                            content=ft.Column(
                                spacing=10,
                                controls=[
                                    settings_option(
                                        icon=ft.icons.PASSWORD,
                                        text="Senha",
                                        color=SOFT_GOLD,
                                        bgcolor=ICON_BG,
                                        on_click=lambda _: page.go("/change_password"),
                                    ),
                                    settings_option(
                                        icon=ft.icons.NOTIFICATIONS,
                                        text="Notificações",
                                        color=SOFT_GOLD,
                                        bgcolor=ICON_BG,
                                        on_click=lambda _: page.go("/notifications_settings"),
                                    ),
                                    settings_option(
                                        icon=ft.icons.LOGOUT,
                                        text="Sair",
                                        color=SOFT_GOLD,
                                        bgcolor=ICON_BG,
                                        on_click=on_logout,
                                    ),
                                ],
                            ),
                        ),

                        ft.Container(height=80),  # Espaço para a navbar
                    ],
                    alignment=ft.MainAxisAlignment.START,
                    spacing=0,
                ),
                # Navbar fixa
                get_navbar(page, active_index=4),
            ]
        ),
    )
    
    # Função auxiliar para criar opções de configuração
def settings_option(icon, text, color, bgcolor, on_click=None):
    return ft.Container(
        content=ft.Row(
            controls=[
                ft.Container(
                    content=ft.IconButton(
                        icon=icon,
                        icon_color=color,
                        icon_size=24,
                        on_click=on_click
                    ),
                    bgcolor=bgcolor,
                    padding=8,
                    border_radius=12,
                ),
                ft.Text(
                    text,
                    size=16,
                    color=color,
                    weight=ft.FontWeight.W_500,
                ),
            ],
            spacing=10,
        ),
        padding=12,
        border_radius=12,
        margin=ft.margin.symmetric(vertical=4, horizontal=20),
    )

def get_change_password_screen(page: ft.Page, on_back: callable,  user_id: str) -> ft.Container:
    DARK_BG = "#121212"
    SOFT_GOLD = "#F7D679"
    CARD_BG = "#1A1A1A"

    # Campos de texto precisam ser definidos fora do handler para acesso
    texfield_senha_atual = ft.TextField(
        label="Senha Atual",
        password=True,
        bgcolor=CARD_BG,
        color=SOFT_GOLD,
    )
    texfield_nova_senha = ft.TextField(
        label="Nova Senha",
        password=True,
        bgcolor=CARD_BG,
        color=SOFT_GOLD,
    )
    texfield_confirmar_senha = ft.TextField(
        label="Confirmar Nova Senha",
        password=True,
        bgcolor=CARD_BG,
        color=SOFT_GOLD,
    )

    def handle_save(e):
        senha_atual = texfield_senha_atual.value
        nova_senha = texfield_nova_senha.value
        confirmar_senha = texfield_confirmar_senha.value
        user = get_user_by_id(user_id)

        if senha_atual != user["password"]:
            page.snackbar = ft.SnackBar(
                ft.Text("Senha atual incorreta."),
                bgcolor="#FF0000",
            )
            page.snackbar.open = True
            page.update()
            return

        if not nova_senha or not confirmar_senha:
            page.snackbar = ft.SnackBar(
                ft.Text("Preencha todos os campos."),
                bgcolor="#FF0000",
            )
            page.snackbar.open = True
            page.update()
            return

        if nova_senha != confirmar_senha:
            page.snackbar = ft.SnackBar(
                ft.Text("As senhas não coincidem."),
                bgcolor="#FF0000",
            )
            page.snackbar.open = True
            page.update()
            return

        # Atualiza a senha
        success, message = update_user(
            user_id,
            password=nova_senha
        )
        if not success:
            page.snackbar = ft.SnackBar(
                ft.Text(message),
                bgcolor="#FF0000",
            )
            page.snackbar.open = True
            page.update()
            return

        page.snackbar = ft.SnackBar(
            ft.Text("Senha alterada com sucesso!"),
            bgcolor="#4BB543",
        )
        page.snackbar.open = True
        page.update()
        page.go("/settings")

    return ft.Container(
        width=400,
        height=830,
        bgcolor=DARK_BG,
        border_radius=ft.border_radius.all(35),
        content=ft.Container(
            padding=20,
            content=ft.Column(
                [
                    ft.Row(
                        [
                            ft.IconButton(
                                icon=ft.icons.ARROW_BACK,
                                icon_color=SOFT_GOLD,
                                on_click=lambda _: on_back(),
                            ),
                            ft.Text(
                                "Alterar Senha",
                                size=20,
                                weight=ft.FontWeight.BOLD,
                                color=SOFT_GOLD,
                            ),
                        ],
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                    ),
                    ft.Container(height=20),
                    texfield_senha_atual,
                    texfield_nova_senha,
                    texfield_confirmar_senha,
                    ft.ElevatedButton(
                        "Salvar",
                        on_click=handle_save,
                        bgcolor=SOFT_GOLD,
                        color=DARK_BG,
                    ),
                ],
                spacing=20,
            ),
        ),
    )
    
def get_notifications_settings_screen(page: ft.Page, on_back: callable) -> ft.Container:
    DARK_BG = "#121212"
    SOFT_GOLD = "#F7D679"

    return ft.Container(
        width=400,
        height=830,
        bgcolor=DARK_BG,
        border_radius=ft.border_radius.all(35),
        content=ft.Container(  # Adicionado Container para padding
            padding=20,
            content=ft.Column(
                [
                    ft.Row(
                        [
                            ft.IconButton(
                                icon=ft.icons.ARROW_BACK,
                                icon_color=SOFT_GOLD,
                                on_click=lambda _: on_back(),
                            ),
                            ft.Text(
                                "Configurações de Notificações",
                                size=20,
                                weight=ft.FontWeight.BOLD,
                                color=SOFT_GOLD,
                            ),
                        ],
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                    ),
                    ft.Switch(label="Notificações por E-mail", value=True),
                    ft.Switch(label="Notificações Push", value=False),
                ],
                spacing=20,
            ),
        ),
    )
