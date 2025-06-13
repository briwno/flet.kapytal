from gc import freeze

import flet as ft
import threading
import warnings
import uuid

# Importações das telas
from screens.info_screen import get_info_screen
from screens.settings_screen import get_settings_screen, get_change_password_screen, get_notifications_settings_screen
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

# Importações de utilitários e dados
from layout import create_iphone_layout
from storage.data.user_data import (
    register_user, authenticate_user, save_transactions, 
    update_user, save_recurring_transaction
)
from api.api_code import get_brazil_news, get_currency_rates
from storage.database_connect import DatabaseConnection
from storage.cache import app_cache

warnings.filterwarnings("ignore", category=DeprecationWarning)

# Verifica a conexão com o banco de dados
db = DatabaseConnection()
try:
    db.connect()
    print("✅ Conexão com o banco de dados estabelecida com sucesso.")
except Exception as e:
    print(f"❌ Erro ao conectar ao banco de dados: {e}")

logged_user_id = None
news_data = None
currency_data = None

def main(page: ft.Page):
    """
    Função principal do aplicativo.
    """
    page.title = "Simulação iPhone"
    page.window_width = 430
    page.window_height = 932
    page.bgcolor = ft.colors.BLACK
    page.update()

    def show_loading_screen():
        """Exibe uma tela de carregamento genérica."""
        loading_spinner = ft.Column(
            [ft.ProgressRing(width=32, height=32, stroke_width=3, color="#F7D679")],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            expand=True,
        )
        return ft.View(
            "/loading",
            [ft.Row([create_iphone_layout(loading_spinner)], alignment=ft.MainAxisAlignment.CENTER)],
            bgcolor=ft.colors.BLACK,
        )

    def load_news_and_currency_data():
        """Carrega dados da API de notícias e moeda em uma thread separada."""
        def load():
            global news_data, currency_data
            if news_data is None:
                try:
                    print("Carregando dados de notícias e moeda...")
                    news_data = get_brazil_news()
                    currency_data = get_currency_rates()
                    print("Dados de notícias e moeda carregados com sucesso!")
                except Exception as e:
                    print(f"Erro ao carregar dados da API: {e}")
        
        threading.Thread(target=load).start()

    def route_change(route):
        print(f"Rota mudou para: {page.route}")
        page.views.clear()

        # --- Handlers para ações nas telas ---
        def handle_logout():
            global logged_user_id
            logged_user_id = None
            app_cache.clear_cache()
            page.go("/login")
        
        def handle_save_transaction(transaction_data):
            save_transactions(transaction_data)
            app_cache.clear_cache(logged_user_id)
            page.go("/transactions") # Alterado de "/home"

        def handle_save_recurring_transaction(transaction_data):
            save_recurring_transaction(transaction_data)
            app_cache.clear_cache(logged_user_id)
            page.go("/transactions")

        def handle_update_user(name, email, phone):
            success, message = update_user(logged_user_id, name=name, email=email, phone=phone)
            if success:
                app_cache.get_user(logged_user_id, force_refresh=True)
                page.go("/profile")
            else:
                page.snackbar = ft.SnackBar(ft.Text(message), bgcolor=ft.colors.RED)
                page.snackbar.open = True
                page.update()

        # --- Funções de carregamento e construção de tela ---
        def load_and_build(build_function):
            """Exibe a tela de carregamento e constrói a tela de destino em paralelo."""
            page.views.append(show_loading_screen())
            page.update()
            threading.Thread(target=build_function).start()
        
        def build_and_display(route, screen):
            """Atualiza a view atual com o conteúdo da nova tela."""
            page.views[0].route = route
            page.views[0].controls = [ft.Row([create_iphone_layout(screen)], alignment=ft.MainAxisAlignment.CENTER)]
            page.update()

        # --- Funções para construir cada tela ---
        def build_home_screen():
            user_data = app_cache.get_user(logged_user_id)
            if user_data is None: page.go("/login"); return
            transactions = app_cache.get_transactions(logged_user_id)
            screen = get_home_screen(page, on_logout=handle_logout, on_notification=lambda: page.go("/notifications"), user_name=user_data.get("name", ""), transactions=transactions or [])
            build_and_display("/home", screen)

        def build_analysis_screen():
            transactions = app_cache.get_transactions(logged_user_id, force_refresh=True)
            screen = get_analysis_screen(page, on_notification=lambda: page.go("/notifications"), transactions=transactions or [])
            build_and_display("/analysis", screen)

        def build_transactions_screen():
            screen = get_transaction_screen(page, on_back=lambda: page.go("/home"), user_id=logged_user_id)
            build_and_display("/transactions", screen)

        def build_profile_screen():
            user_data = app_cache.get_user(logged_user_id)
            if user_data is None: page.go("/login"); return
            screen = get_profile_screen(page, on_back=lambda: page.go("/home"), on_logout=handle_logout, user_id=logged_user_id)
            build_and_display("/profile", screen)

        def build_edit_profile_screen():
            user_data = app_cache.get_user(logged_user_id)
            if user_data is None: page.go("/login"); return
            screen = get_edit_profile_screen(page, on_save=handle_update_user, on_back=lambda: page.go("/profile"), user_id=logged_user_id)
            build_and_display("/edit_profile", screen)

        def build_login_screen():
            def handle_login(email, password):
                global logged_user_id
                success, user_data = authenticate_user(email, password)
                if success:
                    logged_user_id = user_data["id"]
                    app_cache.clear_cache()
                    page.go("/home")
                else: print(user_data)
            screen = get_login_screen(page, on_login=handle_login, switch_to_register=lambda: page.go("/register"))
            build_and_display("/login", screen)

        def build_register_screen():
            def handle_register(name, email, password, confirm_password):
                if password == confirm_password:
                    user_id = str(uuid.uuid4())
                    success, message = register_user(user_id, name, email, password)
                    if success: page.go("/login")
                    else: print(message)
                else: print("As senhas não coincidem")
            screen = get_register_screen(page, on_register=handle_register, switch_to_login=lambda: page.go("/login"))
            build_and_display("/register", screen)

        def build_news_screen():
            if not news_data or not currency_data:
                page.snackbar = ft.SnackBar(ft.Text("Dados de notícias ou moeda não carregados.\nTente novamente mais tarde."), bgcolor=ft.colors.RED)
                page.snackbar.open = True
                # Espera 1 segundo para exibir a mensagem
                threading.Event().wait(1)
                page.update()
                page.go("/home")
            else:
                screen = get_news_screen(page, on_notification=lambda: page.go("/notifications"), news_data=news_data, currency_data=currency_data)
                build_and_display("/news", screen)

        def build_add_transaction_screen():
            screen = get_add_transaction_screen(
                page, 
                on_save=handle_save_transaction, 
                on_save_recurring=handle_save_recurring_transaction,
                on_back=lambda: page.go("/transactions"), 
                user_id=logged_user_id
            )
            build_and_display("/add_transaction", screen)

        def build_notification_screen():
            screen = get_notification_screen(page, on_back=lambda: page.go("/home"))
            build_and_display("/notifications", screen)

        def build_settings_screen():
            screen = get_settings_screen(page, on_back=lambda: page.go("/profile"), on_logout=handle_logout)
            build_and_display("/settings", screen)

        def build_change_password_screen():
            screen = get_change_password_screen(page, on_back=lambda: page.go("/settings"), user_id=logged_user_id)
            build_and_display("/change_password", screen)

        def build_notifications_settings_screen():
            screen = get_notifications_settings_screen(page, on_back=lambda: page.go("/settings"))
            build_and_display("/notifications_settings", screen)

        def build_info_screen():
            screen = get_info_screen(page, on_back=lambda: page.go("/profile"))
            build_and_display("/info", screen)

        # --- Lógica de Roteamento ---
        routes = {
            "/login": build_login_screen,
            "/register": build_register_screen,
            "/home": build_home_screen,
            "/analysis": build_analysis_screen,
            "/transactions": build_transactions_screen,
            "/profile": build_profile_screen,
            "/edit_profile": build_edit_profile_screen,
            "/news": build_news_screen,
            "/add_transaction": build_add_transaction_screen,
            "/notifications": build_notification_screen,
            "/settings": build_settings_screen,
            "/change_password": build_change_password_screen,
            "/notifications_settings": build_notifications_settings_screen,
            "/info": build_info_screen,
        }
        
        if page.route == "/":
            load_news_and_currency_data()
            page.go("/login")
        elif page.route in routes:
            build_function = routes[page.route]
            load_and_build(build_function)
        else:
            # Rota não encontrada (opcional)
            page.views.append(ft.View("/", [ft.Text("Página não encontrada")]))

        page.update()

    def view_pop(view):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go("/")

ft.app(target=main)