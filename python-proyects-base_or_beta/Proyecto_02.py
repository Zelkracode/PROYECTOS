import flet as ft

def main(page: ft.Page):

    page.title = 'LISTA DE COMPRAS'
    page.window.width = 500
    page.window.height = 750
    page.bgcolor = ft.Colors.PINK_200
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.spacing = 20

    # LISTA DEL CARRITO
    carrito = []

    productos_precios = {
        "Leche condensada 385gr": 28,
        "Leche Monarca 500ml": 22,
        "Coca-Cola 500ml": 18,
        "Lechuga": 12,
        "2 Jitomates": 25,
        "1/2 Platano": 20,
        "Frijoles 500gr": 35,
        "Masa 385gr": 15,
        "1/2 Tortillas": 22
}

    # FUNCION PARA AGREGAR PRODUCTOS
    def agregar_carrito(producto):
        carrito.append(producto)
        print(carrito)

    # -----------------------------
    # PANTALLA INICIO
    # -----------------------------
    def inicio():

        page.controls.clear()

        titulo = ft.Text(
            'TIENDA TEO',
            size=50,
            weight=ft.FontWeight.BOLD,
            color=ft.Colors.WHITE,
            italic=True
        )

        texto = ft.Text(
            'Bienvenido a la abarrotera más llena de Guadalajara\n¿Qué desea?',
            size=20,
            text_align=ft.TextAlign.CENTER,
            color=ft.Colors.WHITE
        )

        btn_lista = ft.FilledButton(
            'Lista de productos',
            bgcolor=ft.Colors.PINK_400,
            color=ft.Colors.WHITE,
            on_click=lista_productos
        )

        btn_carrito = ft.FilledButton(
            f"Ver carrito ({len(carrito)})",
            bgcolor=ft.Colors.PINK_700,
            color=ft.Colors.WHITE,
            on_click=ver_carrito
        )

        page.add(titulo, texto, btn_lista, btn_carrito)
        page.update()

    # -----------------------------
    # LISTA DE PRODUCTOS
    # -----------------------------
    def lista_productos(e):

        page.controls.clear()

        titulo = ft.Text(
            'LISTA DE PRODUCTOS',
            size=30,
            weight="bold",
            color=ft.Colors.WHITE
        )

        productos = ft.Column(

            [

                ft.FilledButton(
                    'Alimentos refrigerados',
                    bgcolor=ft.Colors.PINK_400,
                    color=ft.Colors.WHITE,
                    width=250,
                    on_click=alimentos_refrigerados
                ),

                ft.FilledButton(
                    'Frutas y Verduras',
                    bgcolor=ft.Colors.PINK_400,
                    color=ft.Colors.WHITE,
                    width=250,
                    on_click=frutas_y_verduras
                ),

                ft.FilledButton(
                    'Productos locales',
                    bgcolor=ft.Colors.PINK_400,
                    color=ft.Colors.WHITE,
                    width=250,
                    on_click=productos_locales
                ),

            ],

            spacing=20

        )

        btn_regresar = ft.TextButton(
            "Regresar",
            icon=ft.Icons.ARROW_BACK,
            on_click=lambda e: inicio()
        )

        btn_carrito = ft.FilledButton(
            "Ver carrito",
            bgcolor=ft.Colors.PINK_700,
            color=ft.Colors.WHITE,
            on_click=ver_carrito
        )

        page.add(titulo, productos, btn_carrito, btn_regresar)

        page.update()

    # -----------------------------
    # PRODUCTOS REFRIGERADOS
    # -----------------------------
    def alimentos_refrigerados(e):

        page.controls.clear()

        titulo = ft.Text(
            'ARTÍCULOS REFRIGERADOS',
            size=30,
            color=ft.Colors.WHITE
        )

        articulos = ft.Column(

            [

                ft.FilledButton(
                    f"Leche condensada 385gr - ${productos_precios['Leche condensada 385gr']}",
                    bgcolor=ft.Colors.PINK_400,
                    color=ft.Colors.WHITE,
                    on_click=lambda e: agregar_carrito("Leche condensada 385gr")
                ),

                ft.FilledButton(
                     f"Leche Monarca 500ml - ${productos_precios['Leche Monarca 500ml']}",
                    bgcolor=ft.Colors.PINK_400,
                    color=ft.Colors.WHITE,
                    on_click=lambda e: agregar_carrito("Leche Monarca 500ml")
                ),

                ft.FilledButton(
                    f"Coca-Cola 500ml - ${productos_precios['Coca-Cola 500ml']}",
                    bgcolor=ft.Colors.PINK_400,
                    color=ft.Colors.WHITE,
                    on_click=lambda e: agregar_carrito("Coca-Cola 500ml")
                ),

            ],

            spacing=10

        )

        btn_regresar = ft.TextButton(
            "Regresar",
            icon=ft.Icons.ARROW_BACK,
            on_click=lista_productos
        )

        btn_carrito = ft.FilledButton(
            "Ver carrito",
            bgcolor=ft.Colors.PINK_700,
            color=ft.Colors.WHITE,
            on_click=ver_carrito
        )

        page.add(titulo, articulos, btn_carrito, btn_regresar)

        page.update()
        
    # -----------------------------
    # PRODUCTOS FRUTAS Y VERDURAS
    # -----------------------------
    
    def frutas_y_verduras(e):

        page.controls.clear()

        titulo = ft.Text(
            'FRUTAS Y VERDURAS',
            size=30,
            color=ft.Colors.WHITE
        )

        articulos = ft.Column(

            [

                ft.FilledButton(
                    f"Lechuga - ${productos_precios['Lechuga']}",
                    bgcolor=ft.Colors.PINK_400,
                    color=ft.Colors.WHITE,
                    on_click=lambda e: agregar_carrito("Lechuga")
                ),

                ft.FilledButton(
                    f"2 Jitomates - ${productos_precios['2 Jitomates']}",
                    bgcolor=ft.Colors.PINK_400,
                    color=ft.Colors.WHITE,
                    on_click=lambda e: agregar_carrito("2 Jitomates")
                ),

                ft.FilledButton(
                    f"1/2 Platano - ${productos_precios['1/2 Platano']}",
                    bgcolor=ft.Colors.PINK_400,
                    color=ft.Colors.WHITE,
                    on_click=lambda e: agregar_carrito("1/2 Platano")
                ),

            ],

            spacing=10

        )

        btn_regresar = ft.TextButton(
            "Regresar",
            icon=ft.Icons.ARROW_BACK,
            on_click=lista_productos
        )

        btn_carrito = ft.FilledButton(
            "Ver carrito",
            bgcolor=ft.Colors.PINK_700,
            color=ft.Colors.WHITE,
            on_click=ver_carrito
        )

        page.add(titulo, articulos, btn_carrito, btn_regresar)

        page.update()
    
    # -----------------------------
    # PRODUCTOS FRUTAS Y VERDURAS
    # -----------------------------
    
    def productos_locales(e):

        page.controls.clear()

        titulo = ft.Text(
            'PRODUCTOS LOCALES',
            size=30,
            color=ft.Colors.WHITE
        )

        articulos = ft.Column(

            [

                ft.FilledButton(
                    f"Frijoles 500gr - ${productos_precios['Frijoles 500gr']}",
                    bgcolor=ft.Colors.PINK_400,
                    color=ft.Colors.WHITE,
                    on_click=lambda e: agregar_carrito("Frijoles")
                ),

                ft.FilledButton(
                    f"Masa 385gr - ${productos_precios['Masa 385gr']}",
                    bgcolor=ft.Colors.PINK_400,
                    color=ft.Colors.WHITE,
                    on_click=lambda e: agregar_carrito("Masa 385gr")
                ),

                ft.FilledButton(
                    f"1/2 Tortillas - ${productos_precios['1/2 Tortillas']}",
                    bgcolor=ft.Colors.PINK_400,
                    color=ft.Colors.WHITE,
                    on_click=lambda e: agregar_carrito("1/2 Tortillas")
                ),

            ],

            spacing=10

        )

        btn_regresar = ft.TextButton(
            "Regresar",
            icon=ft.Icons.ARROW_BACK,
            on_click=lista_productos
        )

        btn_carrito = ft.FilledButton(
            "Ver carrito",
            bgcolor=ft.Colors.PINK_700,
            color=ft.Colors.WHITE,
            on_click=ver_carrito
        )

        page.add(titulo, articulos, btn_carrito, btn_regresar)

        page.update()

    # -----------------------------
    # VER CARRITO
    # -----------------------------
    
    def vaciar_carrito(e):
        
        carrito.clear()

        ver_carrito(e)
    
    
    def ver_carrito(e):

        page.controls.clear()

        titulo = ft.Text(
            'CARRITO DE COMPRAS',
            size=30,
            weight="bold",
            color=ft.Colors.WHITE
        )

        lista = ft.Column()

        if len(carrito) == 0:

            lista.controls.append(
                ft.Text(
                    "El carrito está vacío",
                    color=ft.Colors.WHITE
                )
            )

        else:

            for producto in carrito:

                lista.controls.append(
                ft.ListTile(
                title=ft.Text(producto, color=ft.Colors.WHITE),
                leading=ft.Icon(ft.Icons.SHOPPING_CART, color=ft.Colors.WHITE)
    )
)

        total = 0

        for producto in carrito:
            total += productos_precios[producto]
            
        total_texto = ft.Text(
        f"TOTAL: ${total}",
        size=25,
        weight="bold",
        color=ft.Colors.WHITE
)
       
        btn_pagar = ft.FilledButton(
        "PAGAR",
        icon=ft.Icons.PAYMENTS,
        bgcolor=ft.Colors.GREEN,
        color=ft.Colors.WHITE,
        on_click=pagar
)
        
        btn_regresar = ft.TextButton(
            "Regresar",
            icon=ft.Icons.ARROW_BACK,
            on_click=lista_productos
        )
        
        btn_vaciar_carrito = ft.TextButton(
            "VACIAR",
            icon=ft.Icons.DELETE_OUTLINE,
            on_click=vaciar_carrito
        )

        page.add(titulo, lista, total_texto,btn_pagar, btn_regresar, btn_vaciar_carrito)

        page.update()

    inicio()
    
    
    def pagar(e):

        page.controls.clear()

        titulo = ft.Text(
            "PAGO REALIZADO",
            size=35,
            weight="bold",
            color=ft.Colors.WHITE
        )

        mensaje = ft.Text(
            "✅ Gracias por tu compra\nTu pedido está en preparación",
            size=20,
            text_align=ft.TextAlign.CENTER,
            color=ft.Colors.WHITE
    )

        btn_inicio = ft.FilledButton(
            "Volver al inicio",
            bgcolor=ft.Colors.PINK_400,
            color=ft.Colors.WHITE,
            on_click=lambda e: inicio()
    )

        carrito.clear()

        page.add(titulo, mensaje, btn_inicio)

    page.update()

ft.app(target=main)