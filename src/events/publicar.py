import requests
import flet as ft
from utilidades.apis import publicar_api


# Manejo del evento de publicación
def click_en_publicar(page, usuario_id, universidad_dropdown, carrera_dropdown, titulo_input, texto_section):
    id_usuario = usuario_id
    id_universidad = universidad_dropdown.value if universidad_dropdown.value else None
    id_carrera = carrera_dropdown.value if carrera_dropdown.value else None
    titulo = titulo_input.value

    # Acceder al TextField dentro de texto_section
    texto_field = texto_section.controls[0]  # Accede al primer elemento dentro del Column
    texto = texto_field.value if isinstance(texto_field, ft.TextField) else None


    # Validar que los campos obligatorios no estén vacíos
    if not titulo:
        snack_bar = ft.SnackBar(ft.Text("El título es obligatorio."))
        page.overlay.append(snack_bar)
        snack_bar.open = True
        page.update()
        return

    # Enviar los datos al endpoint
    response = publicar_api(id_usuario, id_universidad, id_carrera, titulo, texto)

    # Manejo de la respuesta del servidor
    if isinstance(response, dict) and "error" in response:
        snack_bar = ft.SnackBar(ft.Text(f"Error de conexión: {response['error']}"))
    elif response.get("mensaje") == "Publicación creada exitosamente":
        snack_bar = ft.SnackBar(ft.Text("Publicación realizada con éxito."))
        page.go("/home")  # Redirige a la página principal o de publicaciones
    else:
        snack_bar = ft.SnackBar(ft.Text("Error al publicar."))

    page.overlay.append(snack_bar)
    snack_bar.open = True
    page.update()


