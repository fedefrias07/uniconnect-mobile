import requests


def login_api(email, password):
    """
    Enviar datos de inicio de sesión al endpoint Flask.
    """
    try:
        response = requests.post(
            "https://uniconnect.com.ar/api/login",  # URL del endpoint Flask
            json={"correo": email, "contrasena": password},  # Datos en formato JSON
        )
        return response
    except requests.RequestException as e:
        return {"error": str(e)}

    
def registro_api(nombre, apellido, nombre_usuario, correo, contrasena, confirmar_contrasena):
    """
    Enviar los datos de registro al endpoint Flask.
    """
    try:
        response = requests.post(
            "https://uniconnect.com.ar/api/registro",  # URL del endpoint de registro
            json={
                "nombre": nombre,
                "apellido": apellido,
                "nombre_usuario": nombre_usuario,
                "correo": correo,
                "contrasena": contrasena,
                "confirmar_contrasena": confirmar_contrasena,
            },
        )
        print("Respuesta del servidor:", response.status_code, response.text)  # Agregado para depurar

        # Intentar extraer solo el mensaje si la respuesta es JSON válida
        mensaje = response.json().get("message", "Error desconocido.") if response.status_code != 200 else "Registro exitoso."

        return response, mensaje
    except requests.RequestException as e:
        return {"error": str(e)}


def get_usuario(user_id):

    try:
        response = requests.get(f"https://uniconnect.com.ar/api/usuario/{user_id}")

        return response
    except Exception as e:
        print(f"Error al obtener los datos del usuario: {e}")
        
def obtener_publicaciones(usuario_id):
    """
    Consultar el endpoint Flask para obtener las publicaciones asociadas al usuario.
    :param usuario_id: ID del usuario para filtrar las publicaciones.
    :return: Lista de publicaciones en JSON o un mensaje de error.
    """
    try:
        # URL del endpoint Flask
        url = "https://uniconnect.com.ar/api/publicaciones"
        
        # Parámetros (se pasa usuario_id en la query string)
        params = {"usuario_id": usuario_id}

        # Solicitar datos al servidor
        response = requests.get(url, params=params)

        # Comprobar si la respuesta es válida
        if response.status_code == 200:
            return response.json()  # Devuelve las publicaciones
        else:
            print(f"Error al obtener publicaciones: {response.status_code} {response.text}")
            return {"error": "No se pudieron obtener las publicaciones"}
    except requests.RequestException as e:
        return {"error": f"Error en la conexión: {str(e)}"}


def publicar_api(id_usuario, id_universidad, id_carrera, titulo, texto, imagen_path=None):
    """
    Enviar los datos de publicación al endpoint Flask.
    """
    try:
        url = "https://uniconnect.com.ar/api/publicar"  # URL del endpoint
        
        # Datos en formato JSON
        data = {
            "id_usuario": id_usuario,
            "id_universidad": id_universidad,
            "id_carrera": id_carrera,
            "titulo": titulo,
            "texto": texto
        }

        # Si hay una imagen, usar multipart/form-data
        files = None
        if imagen_path:
            with open(imagen_path, "rb") as img:
                files = {"imagen": img}
                response = requests.post(url, data=data, files=files)
        else:
            response = requests.post(url, json=data)

        print("Respuesta del servidor:", response.status_code, response.text)  # Para depuración
        return response.json()  # Devuelve la respuesta en JSON

    except requests.RequestException as e:
        return {"error": str(e)}





