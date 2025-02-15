import flet as ft
from views.login import login_view
from views.registro import register_view
from views.home import view_home


def main(page: ft.Page):
    page.title = "UniConnect App"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER


    # Esta función maneja el cambio de rutas
    def route_change(e):
        print(f"Route change: {e.route}")
        
        # Limpiar las vistas y luego añadir la vista correspondiente a la ruta
        page.views.clear()

        if page.route == "/login":
            page.views.append(login_view(page))

        elif page.route == "/register":
            page.views.append(register_view(page))

        else:
            page.views.append(view_home(page))

        page.update()

    page.on_route_change = route_change

    # Llamar a la ruta inicial
    #page.go("/login")  # Redirige a la vista de login cuando se inicia la app

    # Inicializamos la primera vista según la ruta actual
    page.go("/login")

ft.app(target=main)


