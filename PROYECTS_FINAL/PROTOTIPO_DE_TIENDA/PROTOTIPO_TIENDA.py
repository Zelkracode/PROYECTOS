
##### TIENDA ONLINE 'MiSuperSuper🛒'



##### IMPORTACIONES
import os
import re
from dotenv import load_dotenv
import flet as ft
from supabase import create_client, Client
import hashlib


load_dotenv()

URL_SUPABASE = os.getenv("SUPABASE_URL")
KEY_SUPABASE = os.getenv("SUPABASE_KEY")

# Configuración de Supabase
if not URL_SUPABASE or not KEY_SUPABASE:
    print("Error: No se encontraron las credenciales en el archivo .env")
else:
    supabase = create_client(URL_SUPABASE, KEY_SUPABASE)

def hashear_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def es_correo_valido(correo):
    
    patron = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(patron, correo) is not None

def es_telefono_valido(telefono):
    
    return telefono.isdigit() and 8 <= len(telefono) <= 15

def obtener_negocios():
   
    res = supabase.table("vendedores").select("nombre_negocio, direccion_negocio").execute()
    return res.data


#### REGISTRO DE USUARIO (Actualizado para Supabase)
def registro_usuario_en_nube(nombre, usuario, correo, telefono, password):
    pass_hash = hashear_password(password)
    supabase.table("usuarios").insert({
        "nombre_completo": nombre,
        "nombre_usuario": usuario,
        "correo_usuario": correo,
        "telefono_usuario": telefono,
        "password": pass_hash
    }).execute()

#### REGISTRO DE VENDEDOR (Actualizado para Supabase)
def registro_vendedor_en_nube(propietario, negocio, direccion, correo, telefono, password):
    pass_hash = hashear_password(password)
    supabase.table("vendedores").insert({
        "nombre_propetario": propietario,
        "nombre_negocio": negocio,
        "direccion_negocio": direccion,
        "correo_vendedor": correo,
        "telefono_vendedor": telefono,
        "password": pass_hash
    }).execute()

#### EXCEPCIONES

def correo_ya_existe(correo):
    
    res_u = supabase.table('usuarios').select('correo_usuario').eq('correo_usuario', correo).execute()

    res_v = supabase.table("vendedores").select("correo_vendedor").eq("correo_vendedor", correo).execute()
    
    return len(res_u.data) > 0 or len(res_v.data) > 0


def mostrar_mensaje_login(page, texto, color=ft.Colors.RED_400):
    snack = ft.SnackBar(
        content=ft.Text(texto, color=ft.Colors.WHITE),
        bgcolor=color,
        action="OK", # Botón opcional para cerrar
    )
    page.overlay.append(snack)
    snack.open = True
    page.update()
    
def mostrar_mensaje_resgitro(page, texto, color=ft.Colors.RED_400):
    snack = ft.SnackBar(
        content=ft.Text(texto, color=ft.Colors.WHITE),
        bgcolor=color,
        action="OK", # Botón opcional para cerrar
    )
    page.overlay.append(snack)
    snack.open = True
    page.update()
    


#### LOGIIINNN
    
