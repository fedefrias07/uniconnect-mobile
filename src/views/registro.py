import flet as ft
from events.auth import click_en_registrar


def register_view(page: ft.Page):

    # Títulos
    page.title = "UniConnect Registro"
    title = ft.Text("UNICONNECT", size=30, weight=ft.FontWeight.BOLD, color="#1C2E40")
    subtitle = ft.Text("Crear una cuenta", size=18, weight=ft.FontWeight.W_600, color="#212529")


    # Inputs
    nombre_input = ft.TextField( label="Nombre", width=300, height=45, color="black", border_color="#dfdfdf")
    apellido_input = ft.TextField( label="Apellido", width=300, height=45, color="black", border_color="#dfdfdf")
    username_input = ft.TextField( label="Nombre de usuario", width=300, height=45, color="black", border_color="#dfdfdf")
    email_input = ft.TextField( label="Correo electrónico", width=300, height=45, color="black", border_color="#dfdfdf")
    password_input = ft.TextField( label="Contraseña", password=True, can_reveal_password=True, width=300, height=45, color="black", border_color="#dfdfdf")
    confirm_password_input = ft.TextField(label="Confirmar contraseña", password=True, can_reveal_password=True, width=300, height=45, color="black", border_color="#dfdfdf")

    # Botones
    register_button = ft.ElevatedButton(
        "Registrar",
        width=300,
        height=45,
        style=ft.ButtonStyle(bgcolor="#1C2E40", color="white",
                              shape=ft.RoundedRectangleBorder(radius=8)),
        on_click=lambda e: click_en_registrar(page, nombre_input, apellido_input, username_input, email_input, password_input, confirm_password_input)  # Llamamos la función importada nombre, apellido, nombre_usuario, correo, contrasena, confirmar_contrasena
    )

    back_button = ft.TextButton(
        "Volver al inicio",
        on_click=lambda _: page.go("/login"),  # Redirigir a la vista de login
    )

    # Contenedor principal
    container = ft.Container(
        content=ft.Column(
            [
                title,
                subtitle,
                nombre_input,
                apellido_input,
                username_input,
                email_input,
                password_input,
                confirm_password_input,
                register_button,
                back_button,
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

    # Crear y retornar la vista de registro
    return ft.View(
        "/register",  # Ruta de la vista
        [
            container  # Contenedor con los controles de registro
        ],
        bgcolor=ft.Colors.WHITE,  # Cambiar el color de fondo
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        vertical_alignment=ft.MainAxisAlignment.CENTER
    )
