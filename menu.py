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
    resultado = cursor.execute("SELECT * FROM producto").fetchall()
    print("{:<4} {:<20} {:<10}".format("ID", "PRODUCTO", "PRECIO"))
    for row in resultado:
        id, producto, precio = row[0], row[1], row[2]
        print("{:<4} {:<20} {:<10}".format(id, producto, precio))


def mostrar_producto():
    try:
        id = int(input("Ingresa el id del producto a visualizar: "))
        resultado = cursor.execute(f"SELECT * FROM producto WHERE id_prod = {id}").fetchone()
        if resultado != None:
            print("{:<2} | {:<25} | {:<20}".format("ID", "PRODUCTO", "PRECIO"))
            # for row in resultado:
            id, producto, precio = resultado[0], resultado[1], resultado[2]
            print("{:<2} | {:<25} | {:<20}".format(id, producto, precio))
            return resultado
        else:
            print("""
                        PRODUCTO NO ENCONTRADO
                """)
            mostrar_producto()
    except ValueError:
        print("ID desconocido, selecciona uno de la lista...")


#UPDATE
def actualizar_producto():
    mostrar_productos()
    res = mostrar_producto()
    id, prod, prec = res[0], res[1], res[2]

    limpiar_pantalla()
    opcion = int(input(f"""
              Selecciona la opción
            que desea actualizar del:
                {prod.upper()}
        1) NOMBRE
        2) PRECIO

    Selecciona una opción:
        """))
    match opcion:
        case 1:
            prod_nuevo = input("Ingresa el nuevo nombre del PRODUCTO: ")
            cursor.execute(f"UPDATE producto SET nombre_producto = {prod_nuevo} WHERE id_prod = {id}")
            print("""
                    ====================
                    PRODUCTO ACTUALIZADO
                    ====================
                """)
            conexion.commit()
        case 2:
            prec_nuevo = float(input("Ingresa el nuevo precio del PRODUCTO: "))
            cursor.execute(f"UPDATE producto SET precio = {prec_nuevo} WHERE id_prod = {id}")
            print("""
                    ====================
                     PRECIO ACTUALIZADO
                    ====================
                """)
            conexion.commit()
        case _:
            print("Opción incorrecta.")

    limpiar_pantalla()
    mostrar_productos()


    # cursor.execute(f"UPDATE producto SET")

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
