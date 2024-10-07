from tools import limpiar_pantalla, seguir
from menu import actualizar_producto, borrar_producto, crear_producto, mostrar_productos, mostrar_producto
# from bd import conexion, cursor

def inicio_menu_productos():
    limpiar_pantalla()
    print("""
                    Bienvenido
            Vamos a agregar productos al menu
            =================================

        Selecciona la acción a realizar
        0) Listar productos
        1) Agregar producto al menú
        2) Actualizar producto del menú
        3) Borrar producto del menú
        4) Regresar
        """)
    try:
        accion = int(input())

        match accion:
            case 0:
                mostrar_productos()
                seguir()
            case 1:
                limpiar_pantalla()
                crear_producto()
                seguir()
            case 2:
                actualizar_producto()
                seguir()
            case 3:
                borrar_producto()
                seguir()
            case 4:
                pass
            case _:
                print("Opción no reconocida, intenta de nuevo")
                inicio_menu_productos()

    except ValueError:
        print("""
            ===========================
                Solo puedes ingresar
            números enteros del 1 al 4
            ===========================
            """)
        seguir()
        inicio_menu_productos()

if __name__=="__main__":
    inicio_menu_productos()
    limpiar_pantalla()
