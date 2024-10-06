import sqlite3

#creamos la conexión a la DB (si no existe la DB, la va a crear)
conexion = sqlite3.connect("restaurante.db")

#creamos el cursos para manupular la DB
cursor = conexion.cursor()

#Creamos la primera tabla PRODUCTO (Solo si no existe)
cursor.execute("""
    CREATE TABLE IF NOT EXISTS producto(
    id_prod INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre_producto VARCHAR(50) NOT NULL,
    precio FLOAT NOT NULL
    );
    """)

#Creamos la tabla FORMA DE PAGO
cursor.execute("""
    CREATE TABLE IF NOT EXISTS formapago(
    id_pago PRIMARY KEY AUTOINCREMENT,
    pago VARCHAR (20),
    );
    """)

#Creamos la tabla MESAS
cursor.execute("""
    CREATE TABLE IF NOT EXISTS mesas(
    id_mesas PRIMARY KEY AUTOINCREMENT,
    estatus INTEGER NOT NULL,
    id_prod_FK INTEGER,
    FOREIGN KEY(id_prod_FK) REFERENCE producto(id_prod)
    );
    """)

#Creamos la tabla de relación TICKET
cursor.execute("""
    CREATE TABLE IF NOT EXISTS ticket(
    id_ticket PRIMARY KEY AUTOINCREMENT,
    total FLOAT NOT NULL
    id_prod_FK INTEGER,
    id_pago_FK INTERGER,
    id_mesa_FK INTEGER,
    FOREIGN KEY(id_prod_FK) REFERENCE producto(id_prod),
    FOREIGN KEY(id_pago_FK) REFERENCE formapago(id_pago),
    FOREIGN KEY(id_mesa_FK) REFERENCE mesas(id_mesas),
    );
    """)

#Creamos la persistencia de las tablas
conexion.commit()
