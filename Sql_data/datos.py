import sqlite3

conn = sqlite3.connect('Sql_data/db_personas.db')
cursor = conn.cursor()

cursor.execute("""SELECT p.fecha_ingreso,p.residencia,p.rut,p.nombre_completo,p.nacionalidad,p.fecha_de_nacimiento,p.profesion,s.Rol
FROM personas AS p
INNER JOIN Salarios AS s ON p.id_rol = s.id_salarios""")

resultados = cursor.fetchall()
for fila in resultados:
    print(fila)

conn.close()
