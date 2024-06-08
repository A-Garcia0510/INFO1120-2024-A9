import sqlite3 as sql
import pandas as pd

datos=sql.connect('db_personas.db')

def filtro(rut):
    consultaFIL="SELECT * FROM personas as p WHERE p.rut="+ rut
    return consultaFIL

resultado=filtro('"16837051-2"')

busq=pd.read_sql(resultado,con=datos)
print(busq)