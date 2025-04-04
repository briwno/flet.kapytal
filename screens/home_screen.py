import flet as ft

def get_home_screen(page: ft.Page, on_logout: callable) -> ft.Container:
    return ft.Container(
        width=400,
        height=830,
        bgcolor="#000000",  # Fundo preto
        border_radius=ft.border_radius.all(40),
        padding=ft.padding.all(0),
        content=ft.Stack(
            [
                # Cabeçalho dourado superior
                ft.Container(
                    width=400,
                    height=250,
                    bgcolor="#e4b849",  # Dourado
                    border_radius=ft.BorderRadius(
                        top_left=40,
                        top_right=40,
                        bottom_left=30,
                        bottom_right=30,
                    ),
                    padding=ft.padding.all(40),
                    content=ft.Column(
                        [
                            ft.Text(
                                "Olá, Bem-vindo de volta {user}",
                                size=22,
                                weight=ft.FontWeight.BOLD,
                                color=ft.colors.BLACK,
                            ),
                            ft.Row(
                                [
                                    ft.Column(
                                        [
                                            ft.Text("Saldo Total", size=14, color=ft.colors.BLACK),
                                            ft.Text("R$ 7.783,00", size=24, weight=ft.FontWeight.BOLD, color=ft.colors.BLACK),
                                        ],
                                    ),
                                    ft.Column(
                                        [
                                            ft.Text("Despesas Totais", size=14, color=ft.colors.BLACK),
                                            ft.Text("- R$ 1.187,40", size=24, weight=ft.FontWeight.BOLD, color="#3E83FF"),
                                        ],
                                    ),
                                ],
                                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                            ),
                        ],
                    ),
                ),
                # Corpo principal
                ft.Container(
                    width=400,
                    height=630,
                    bgcolor=ft.colors.BLACK,  # Branco translúcido
                    border_radius=ft.border_radius.all(50),
                    padding=ft.padding.symmetric(horizontal=20, vertical=30),
                    content=ft.Column(
                        [
                            # Seção de economia e receita
                            ft.Container(
                                bgcolor="#e4b849",
                                border_radius=20,
                                padding=ft.padding.all(15),
                                content=ft.Row(
                                    [
                                        ft.Icon(name=ft.icons.SAVINGS, color=ft.colors.BLACK, size=40),
                                        ft.Column(
                                            [
                                                ft.Text("Economia em Metas", color=ft.colors.BLACK, size=16),
                                                ft.Text("Receita da Última Semana", color=ft.colors.BLACK, size=14),
                                                ft.Text("R$ 4.000,00", color=ft.colors.BLACK, size=18, weight=ft.FontWeight.BOLD),
                                            ],
                                        ),
                                    ],
                                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                                ),
                            ),
                            ft.Row(
                                [
                                    ft.TextButton("Diário", on_click=lambda _: print("Diário")),
                                    ft.TextButton("Semanal", on_click=lambda _: print("Semanal")),
                                    ft.TextButton("Mensal", on_click=lambda _: print("Mensal"), style=ft.ButtonStyle(bgcolor="#e4b849", color=ft.colors.BLACK)),
                                ],
                                alignment=ft.MainAxisAlignment.SPACE_AROUND,
                            ),
                            # Lista de transações
                            ft.Column(
                                [
                                    ft.ListTile(
                                        leading=ft.Icon(ft.icons.WORK, color=ft.colors.BLUE),
                                        title=ft.Text("Salário", size=16, weight=ft.FontWeight.BOLD),
                                        subtitle=ft.Text("+ Mensal - R$ 4.000,00"),
                                    ),
                                    ft.ListTile(
                                        leading=ft.Icon(ft.icons.SHOPPING_CART, color=ft.colors.RED),
                                        title=ft.Text("Mercado", size=16, weight=ft.FontWeight.BOLD),
                                        subtitle=ft.Text("- Compras - R$ 100,00"),
                                    ),
                                    ft.ListTile(
                                        leading=ft.Icon(ft.icons.HOME, color=ft.colors.ORANGE),
                                        title=ft.Text("Aluguel", size=16, weight=ft.FontWeight.BOLD),
                                        subtitle=ft.Text("- Moradia - R$ 674,40"),
                                    ),
                                ],
                            ),
                        ],
                    ),
                    margin=ft.margin.only(top=200),
                ),
                # Barra de navegação inferior
                ft.Container(
                    width=300,
                    height=60,
                    bgcolor='#f7d679',
                    border_radius=ft.border_radius.only(
                        top_left=40,
                        top_right=40,
                        bottom_left=40,
                        bottom_right=40,
                        
                    ),
                    padding=ft.padding.symmetric(horizontal=20),
                    content=ft.Row(
                        [
                            ft.IconButton(icon=ft.icons.HOME, icon_color=ft.colors.BLACK),
                           
                            ft.IconButton(icon=ft.icons.SWAP_HORIZ, icon_color=ft.colors.BLACK),
                            ft.IconButton(icon=ft.icons.LIBRARY_BOOKS, icon_color=ft.colors.BLACK),
                            ft.IconButton(icon=ft.icons.PERSON, icon_color=ft.colors.BLACK),
                            ft.IconButton(icon=ft.icons.LOGOUT, icon_color=ft.colors.BLACK, on_click=lambda _: on_logout()),
                        ],
                        alignment=ft.MainAxisAlignment.SPACE_AROUND,
                    ),
                    alignment=ft.alignment.center,
                    margin=ft.margin.only(top=750, left=50),
                ),
            ]
        ),
    )
