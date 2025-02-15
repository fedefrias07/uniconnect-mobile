import requests
import flet as ft
from utilidades.apis import get_usuario
from events.publicar import click_en_publicar

def view_home(page: ft.Page):
    page.title = "UniConnect - Menu Principal"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.bgcolor = "#f3f4f6"

    # ---------------- VISTA EXPLORAR ----------------

    def get_explorar_content():
        publicaciones = [
            {"usuario": "fedefrias", "tiempo": "Hace 3 días", "contenido": "Hola facu", "comentarios": 1, "likes": 0, "corazones": 0, "compartidos": 10},
            {"usuario": "fedefrias", "tiempo": "Hace 3 días", "contenido": "probando vacio\nasdasd", "comentarios": 1, "likes": 0, "corazones": 1, "compartidos": 10},
            {"usuario": "Rodrigo", "tiempo": "Hace 26 días", "contenido": "Este es mi primer post\nGoooooood", "comentarios": 3, "likes": 1, "corazones": 1, "compartidos": 10},
            {"usuario": "fedefrias", "tiempo": "Hace 51 días", "contenido": "Funca?\nhola", "comentarios": 3, "likes": 0, "corazones": 1, "compartidos": 10},
        ]

        publicaciones_widgets = []
        for pub in publicaciones:
            publicaciones_widgets.append(
                ft.Container(
                    content=ft.Column([
                        ft.Row([
                            ft.CircleAvatar(content=ft.Text(pub["usuario"][0].upper()), radius=20),
                            ft.Column([
                                ft.Text(pub["usuario"], weight=ft.FontWeight.BOLD),
                                ft.Text(pub["tiempo"], size=12, color="#555"),
                            ], spacing=0),
                        ], spacing=10, alignment=ft.MainAxisAlignment.START),
                        ft.Text(pub["contenido"], size=14),
                        ft.Row([
                            ft.TextButton(f"💬 {pub['comentarios']}", on_click=lambda e: print("Comentario")),
                            ft.TextButton(f"👍 {pub['likes']}", on_click=lambda e: print("Like")),
                            ft.TextButton(f"❤️ {pub['corazones']}", on_click=lambda e: print("Corazón")),
                            ft.TextButton(f"🔄 {pub['compartidos']}", on_click=lambda e: print("Compartir")),
                        ], spacing=10, alignment=ft.MainAxisAlignment.START),
                    ], spacing=5),
                    padding=15,
                    bgcolor="#ffffff",
                    border_radius=10,
                    shadow=ft.BoxShadow(blur_radius=4, spread_radius=0.2, color="#ddd"),
                )
            )

        return ft.Container(
            content=ft.Column([
                ft.Text("Explorar", size=32, weight=ft.FontWeight.BOLD, color="#1C2E40"),
                ft.Text("Descubre nuevas publicaciones y conecta con otros usuarios.", size=18, color="#555"),
                ft.Container(
                    content=ft.ListView(
                        controls=publicaciones_widgets,
                        expand=True,  # Expande para ocupar el espacio disponible
                        spacing=10,  # Espacio entre elementos
                        auto_scroll=False  # No auto-scroll para permitir desplazamiento manual
                    ),
                    height=400,  # Altura máxima del área de scroll
                    bgcolor="#f9f9f9",
                    border_radius=10,
                    padding=10,
                )
            ], alignment=ft.MainAxisAlignment.CENTER),
            padding=30,
            alignment=ft.alignment.center,
            border_radius=12,
            bgcolor="#f3f4f6",
            shadow=ft.BoxShadow(blur_radius=8, spread_radius=0.3, color="#dcdcdc"),
        )

    # ---------------- VISTA PUBLICAR ----------------

    def get_publicar_content():
        def cambiar_seccion(e):
            texto_section.visible = (e.control.text == "Texto")
            imagen_section.visible = not texto_section.visible
            page.update()

        opciones = ft.Row([
            ft.TextButton("Texto", on_click=cambiar_seccion),
            ft.TextButton("Imagen", on_click=cambiar_seccion)
        ], alignment=ft.MainAxisAlignment.CENTER)

        # Dropdown para universidad (suponiendo que haya varias opciones)
        universidad_dropdown = ft.Dropdown(
            options=[
                ft.dropdown.Option("1", text="Da Vinci")
            ],
            hint_text="Selecciona una universidad",
            width=400
        )

        # Dropdown para carrera
        carrera_dropdown = ft.Dropdown(
            options=[
                ft.dropdown.Option("1", text="Analista de sistemas"),
                ft.dropdown.Option("6", text="Cine y Animacion"),
            ],
            hint_text="Selecciona una carrera",
            width=400
        )

        id_usuario = page.session.get("user_id")  # Mantener esto igual

        titulo_input = ft.TextField(label="Título", width=400)

        texto_section = ft.Column([
            ft.TextField(label="Escribe tu publicación", multiline=True, width=400, max_length=300),
        ], visible=True)

        imagen_section = ft.Column([
            ft.FilePicker(on_result=lambda e: print(e.files)),  
            ft.ElevatedButton(
                text="Seleccionar Imagen",
                icon=ft.icons.IMAGE,
                on_click=lambda _: print("Función para subir imagen")
            ),
            ft.Text("Arrastra tu imagen aquí o selecciona un archivo")
        ], visible=False)

        btn_publicar = ft.ElevatedButton(
            "Publicar",
            bgcolor="#007bff",
            color="white",
            on_click=lambda e: click_en_publicar(
                page, id_usuario, universidad_dropdown, carrera_dropdown, titulo_input, texto_section
            )
        )

        return ft.Container(
            content=ft.Column(
                [ft.Text("Crear Publicación", size=28, weight=ft.FontWeight.BOLD),
                opciones, universidad_dropdown, carrera_dropdown, titulo_input, texto_section, imagen_section, btn_publicar],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER
            ),
            padding=30,
            border_radius=12,
            bgcolor="#ffffff",
            shadow=ft.BoxShadow(blur_radius=8, spread_radius=0.3, color="#dcdcdc"),
        )

    # ---------------- VISTA PERFIL ----------------

    def get_perfil_content():
        user_id = page.session.get("user_id")
        username = "Usuario Desconocido"
        email = "Correo Desconocido"
        seguidores = 0
        siguiendo = 0
        publicaciones = []

        if user_id:
            response = get_usuario(user_id)
            if response.status_code == 200:
                data = response.json()
                if data.get("success"):
                    username = data.get("username", "Desconocido")
                    email = data.get("email", "Desconocido")
                    nombre = data.get("nombre", "Desconocido")
                    apellido = data.get("apellido", "Desconocido")
                    foto = data.get("foto", "Desconocido")
                    fecha_creacion = data.get("fecha_creacion", "Desconocido")
                    seguidores = data.get("seguidores", 0)
                    siguiendo = data.get("siguiendo", 0)
                    publicaciones = data.get("publicaciones", [])

        avatar = ft.Image(
            src=f"https://uniconnect.com.ar/{foto}",
            width=100,
            height=100,
            border_radius=50,
            error_content=ft.Icon(ft.icons.PERSON, size=50, color="black")
        )

        uniconnect = ft.Text("UniConnect", size=18, weight=ft.FontWeight.BOLD)
        menu = ft.Icon(ft.Icons.MENU, size=35, color="black")

        container_perfil = ft.Row([uniconnect, menu], alignment=ft.MainAxisAlignment.SPACE_BETWEEN, expand=True)

        banner = ft.Container(
            bgcolor="#007bff",
            height=120,
            expand=True,
            border_radius=ft.border_radius.only(top_left=20, top_right=20)
        )

        user_info = ft.Column([
            ft.Row([
                avatar,
                ft.Column([
                    ft.Text(username, size=20, weight=ft.FontWeight.BOLD),
                    ft.Text(email, size=14),
                    ft.Row([
                        ft.Text(nombre, size=14),
                        ft.Text(apellido, size=14),
                    ], spacing=5),
                    ft.Text(fecha_creacion, size=14),
                    ft.Text(f"{len(publicaciones)} Publicaciones | {seguidores} Seguidores | {siguiendo} Seguidos", size=12)
                ], spacing=2)
            ], spacing=20, alignment=ft.MainAxisAlignment.CENTER)
        ], spacing=10)

        publicaciones_lista = ft.Column([
            ft.Container(
                content=ft.Column([
                    ft.Text(pub["titulo"], weight=ft.FontWeight.BOLD, size=16),
                    ft.Text(pub["contenido"], size=14, color="#444"),
                ]),
                padding=15,
                bgcolor="#ffffff",
                border_radius=8,
                shadow=ft.BoxShadow(blur_radius=4, spread_radius=0.2, color="#ddd"),
            ) for pub in publicaciones
        ], spacing=10)

        def on_logout_click(e):
            page.session.clear()
            snack_bar = ft.SnackBar(ft.Text("Has cerrado sesión exitosamente."))
            page.overlay.append(snack_bar)
            snack_bar.open = True
            page.update()
            page.go("/login")

        logout_button = ft.ElevatedButton("Cerrar sesión", bgcolor="#dc3545", color="white", on_click=on_logout_click)

        return ft.Container(
            content=ft.Column([
                container_perfil,
                banner,
                ft.Container(content=user_info, padding=20),
                ft.Text("Publicaciones", size=18, weight=ft.FontWeight.BOLD),
                publicaciones_lista if publicaciones else ft.Text("Aún no hay publicaciones."),
                logout_button
            ], horizontal_alignment=ft.CrossAxisAlignment.CENTER),
            padding=10,
            border_radius=8,
            bgcolor="#f8f9fa"
        )

    # ---------------- CONFIGURACIÓN DE LA NAVEGACIÓN ----------------

    dynamic_container = ft.ResponsiveRow()

    def update_content(index):
        dynamic_container.controls.clear()
        if index == 0:
            dynamic_container.controls.append(get_explorar_content())
        elif index == 1:
            dynamic_container.controls.append(get_publicar_content())
        elif index == 2:
            dynamic_container.controls.append(get_perfil_content())
        page.update()

    navigation_bar = ft.NavigationBar(
        destinations=[
            ft.NavigationBarDestination(icon=ft.Icons.EXPLORE, label="Explorar"),
            ft.NavigationBarDestination(icon=ft.Icons.POST_ADD, label="Publicar"),
            ft.NavigationBarDestination(icon=ft.Icons.PERSON, label="Perfil"),
        ],
        on_change=lambda e: update_content(e.control.selected_index),
    )

    update_content(0)

    return ft.View(
        "/home",
        [
            navigation_bar,
            dynamic_container,
        ],
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        vertical_alignment=ft.MainAxisAlignment.START,
    )
