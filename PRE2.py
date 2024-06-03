import sqlite3 as sql
import pandas as pd
datos=sql.connect('db_personas.db')

df=pd.read_sql(sql='SELECT p.fecha_ingreso, p.residencia, p.rut, p.nombre_completo,p.nacionalidad, p.fecha_de_nacimiento, p.profesion, s.Sueldo FROM personas AS p INNER JOIN Salarios AS s p.id_rol = s.id_salarios', con=datos)
print(df.head())