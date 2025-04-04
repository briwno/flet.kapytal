import flet as ft

def create_iphone_layout(content: ft.Control) -> ft.Stack:
    """
    Cria o layout do iPhone com moldura e conteúdo interativo.
    """
    return ft.Stack(
        [
            content,  # Conteúdo interativo
            ft.TransparentPointer(  # Permite que eventos de clique passem através da moldura
                content=ft.Image(
                    src="assets/iphone-moldure.png",
                    width=430,
                    height=932,
                    fit=ft.ImageFit.CONTAIN,
                ),
            ),
        ],
        alignment=ft.alignment.center,
        expand=True,
    )