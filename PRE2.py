import sqlite3 as sql
import pandas as pd
datos=sql.connect('db_personas.db')

Consulta="""
SELECT P.fecha_ingreso, S.Rol, P.residencia,P.rut,P.nombre_completo,P.nacionalidad,P.fecha_de_nacimiento,P.profesion,S.sueldo 
FROM personas AS P 
INNER JOIN Salarios AS S ON P.id_rol = S.id_salarios
"""
df=pd.read_sql(Consulta,con=datos)

print(df)