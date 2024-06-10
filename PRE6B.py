import sqlite3 as sql
import matplotlib.pyplot as plt

conexionV2= sql.connect('DATA/db_personas.db')
cursorV2= conexionV2.cursor()

consultaV2="""
SELECT p.profesion, ROUND(COUNT(*) * 100.0 / (SELECT COUNT(*) FROM personas), 2) AS porcentaje
FROM personas p
GROUP BY p.profesion;
"""
cursorV2.execute(consultaV2)
resultadosV2=cursorV2.fetchall()

profesionV2=[resultado[0]for resultado in resultadosV2]
porcentaje=[resultado[1]for resultado in resultadosV2]

plt.figure(figsize=(10,6))
plt.pie(porcentaje, labels=profesionV2, autopct='%1.1f%%', startangle=140)
plt.title('Distribucion de Profesiones')
plt.axis('equal')
plt.show()