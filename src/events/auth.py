import flet as ft
from utilidades.apis import login_api, registro_api


# Manejo del evento de inicio de sesión
def click_en_login(page, email_input, password_input):
    email = email_input.value
    password = password_input.value

    if not email or not password:
        snack_bar = ft.SnackBar(ft.Text("Por favor, completa todos los campos."))
        page.overlay.append(snack_bar)
        snack_bar.open = True
        page.update()
        return

    response = login_api(email, password)

    if isinstance(response, dict) and "error" in response:
        snack_bar = ft.SnackBar(ft.Text(f"Error de conexión: {response['error']}"))
    elif response.status_code == 200:
        data = response.json()
        if data.get("success"):
            page.session.set("user_id", data["user_id"])
            snack_bar = ft.SnackBar(ft.Text("Inicio de sesión exitoso."))
            page.go("/home")
        else:
            snack_bar = ft.SnackBar(ft.Text(data.get("message", "Error desconocido.")))
    else:
        snack_bar = ft.SnackBar(ft.Text("Correo o contraseña incorrectos."))

    page.overlay.append(snack_bar)
    snack_bar.open = True
    page.update()



# Manejo del evento de registro
import flet as ft

def click_en_registrar(page, name_input, apellido_input, username_input, email_input, password_input, confirm_password_input):
    username = username_input.value
    email = email_input.value
    password = password_input.value
    name = name_input.value
    apellido = apellido_input.value
    confirmar_contrasena = confirm_password_input.value

    if not username or not email or not password:
        snack_bar = ft.SnackBar(ft.Text("Por favor, completa todos los campos."))
        page.overlay.append(snack_bar)
        snack_bar.open = True
        page.update()
        return

    response, mensaje = registro_api(name, apellido, username, email, password, confirmar_contrasena)

    snack_bar_text = mensaje if response is not None else "Error de conexión."
    
    if response and response.status_code in (200, 201) and response.json().get("success"):
        snack_bar_text = "Registro exitoso."
        page.go("/login")

    snack_bar = ft.SnackBar(ft.Text(snack_bar_text))
    page.overlay.append(snack_bar)
    snack_bar.open = True
    page.update()



    