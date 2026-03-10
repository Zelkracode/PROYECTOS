
import flet as ft


def main(page: ft.Page):
    page.title = 'LISTA DE COMPRAS'
    page.window.width = 500
    page.window.height = 750
    page.bgcolor = ft.Colors.PINK_200
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.spacing = 30
    
    titulo = ft.Text('TIENDA TEO', size=50,weight=ft.FontWeight.BOLD,color=ft.Colors.WHITE,italic=True)
    texto = ft.Text('Bienvenido a la abarrotera mas llena de Guadalajara, que desea?', 
                    size=20,
                    weight=ft.FontWeight.BOLD,
                    color=ft.Colors.WHITE,
                    text_align=ft.CrossAxisAlignment.CENTER,
                    italic=True,
                    margin=ft.margin.only(bottom=80))





    def lista_productos(e):
        
        page.controls.clear()
        
        titulo_lista = ft.Text(
            'LISTA DE PRODUCTOS', 
            size=30, 
            weight="bold", 
            color=ft.Colors.WHITE
        )
        instrucciones = ft.Column(
            controls=[
                ft.Text('¿Cómo comprar algún producto?', size=20, weight="bold", color=ft.Colors.PINK_900),
                ft.Text('1. Seleccione los productos de su agrado', color=ft.Colors.WHITE),
                ft.Text('2. Seleccione pagar y después método de pago', color=ft.Colors.WHITE),
                ft.Text('3. Seleciona el metodo de recoleccion o entrega y listo', color=ft.Colors.WHITE)
            ],
            spacing=10
        )
        
        productos= ft.Row([
            ft.Text('Alimentos refrigerados',size=16, weight="bold", color=ft.Colors.WHITE),
            ft.Text('Frutas y Verduras',size=16, weight="bold", color=ft.Colors.WHITE),
            ft.Text('Productos locales',size=16, weight="bold", color=ft.Colors.WHITE)
        ],
        spacing=5                  
    )
        
        lista_AlimentosRefrigerados = ft.Column([
            ft.FilledButton('Bebidas'),
            ft.FilledButton('Carnes'),
            ft.FilledButton('Productos de granja')
        ]
        
        )
        
        page.add(titulo_lista,
                 instrucciones,
                 productos,
                 lista_AlimentosRefrigerados)
        
        page.update()
        
        

    
    

  
    btn_lista = ft.FilledButton('Lista de productos',
                                color= ft.Colors.WHITE,
                                style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=10)),
                                bgcolor=ft.Colors.PINK_400,
                                on_click=lista_productos)
    
    page.add(titulo,
            texto,
            btn_lista)


ft.app(target=main)