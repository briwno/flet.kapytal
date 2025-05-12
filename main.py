import flet as ft
import threading
import warnings
import uuid
from screens.info_screen import get_info_screen
from screens.settings_screen import get_settings_screen
from storage.data.user_data import get_user_by_id
from screens.analysis_screen import get_analysis_screen
from screens.login_screen import get_login_screen
from screens.news_screen import get_news_screen
from screens.profile_screen import get_profile_screen
from screens.register_screen import get_register_screen
from screens.home_screen import get_home_screen
from screens.add_transaction_screen import get_add_transaction_screen
from screens.notification_screen import get_notification_screen
from screens.transaction_screen import get_transaction_screen
from screens.edit_profile_screen import get_edit_profile_screen
from screens.settings_screen import get_change_password_screen
from screens.settings_screen import get_notifications_settings_screen
from screens.settings_screen import get_theme_settings_screen
from layout import create_iphone_layout
from storage.data.user_data import register_user, authenticate_user, save_transactions, load_transactions
from api.api_code import get_brazil_news, get_currency_rates


warnings.filterwarnings("ignore", category=DeprecationWarning)

logged_user_id = None  # Variável global para armazenar o ID do usuário logado


def main(page: ft.Page):
    """
    Função principal do aplicativo.
    :param page: A página principal do Flet.
    """
    # Configurações iniciais da página
    page.title = "Simulação iPhone"
    page.window_width = 430
    page.window_height = 932
    page.bgcolor = ft.colors.BLACK
    page.update()
    
    def load_data():
        try:
            global news_data, currency_data  # Variáveis globais para armazenar os dados
            news_data = get_brazil_news()
            currency_data = get_currency_rates()
            print("Dados carregados com sucesso!")
        except Exception as e:
            print(f"Erro ao carregar dados: {e}")
        
                
    def route_change(route):
        print(f"Rota mudou para: {route}")
        
        # Cria uma nova view para a rota atual
        if page.route == "/":
            load_data()
            initial_screen = ft.Container(
                width=390,
                height=844,
                bgcolor=ft.colors.WHITE70,
                border_radius=ft.border_radius.all(50),
                padding=ft.padding.all(10),
                content=ft.Column(
                    [
                        ft.Text(
                            "Bem-vindo ao App!",
                            size=30,
                            color=ft.colors.BLACK,
                            text_align=ft.TextAlign.CENTER
                        ),
                        ft.Text(
                            "Esta é uma simulação de iPhone.",
                            size=20,
                            color=ft.colors.BLACK,
                            text_align=ft.TextAlign.CENTER
                        ),
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER
                )
            )
            
            # Adiciona a tela inicial
            page.views.append(
                ft.View(
                    route="/",
                    controls=[ft.Row([create_iphone_layout(initial_screen)], alignment=ft.MainAxisAlignment.CENTER)]
                )
            )
            page.update()

            # Redireciona para a tela de login após exibir a tela inicial
            page.go("/login")
            
        elif page.route == "/login":
            def handle_login(email, password):
                global logged_user_id
                success, user_data = authenticate_user(email, password)
                if success:
                    logged_user_id = user_data["id"]  # Armazena o ID do usuário logado
                    print(f"Bem-vindo, {user_data['name']}! ID: {logged_user_id}")
                    page.go("/home")
                else:
                    print(user_data)  # Exibe a mensagem de erro

            login_screen = get_login_screen(
                page,
                on_login=handle_login,
                switch_to_register=lambda: page.go("/register")
            )
            page.views.append(
                ft.View(
                    route="/login",
                    controls=[ft.Row([create_iphone_layout(login_screen)], alignment=ft.MainAxisAlignment.CENTER)]
                )
            )
        elif page.route == "/register":
            def handle_register(name, email, password, confirm_password):
                if password == confirm_password:
                    user_id = str(uuid.uuid4())
                    success, message = register_user(user_id, name, email, password)
                    if success:
                        print(f"Usuário {name} registrado com sucesso com ID {user_id}!")
                        page.go("/login")
                    else:
                        print(message)
                else:
                    print("As senhas não coincidem")

            register_screen = get_register_screen(
                page,
                on_register=handle_register,
                switch_to_login=lambda: page.go("/login")
            )
            page.views.append(
                ft.View(
                    route="/register",
                    controls=[ft.Row([create_iphone_layout(register_screen)], alignment=ft.MainAxisAlignment.CENTER)]
                )
            )
        elif page.route == "/home":
            user_data = get_user_by_id(logged_user_id)  # Obtém os dados do usuário logado
            if user_data is None:
                print("Usuário não encontrado.")
                page.go("/login")
                return

            transactions = load_transactions(logged_user_id)  # Carrega as transações do usuário logado

            home_screen = get_home_screen(
                page,
                on_logout=lambda: page.go("/login"),
                on_notification=lambda: page.go("/notifications"),
                user_name=user_data["name"],
                transactions=transactions  # Passa as transações para a tela
            )
            page.views.append(
                ft.View(
                    route="/home",
                    controls=[ft.Row([create_iphone_layout(home_screen)], alignment=ft.MainAxisAlignment.CENTER)]
                )
            )
        elif page.route == "/analysis":
            analysis_screen = get_analysis_screen(
                page,
                on_notification=lambda: page.go("/notifications"),
                transactions=load_transactions(logged_user_id),  # Carrega as transações do usuário logado
            )
            page.views.append(
                ft.View(
                    route="/analysis",
                    controls=[ft.Row([create_iphone_layout(analysis_screen)], alignment=ft.MainAxisAlignment.CENTER)]
                )
            )
        elif page.route == "/add":
            def handle_save(transaction_data):
                save_transactions(transaction_data)  # Salva a transação no arquivo
                print("Transação salva:", transaction_data)
                page.go("/transactions")  # Redireciona para a tela de transações

            add_transaction_screen = get_add_transaction_screen(
                page,
                on_save=handle_save,
                user_id=logged_user_id  # Passa o ID do usuário logado
            )
            page.views.append(
                ft.View(
                    route="/add",
                    controls=[ft.Row([create_iphone_layout(add_transaction_screen)], alignment=ft.MainAxisAlignment.CENTER)]
                )
            )
        elif page.route == "/notifications":
            notification_screen = get_notification_screen(
                page,
                on_back=lambda: page.go("/home")
            )
            page.views.append(
                ft.View(
                    route="/notifications",
                    controls=[ft.Row([create_iphone_layout(notification_screen)], alignment=ft.MainAxisAlignment.CENTER)]
                )
            )
        elif page.route == "/transactions":
            transaction_screen = get_transaction_screen(
                page,
                on_back=lambda: page.go("/home"),
                user_id=logged_user_id  # Passa o ID do usuário logado
            )
            page.views.append(
                ft.View(
                    route="/transactions",
                    controls=[ft.Row([create_iphone_layout(transaction_screen)], alignment=ft.MainAxisAlignment.CENTER)]
                )
            )
        elif page.route == "/news":
            news_screen = get_news_screen(
                page,
                on_notification=lambda: page.go("/notifications"),
                news_data=news_data,  # Dados carregados uma vez
                currency_data=currency_data  # Dados carregados uma vez
            )
            page.views.append(
                ft.View(
                    route="/news",
                    controls=[ft.Row([create_iphone_layout(news_screen)], alignment=ft.MainAxisAlignment.CENTER)]
                )
            )
        elif page.route == "/profile":
            profile_screen = get_profile_screen(
                page,
                on_back=lambda: page.go("/home"),
                on_logout=lambda: page.go("/login"),
                user_id=logged_user_id  # Passa o ID do usuário logado
            )
            page.views.append(
                ft.View(
                    route="/profile",
                    controls=[ft.Row([create_iphone_layout(profile_screen)], alignment=ft.MainAxisAlignment.CENTER)]
                )
            )
        elif page.route == "/edit_profile":
            edit_profile_screen = get_edit_profile_screen(
                page,
                on_back=lambda: page.go("/home"),
                on_logout=lambda: page.go("/login"),
                user_id=logged_user_id  # Passa o ID do usuário logado
            )
            page.views.append(
                ft.View(
                    route="/edit_profile",
                    controls=[ft.Row([create_iphone_layout(edit_profile_screen)], alignment=ft.MainAxisAlignment.CENTER)]
                )
            )
        elif page.route == "/info":
            info_screen = get_info_screen(
                page,
                on_back=lambda: page.go("/home"),
                on_logout=lambda: page.go("/login")
            )
            page.views.append(
                ft.View(
                    route="/info",
                    controls=[ft.Row([create_iphone_layout(info_screen)], alignment=ft.MainAxisAlignment.CENTER)]
                )
            )
        elif page.route == "/settings":
            settings_screen = get_settings_screen(
                page,
                on_back=lambda: page.go("/home"),
                on_logout=lambda: page.go("/login")
            )
            page.views.append(
                ft.View(
                    route="/settings",
                    controls=[ft.Row([create_iphone_layout(settings_screen)], alignment=ft.MainAxisAlignment.CENTER)]
                )
            )
        elif page.route == "/change_password":
            change_password_screen = get_change_password_screen(
                page,
                
                on_back=lambda: page.go("/settings"),
                user_id=logged_user_id  # Passa o ID do usuário logado
            )
            page.views.append(
                ft.View(
                    route="/change_password",
                    controls=[ft.Row([create_iphone_layout(change_password_screen)], alignment=ft.MainAxisAlignment.CENTER)]    
                )
            )
        elif page.route == "/notifications_settings":
            notifications_settings_screen = get_notifications_settings_screen(
                page,
                on_back=lambda: page.go("/settings"),
            )
            page.views.append(
                ft.View(
                    route="/notifications_settings",
                    controls=[ft.Row([create_iphone_layout(notifications_settings_screen)], alignment=ft.MainAxisAlignment.CENTER)]
                    
                )
            )
        elif page.route == "/theme_settings":
            theme_settings_screen = get_theme_settings_screen(
                page,
                on_back=lambda: page.go("/settings"),
            )
            page.views.append(
                ft.View(
                    route="/theme_settings",
                    controls=[ft.Row([create_iphone_layout(theme_settings_screen)], alignment=ft.MainAxisAlignment.CENTER)]
                )
            )
            
        
        page.update()

    def view_pop(view):
        page.views.pop()
        if page.views:
            top_view = page.views[-1]
            page.go(top_view.route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go("/")


# Inicializa o aplicativo
ft.app(target=main)