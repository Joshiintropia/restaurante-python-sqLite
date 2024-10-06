from tools import limpiar_pantalla, seguir
from bd import conexion, cursor

def crear_producto():
    nombre_producto = input("Ingresar nombre del producto del Menú: ")
    try:
        precio = float(input(f"Ingresa el precio del producto {nombre_producto}: "))
        print(f"Producto = {nombre_producto} | Precio = {precio}" )

        #CREAMOS LA INSERSION A LA BASE DE DATOS EN LA TABLA producto
        cursor.execute(f"""
            INSERT INTO producto (nombre_producto, precio) VALUES ("{nombre_producto}, {precio}")
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
