import sqlite3 as sql
import matplotlib.pyplot as plt

conexionV3= sql.connect('DATA/db_personas.db')
cursorV3= conexionV3.cursor()

consultaV3="""
SELECT nacionalidad, 
COUNT(*) as cantidad_trabajadores
FROM  personas 
GROUP BY nacionalidad;
"""
cursorV3.execute(consultaV3)
resultadosV3=cursorV3.fetchall()

nacionalidades=[resultado[0]for resultado in resultadosV3]
cant=[resultado[1]for resultado in resultadosV3]

plt.figure(figsize=(5,7))
plt.bar(nacionalidades, cant,color='skyblue')
plt.xlabel('Nacionalidades')
plt.ylabel('Cantidad de Trabajadores')
plt.title('Trabajadores por Nacionalidad')
plt.xticks(rotation=45,ha='right')
plt.show()