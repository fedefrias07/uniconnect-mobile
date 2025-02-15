import flet as ft
from events.auth import click_en_login

def login_view(page: ft.Page):
    # Títulos
    page.title = "UniConnect Login"
    title = ft.Text("UNICONNECT", size=30, weight=ft.FontWeight.BOLD, color="#1C2E40")
    subtitle = ft.Text("Iniciar sesión", size=18, weight=ft.FontWeight.W_600, color="#212529")

    # Inputs
    email_input = ft.TextField(label="Correo electrónico", width=300, height=45, color="black", border_color="#dfdfdf" )
    password_input = ft.TextField(label="Contraseña", password=True, can_reveal_password=True, width=300, height=45, color="black", border_color="#dfdfdf")

    # Botones
    login_button = ft.ElevatedButton(
        "Iniciar sesión", width=300, height=45, style=ft.ButtonStyle(bgcolor="#1C2E40", color="white", shape=ft.RoundedRectangleBorder(radius=8)), 
        on_click=lambda e: click_en_login(page, email_input, password_input)  # Llamamos la función importada
    )

    forgot_password = ft.TextButton(
        "¿Olvidaste tu contraseña?", style=ft.ButtonStyle(
            color="#555555"  # Aquí defines el color personalizado
        ),
        on_click=lambda _: print("Recuperar contraseña clickeado"),
    )

    register_button = ft.OutlinedButton(
        "Registrarse",
        width=300,
        height=45,
        style=ft.ButtonStyle(
            color="black",
            shape=ft.RoundedRectangleBorder(radius=10),  # Border radius de 12 píxeles
            side=ft.BorderSide(1, "#1C2E40"),
        ),
        # on_click=lambda _: page.go("/register"),  # Redirige a la vista de registro
        on_click=lambda _: (print("Navegando a /register"), page.go("/register")),  # Depuración
    )

    google_button = ft.ElevatedButton(
        "Sign up with Google",
        width=300,
        style=ft.ButtonStyle(
            bgcolor="#4285F4",
            color="white"
        ),
    )

    # Contenedor principal con todos los controles
    container = ft.Container(
        content=ft.Column(
            [
                title,
                subtitle,
                email_input,
                password_input,
                login_button,
                forgot_password,
                register_button,
                google_button,
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=10,
        ),
        padding=20,
        width=350,
        alignment=ft.alignment.center,
        border_radius=ft.border_radius.all(10),
        bgcolor="white",
        shadow=ft.BoxShadow(
            blur_radius=5, spread_radius=0.2, color="#cfcfcf", offset=ft.Offset(0, 0)
        ),
    )

    # Crear la vista y retornar
    return ft.View(
        "/login",  # Ruta de la vista
        [
            container  # Contenedor principal con los controles
        ],
        bgcolor=ft.Colors.WHITE,  # Cambiar el color de fondo
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        vertical_alignment = ft.MainAxisAlignment.CENTER

    )
