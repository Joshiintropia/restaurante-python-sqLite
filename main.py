from tools import limpiar_pantalla, seguir
from menu import crear_producto
# from bd import conexion, cursor

def inicio_menu_productos():
    limpiar_pantalla()
    print("""
                    Bienvenido
            Vamos a agregar productos al menu
            =================================

        Selecciona la acción a realizar
        1) Agregar producto al menú
        2) Actualizar producto del menú
        3) Borrar producto del menú
        4) Regresar
        """)
    try:
        accion = int(input())

        match accion:
            case 1:
                limpiar_pantalla()
                crear_producto()
                seguir()
            case 2:
                pass
            case 3:
                pass
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
