import sqlite3 as lite

conexion = lite.connect("contrasenaSegura.db")

with conexion:

    cursor = conexion.cursor()

    def crear_tabla_contrasenas():
        cursor.execute('''
                    CREATE TABLE IF NOT EXISTS contrasenas (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    servicio TEXT NOT NULL,
                    usuario TEXT NOT NULL,
                    password TEXT NOT NULL
                    )
        ''')


    def guardar_contrasena(servicio, usuario, password):
        try:
            cursor.execute('''
                        INSERT INTO contrasenas (servicio, usuario, password)
                    VALUES(?, ?, ?)
            ''', (servicio, usuario, password))
            conexion.commit()
            print('Contraseña guardada')

        except lite.Error as e:
            print(f"Error al guardar la contraseña: {e}")

    cursor.execute('SELECT * FROM contrasenas')
    filas = cursor.fetchall()
    for fila in filas:
        print(fila)



