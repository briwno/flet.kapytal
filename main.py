import flet as ft
import threading
from screens.login_screen import get_login_screen
from screens.profile_screen import get_profile_screen
from screens.register_screen import get_register_screen
from screens.home_screen import get_home_screen
from screens.add_transaction_screen import get_add_transaction_screen
from screens.notification_screen import get_notification_screen
from screens.transaction_screen import get_transaction_screen
from layout import create_iphone_layout


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
    
    def close_dialog(tela):
        tela.open = False
        page.update()
        page.go("/home")
                
    def route_change(route):
        print(f"Rota mudou para: {route}")
        page.clean()
        
        if page.route == "/":
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
            page.add(ft.Row([create_iphone_layout(initial_screen)], alignment=ft.MainAxisAlignment.CENTER))
            threading.Timer(1, lambda: page.go("/login")).start()
            
        elif page.route == "/login":
            def handle_login():
                print("Função handle_login chamada")
                page.go("/home")
                
            login_screen = get_login_screen(
                page,
                on_login=handle_login,
                switch_to_register=lambda: page.go("/register")
            )
            page.add(ft.Row([create_iphone_layout(login_screen)], alignment=ft.MainAxisAlignment.CENTER))
            
        elif page.route == "/register":
            register_screen = get_register_screen(
                page,
                on_register=lambda: print("Registrar clicado!"),
                switch_to_login=lambda: page.go("/login")
            )
            page.add(ft.Row([create_iphone_layout(register_screen)], alignment=ft.MainAxisAlignment.CENTER))
            
        elif page.route == "/home":
            home_screen = get_home_screen(
                page,
                on_logout=lambda: page.go("/login"),
                on_notification=lambda: page.go("/notifications")
            )
            page.add(ft.Row([create_iphone_layout(home_screen)], alignment=ft.MainAxisAlignment.CENTER))
            
        elif page.route == "/analysis":
            analysis_screen = ft.AlertDialog(
                modal=True,
                title=ft.Text("Análise Financeira"),
                content=ft.Text("Tela de análise financeira em desenvolvimento."),
                actions=[
                    ft.TextButton("Fechar", on_click=lambda _: close_dialog(analysis_screen)),
                    
                ]
            )
            page.dialog = analysis_screen
            analysis_screen.open = True
            page.update()
            page.add(ft.Row([create_iphone_layout(analysis_screen)], alignment=ft.MainAxisAlignment.CENTER))
            
        elif page.route == "/add":
            def handle_save(transaction_data):
                print("Transação salva:", transaction_data)
                page.go("/home")
                
            add_transaction_screen = get_add_transaction_screen(
                page,
                on_save=handle_save
            )
            page.add(ft.Row([create_iphone_layout(add_transaction_screen)], alignment=ft.MainAxisAlignment.CENTER))
            
        elif page.route == "/notifications":
            notification_screen = get_notification_screen(
                page,
                on_back=lambda: page.go("/home")
            )
            page.add(ft.Row([create_iphone_layout(notification_screen)], alignment=ft.MainAxisAlignment.CENTER))
            
        elif page.route == "/transactions":
            transaction_screen = get_transaction_screen(
                page,
                on_back=lambda: page.go("/home")
            )
            page.add(ft.Row([create_iphone_layout(transaction_screen)], alignment=ft.MainAxisAlignment.CENTER))
            
        
        elif page.route == "/profile":
            profile_screen= get_profile_screen(
                page,
                on_back=lambda: page.go("/home"),
                on_logout=lambda: page.go("/login")
            )
            page.add(ft.Row([create_iphone_layout(profile_screen)], alignment=ft.MainAxisAlignment.CENTER))

    def view_pop(view):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go("/")


# Inicializa o aplicativo
ft.app(target=main)