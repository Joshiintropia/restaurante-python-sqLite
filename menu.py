from tools import limpiar_pantalla, seguir
from bd import conexion, cursor

#CREATE
def crear_producto():
    nombre_producto = input("Ingresar nombre del producto del Menú: ").capitalize()
    try:
        precio = float(input(f"Ingresa el precio del producto {nombre_producto}: "))
        print(f"Producto = {nombre_producto} | Precio = {precio}" )

        #CREAMOS LA INSERSION A LA BASE DE DATOS EN LA TABLA producto
        cursor.execute(f"""
            INSERT INTO producto (nombre_producto, precio) VALUES ("{nombre_producto}", {precio})
            """)
        conexion.commit()

        print("""
                =================
                PRODUCTO AGREGADO
                =================
            """)

    except ValueError:
        print("""
            ============================
                Solo puedes agregar
            números enteros o decimales.
            ============================
            """)
        seguir()
        limpiar_pantalla()
        crear_producto()


#READ
def mostrar_productos():
    pass

def mostrar_producto():
    pass

#UPDATE
def actualizar_producto():
    pass

#DELETE
def borrar_producto():
    try:
        id_prod = int(input("Ingresa el ID del prodcuto a borrar: "))
        cursor.execute(f"DELETE FROM producto where id_prod = {id_prod}")
        print("""
                ===================
                PRODUCTO ELIMINADO
                ===================
            """)
        seguir()
    except ValueError:
        print("""
                Debes ingresar solo números enteros
            """)
        seguir()
    except KeyError:
        print("""
                ================================
                El producto ingresado no existe
                    NO se puede borrar
                ================================
            """)
        seguir()
