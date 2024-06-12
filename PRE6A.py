import sqlite3 as sql
import matplotlib.pyplot as plt

conexion= sql.connect('DATA/db_personas.db')
cursor= conexion.cursor()

consulta="""
SELECT p.profesion, ROUND(AVG(s.sueldo) / 1000000, 2) AS promedio_sueldo_millones
FROM personas p
JOIN  Salarios s ON p.id_rol = s.id_salarios
GROUP BY p.profesion;
"""
cursor.execute(consulta)
resultados=cursor.fetchall()

profe=[resultado[0]for resultado in resultados]
sueld=[resultado[1]for resultado in resultados]

plt.figure(figsize=(8,6))
plt.bar(profe, sueld, color='green')
plt.xlabel('Profesion')
plt.ylabel('Promedio de Sueldo(en Millones CLP)')
plt.title('Promedio de Sueldo por Profesion')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()