def login(page):
    page.controls.clear()
    

    intento_correo = ft.TextField(
        label='Correo',
        width=300,
        color=ft.Colors.WHITE,
        border_color=ft.Colors.WHITE,
        label_style=ft.TextStyle(color=ft.Colors.WHITE),
        focused_border_color=ft.Colors.BLUE_200
    )
    
    intento_contraseña = ft.TextField(
        label='Contraseña',
        password=True,
        can_reveal_password=True,
        width=200,
        color=ft.Colors.WHITE,
        border_color=ft.Colors.WHITE,
        label_style=ft.TextStyle(color=ft.Colors.WHITE),
        focused_border_color=ft.Colors.BLUE_200
    )
    
    def intento_login(e):
        if not intento_correo.value or not intento_contraseña.value:
            print('Error: Todos los campos son obligatorios')
            return
        
        try:
            password_hasheada = hashear_password(intento_contraseña.value)
            
            res_v = supabase.table("vendedores").select("*").eq("correo_vendedor", intento_correo.value).eq("password", password_hasheada).execute()
            
            if res_v.data:
                datos = res_v.data[0]
                inicio_logeado_vendedor(page)
                return

            # 2. Si no es vendedor, intentar buscar en Usuarios
            # Dentro de la función login(page), en el apartado de usuarios:
            res_u = supabase.table("usuarios").select("*").eq("correo_usuario", intento_correo.value).eq("password", password_hasheada).execute()
            
            if res_u.data:
                datos_usuario = res_u.data[0]
                nombre_usuario = datos_usuario.get("nombre_completo", "Usuario") # Extrae el nombre
                
                mostrar_mensaje_login(page, f"¡Bienvenido {nombre_usuario}!", ft.Colors.GREEN_400)
                
                # PASAMOS EL NOMBRE AQUÍ
                inicio_logeado_usuario(page, nombre_usuario) 
            else:
                print('Error: Credenciales incorrectas')
                
        except Exception as ex:
            print(f"Error en el login: {ex}")        

    page.add(
        ft.Stack(
            expand=True,
            controls=[
            ft.Container(
                expand=True,
                gradient=ft.LinearGradient(
                    begin=ft.Alignment(0, .1),
                    end=ft.Alignment(0, 1),
                    colors=['#0f2027', '#203a43', '#2c5364']
                )
            ),
            
            ft.Container(
                expand=True,
                alignment=ft.Alignment(0, 0),
                content=
                    ft.Column(
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        alignment=ft.MainAxisAlignment.CENTER,
                        spacing=40,
                        controls=[
                        ft.Column(
                            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                            alignment=ft.MainAxisAlignment.CENTER,
                            spacing=10,
                            controls=[
                            ft.Text('INGRESE SUS CREDENCIALES',
                                    size=30,
                                    weight='bold',
                                    color=ft.Colors.WHITE
                                    ),
                            ft.Text('Gracias por elegir MiSuperSuper',
                                    size=16,
                                    weight='bold',
                                    color=ft.Colors.WHITE
                                    ),
                                ]     
                            ),
                        ft.Column(
                            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                            alignment=ft.MainAxisAlignment.CENTER,
                            spacing=10,
                            controls=[
                                intento_correo,
                                intento_contraseña
                            ]
                        ),
                        
                        ft.FilledButton(
                            'Ingresar',
                            color=ft.Colors.WHITE,
                            bgcolor=ft.Colors.BLUE_GREY_400,
                            on_click=intento_login
                            ),
                        ft.TextButton(
                            'Volver',
                            on_click=lambda _: main(page)
                        )
                    ]
                )
            ) 
        ]            
    )
)   




### LOGEO DE VENDEDOR

def inicio_logeado_vendedor(page):
    pass



#### LOGEO DE USUARIO

