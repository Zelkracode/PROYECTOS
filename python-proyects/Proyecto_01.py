import flet as ft

def main(page: ft.Page):
    page.title = 'Mis tareas'
    page.window.width = 400 
    page.window.height = 600
    page.bgcolor = ft.Colors.BLUE_GREY_900
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.padding = 20

    titulo = ft.Text("Mis Pendientes", size=30, weight=ft.FontWeight.BOLD, color=ft.Colors.WHITE)
    
    lista_tareas = ft.Column()

    def tachar_tarea(e):

        if e.control.value == True:
            e.control.label_style = ft.TextStyle(
                color=ft.Colors.WHITE_54, 
                decoration=ft.TextDecoration.LINE_THROUGH,
                italic=True
            )
        else:

            e.control.label_style = ft.TextStyle(
                color=ft.Colors.WHITE, 
                decoration=ft.TextDecoration.NONE,
                italic=False
            )
        page.update()

    def borra_tarea(e):
        lista_tareas.controls.remove(e.control.data)
        page.update()
        
    def Agregar(e):
        if tarea.value != '':

            check_tarea = ft.Checkbox(
                label=tarea.value, 
                value=False,
                label_style=ft.TextStyle(color=ft.Colors.WHITE, size=16),
                on_change=tachar_tarea 
            )
            
            nueva_fila = ft.Row(
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                controls=[check_tarea]
            )
            
            boton_borrar = ft.IconButton(
                icon=ft.Icons.DELETE_OUTLINE, 
                on_click=borra_tarea, 
                icon_color=ft.Colors.RED,
                data=nueva_fila 
            )
            
            nueva_fila.controls.append(boton_borrar)
            lista_tareas.controls.append(nueva_fila)
            
            tarea.value = ''
            page.update()

    tarea = ft.TextField(
        hint_text='¿Qué tarea tienes?', 
        color=ft.Colors.WHITE, 
        expand=True,
        border_color=ft.Colors.BLUE_400,
        on_submit=Agregar 
    ) 
    btn_add = ft.ElevatedButton('Agregar', on_click=Agregar)
    
    page.add(
        titulo,
        ft.Row([
            tarea,
            btn_add,
        ]),
        lista_tareas
    )

ft.app(target=main)