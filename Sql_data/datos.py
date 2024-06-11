import sqlite3
import pandas as pd

# Conectar a la base de datos SQLite
conn = sqlite3.connect('Sql_data/db_personas.db')
cursor = conn.cursor()

# Ejecutar la consulta SQL
cursor.execute("""
SELECT p.fecha_ingreso, p.residencia, p.rut, p.nombre_completo, p.nacionalidad, p.fecha_de_nacimiento, p.profesion, s.Rol, s.Sueldo
FROM personas AS p
INNER JOIN Salarios AS s ON p.id_rol = s.id_salarios
""")

# Obtener todos los resultados
resultados = cursor.fetchall()

# Imprimir los resultados con nombres de columnas
column_names = ["Fecha Ingreso", "Residencia", "RUT", "Nombre Completo", "Nacionalidad", "Fecha de Nacimiento", "Profesión", "Rol", "Sueldo"]

for fila in resultados:
    fila_dict = dict(zip(column_names, fila))
    for col, val in fila_dict.items():
        print(f"{col}: {val}")
    print()  # Nueva línea para separar las filas

# Cerrar la conexión a la base de datos
conn.close()