def inicio_logeado_usuario(page, nombre):
    page.controls.clear()
    
    # --- Componentes de la Interfaz ---
    
    # 1. Barra de búsqueda (típica de apps de delivery)
    busqueda = ft.TextField(
        hint_text="¿Qué se te antoja hoy?",
        prefix_icon=ft.Icons.SEARCH,
        border_radius=15,
        bgcolor=ft.Colors.WHITE,
        color=ft.Colors.BLACK,
        height=45,
        expand=True
    )

    # 2. Generador de "Cards" para cada negocio
    def crear_card_negocio(datos_vendedor):
        return ft.Container(
            content=ft.Column([
                ft.Icon(ft.Icons.STOREFRONT, size=40, color=ft.Colors.BLUE_GREY_700),
                ft.Text(datos_vendedor['nombre_negocio'], weight="bold", size=16),
                ft.Text(datos_vendedor['direccion_negocio'], size=12, color=ft.Colors.GREY_700),
                ft.ElevatedButton("Ver productos", color=ft.Colors.WHITE, bgcolor=ft.Colors.ORANGE_700)
            ], alignment=ft.MainAxisAlignment.CENTER, horizontal_alignment=ft.CrossAxisAlignment.CENTER),
            width=160,
            height=180,
            bgcolor=ft.Colors.WHITE,
            border_radius=20,
            padding=10,
            shadow=ft.BoxShadow(blur_radius=10, color=ft.Colors.with_opacity(0.2, ft.Colors.BLACK))
        )

    # Obtenemos los datos reales de Supabase
    lista_negocios_db = obtener_negocios()
    
    # Creamos la fila de negocios (puedes usar un Row con scroll o un GridView)
    fila_negocios = ft.Row(
        scroll=ft.ScrollMode.ALWAYS,
        controls=[crear_card_negocio(n) for n in lista_negocios_db]
    )

    # --- Construcción del Layout ---
    page.add(
        ft.Container(
            expand=True,
            gradient=ft.LinearGradient(
                begin=ft.Alignment(0, -1),
                end=ft.Alignment(0, 1),
                colors=['#2c3e50', '#4ca1af']
            ),
            padding=20,
            content=ft.Column([
                # Header: Perfil y Config
                ft.Row([
                    ft.Text(f"Hola, {nombre}", size=20, weight="bold", color=ft.Colors.WHITE),
                    ft.Row([
                        ft.IconButton(ft.Icons.PERSON, icon_color=ft.Colors.WHITE),
                        ft.IconButton(ft.Icons.SETTINGS, icon_color=ft.Colors.WHITE),
                    ])
                ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
                
                ft.Text("Explora MiSuperSuper", size=28, weight="bold", color=ft.Colors.WHITE),
                
                # Buscador
                ft.Row([busqueda]),
                
                ft.Divider(height=20, color=ft.Colors.TRANSPARENT),
                
                # Sección de Negocios
                ft.Text("Tiendas disponibles", size=18, weight="bold", color=ft.Colors.WHITE),
                fila_negocios,
                
                # Puedes añadir más secciones como "Ofertas" o "Categorías"
            ], scroll=ft.ScrollMode.AUTO)
        )
    )
    page.update()




##### USUARIOS

def crear_usuario(page):
    page.controls.clear()
    
    # Definimos los campos aquí para que sea más limpio
    input_nombre = ft.TextField(
        label='Nombre completo',
        width=300,
        color=ft.Colors.WHITE,
        border_color=ft.Colors.WHITE,
        label_style=ft.TextStyle(color=ft.Colors.WHITE),
        focused_border_color=ft.Colors.BLUE_200
    )
    
    input_usuario = ft.TextField(
        label='Nombre de usuario',
        width=300,
        color=ft.Colors.WHITE,
        border_color=ft.Colors.WHITE,
        label_style=ft.TextStyle(color=ft.Colors.WHITE),
        focused_border_color=ft.Colors.BLUE_200
    )
    
    input_correo = ft.TextField(
        label="Correo",
        width=300,
        color=ft.Colors.WHITE,
        border_color=ft.Colors.WHITE,
        label_style=ft.TextStyle(color=ft.Colors.WHITE),
        focused_border_color=ft.Colors.BLUE_200
    )
    
    input_telefono= ft.TextField(
        label='Telefono',
        keyboard_type=ft.KeyboardType.NUMBER,
        input_filter=ft.InputFilter(allow=True, regex_string=r"[0-9]", replacement_string=""),
        width=300,
        color=ft.Colors.WHITE,
        border_color=ft.Colors.WHITE,
        label_style=ft.TextStyle(color=ft.Colors.WHITE),
        focused_border_color=ft.Colors.BLUE_200
    )

    input_contraseña = ft.TextField(
        label='Contraseña',
        password=True,
        can_reveal_password=True,
        width=300,
        color=ft.Colors.WHITE,
        border_color=ft.Colors.WHITE,
        label_style=ft.TextStyle(color=ft.Colors.WHITE),
        focused_border_color=ft.Colors.BLUE_200
    )
    
    #### REGISTRO EN DB
    
    def registro_en_db(e):
        if not all([input_nombre.value, input_usuario.value, input_correo.value, input_telefono.value, input_contraseña.value]):
            mostrar_mensaje_resgitro(page, "Error: Todos los campos son obligatorios", ft.Colors.RED_400)
            return

        if not es_correo_valido(input_correo.value):
            mostrar_mensaje_resgitro(page, "Formato de correo no válido (ej: usuario@correo.com)", ft.Colors.ORANGE_700)
            return
        
        if not es_telefono_valido(input_telefono.value):
            mostrar_mensaje_resgitro(page, "El teléfono debe contener solo números (8-15 dígitos)", ft.Colors.ORANGE_700)
            return
        
        
        if correo_ya_existe(input_correo.value):
            mostrar_mensaje_resgitro(page, "Este correo ya está registrado", ft.Colors.ORANGE_700)
            return
        

        
        try:
            # 2. VALIDACIÓN
            registro_usuario_en_nube(
                input_nombre.value, 
                input_usuario.value, 
                input_correo.value, 
                input_telefono.value, 
                input_contraseña.value
            )
            mostrar_mensaje_resgitro(page, '¡Registro de cuenta exitoso!', ft.Colors.GREEN_400)
            main(page)
            

        except Exception as ex:
            print(f'Error inesperado: {ex}')


    page.add(
        ft.Stack(
            expand=True,
            controls=[
                # CAPA 1: EL FONDO
                ft.Container(
                    expand=True,
                    gradient=ft.LinearGradient(
                        begin=ft.Alignment(0, -1),
                        end=ft.Alignment(0, 1),
                        colors=['#0f2027', '#203a43', '#2c5364']
                    ),
                ),
                
                # CAPA 2: EL CONTENIDO (Todo en una sola columna central)
                ft.Container(
                    expand=True,
                    alignment=ft.Alignment(0, 0), # Esto centra la columna en la pantalla
                    content=ft.Column(
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        alignment=ft.MainAxisAlignment.CENTER,
                        spacing=30, # Espacio entre el bloque de texto y los inputs
                        controls=[
                            # Sub-columna para los textos
                            ft.Column(
                                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                spacing=100,
                                controls=[
                                    ft.Text('REGISTRO DE USUARIO', 
                                            size=30,
                                            weight='bold',
                                            color=ft.Colors.WHITE
                                            ),
                                    ft.Text('Recuerda llenar tus datos correctamente',
                                            size=16,
                                            weight='bold',
                                            color=ft.Colors.WHITE
                                            ),
                                ]
                            ),
                            
                            # Sub-columna para los inputs (Aquí es donde deben ir para que salgan abajo)
                            ft.Column(
                                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                spacing=10,
                                controls=[
                                    input_nombre,
                                    input_usuario,
                                    input_correo,
                                    input_telefono,
                                    input_contraseña,
                                    ft.FilledButton(
                                        'Finalizar Registro',
                                        bgcolor=ft.Colors.BLUE_GREY_500,
                                        width=300,
                                        on_click=registro_en_db 
                                    ),
                                    ft.TextButton(
                                        'Volver',
                                        on_click=lambda _: main(page)
                                    )
                                ]
                            )
                        ]
                    )
                ),
            ]
        )
    )
    page.update()
            


#### REGISTRO DE VENDEDOR
            
def crear_vendedor(page):
    page.controls.clear()
    
    
    input_propetario = ft.TextField(
        label='Nombre del propetario',
        color=ft.Colors.WHITE,
        border_color=ft.Colors.WHITE,
        label_style=ft.TextStyle(color=ft.Colors.WHITE),
        focused_border_color=ft.Colors.BLUE_200
    )
    
    input_negocio = ft.TextField(
        label='Nombre del negocio',
        color=ft.Colors.WHITE,
        border_color=ft.Colors.WHITE,
        label_style=ft.TextStyle(color=ft.Colors.WHITE),
        focused_border_color=ft.Colors.BLUE_200
    )
    
    input_direccion = ft.TextField(
        label='Dirección',
        color=ft.Colors.WHITE,
        border_color=ft.Colors.WHITE,
        label_style=ft.TextStyle(color=ft.Colors.WHITE),
        focused_border_color=ft.Colors.BLUE_200
    )
    
    input_correo = ft.TextField(
        label='Correo',
        color=ft.Colors.WHITE,
        border_color=ft.Colors.WHITE,
        label_style=ft.TextStyle(color=ft.Colors.WHITE),
        focused_border_color=ft.Colors.BLUE_200
    ) 
    
    input_telefono = ft.TextField(
        label='Telefono',
        keyboard_type=ft.KeyboardType.NUMBER,
        input_filter=ft.InputFilter(allow=True, regex_string=r"[0-9]", replacement_string=""),
        color=ft.Colors.WHITE,
        border_color=ft.Colors.WHITE,
        label_style=ft.TextStyle(color=ft.Colors.WHITE),
        focused_border_color=ft.Colors.BLUE_200
    )
    
    input_contraseña = ft.TextField(
        label='Contraseña',
        password=True,
        can_reveal_password=True,
        color=ft.Colors.WHITE,
        border_color=ft.Colors.WHITE,
        label_style=ft.TextStyle(color=ft.Colors.WHITE),
        focused_border_color=ft.Colors.CYAN_200
    )
    
    #### REGISTRO EN DB
    
    def registro_en_db(e):
        if not all([input_propetario.value, input_negocio.value, input_direccion, input_correo.value, input_telefono.value, input_contraseña.value]):
            mostrar_mensaje_resgitro(page, "Error: Todos los campos son obligatorios", ft.Colors.RED_400)
            return

        if not es_correo_valido(input_correo.value):
            mostrar_mensaje_resgitro(page, "Formato de correo no válido (ej: usuario@correo.com)", ft.Colors.ORANGE_700)
            return
        
        if not es_telefono_valido(input_telefono.value):
            mostrar_mensaje_resgitro(page, "El teléfono debe contener solo números (8-15 dígitos)", ft.Colors.ORANGE_700)
            return
        
        
        if correo_ya_existe(input_correo.value):
            mostrar_mensaje_resgitro(page, "Este correo ya está registrado", ft.Colors.ORANGE_700)
            return
        try:
            registro_vendedor_en_nube(
                input_propetario.value,
                input_negocio.value,
                input_direccion.value,
                input_correo.value,
                input_telefono.value,
                input_contraseña.value 
            )
            mostrar_mensaje_resgitro(page, '¡Registro de cuenta exitoso!', ft.Colors.GREEN_400)
            main(page) # Regresamos al inicio
            
        except Exception as ex:
            print(f'Error al registrar en Supabase: {ex}')
   
    
    
    
    page.add(
        ft.Stack(
            expand=True,
            controls=[
                ft.Container(
                    expand=True,
                    gradient=ft.LinearGradient(
                        begin=ft.Alignment(0, -1),
                        end=ft.Alignment(0, 1),
                        colors=['#0f2027', '#203a43', '#2c5364']
                    )
                ),
                
                ft.Container(
                    expand=True,
                    alignment=ft.Alignment(0, 0),
                    
                    content=ft.Column(
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        alignment=ft.MainAxisAlignment.CENTER,
                        spacing=30,
                        controls=[
                            ft.Column(
                                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                spacing=100,
                                controls=[
                                    ft.Text('REGISTRO DE VENDEDOR',
                                            size=26,
                                            color=ft.Colors.WHITE,
                                            weight='bold'
                                            ),
                                    ft.Text('Recuerda llenar tus datos correctamente',
                                            size=20,
                                            color=ft.Colors.WHITE,
                                            weight='bold',)
                                ]
                            ),
                            ft.Column(
                                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                spacing=10,
                                controls=[
                                    input_propetario,
                                    input_negocio,
                                    input_direccion,
                                    input_correo,
                                    input_telefono,
                                    input_contraseña,
                                    ft.FilledButton(
                                        'Finalizar Registro',
                                        bgcolor=ft.Colors.BLUE_GREY_500,
                                        width=300,
                                        on_click=registro_en_db 
                                    ),                                                                        
                                    ft.TextButton(
                                        'Volver',
                                        on_click=lambda _: main(page)
                                    )                                
                                ]
                            )
                        ]
                    )
                )
            ]
        )
    )


### PAGE THE START


def main(page: ft.Page):
    page.controls.clear()
    
    page.title = 'MiSuperSuper 🛒'
    page.padding = 0
    
    
    page.add(
        ft.Stack(
            expand=True,
            controls=[
            # FONDO
            ft.Container(
                expand=True,
                gradient=ft.LinearGradient(
                    begin=ft.Alignment(0, -1),
                    end=ft.Alignment(0, 1),
                    colors=['#0f2027', '#203a43', '#2c5364']
                ),       
            ),
            
            # TEXTO   
            ft.Container(
                expand=True,
                alignment=ft.Alignment(0, 0),
                content=ft.Column(
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    spacing=30,
                    controls=[
                        #TEXTOS
                        ft.Column(
                            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                            alignment=ft.MainAxisAlignment.CENTER,
                            spacing=100,
                            controls=[
                        ft.Text('BIENVENIDO',
                                size=50,
                                color=ft.Colors.WHITE,
                                weight='bold'
                                ),
                        ft.Text('Seleccione una opción',
                                weight='bold',
                                size=20,
                                color=ft.Colors.WHITE
                                )
                            ]
                        ),
                        # BOTONES
                        ft.Column(
                            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                            spacing=15,
                            controls=[
                            ft.FilledButton(
                                'Registrarme como usuario 👤',
                                elevation=100,
                                width=300,
                                color=ft.Colors.WHITE,
                                bgcolor=ft.Colors.BLUE_GREY_700,
                                on_click=lambda _: crear_usuario(page)
                            ),
                            ft.FilledButton(
                                'Registrarme como vendedor 👨‍💻',
                                elevation=100,
                                width=300,
                                color=ft.Colors.WHITE,
                                bgcolor=ft.Colors.BLUE_GREY_700,
                                on_click=lambda _: crear_vendedor(page)
                            ),
                            ft.FilledButton(
                                'Iniciar sesión',
                                elevation=100,
                                width=135,
                                color=ft.Colors.WHITE,
                                bgcolor=ft.Colors.BLUE_GREY_400,
                                on_click=lambda _: login(page)
                            )
                            ]
                        )
                    ]
                )
                
            )
        ]
    )
)
    page.update()
    
### Inicializar app
ft.app(target=main)
