import sqlite3 as sql
import pandas as pd
import matplotlib.pyplot as plt
import PRE4 as PRE4A
import PRE5 as PRE5A

def PRE1():
    conn = sql.connect('Sql_data/db_personas.db')
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

def PRE2():
    datos=sql.connect('DATA/db_personas.db')

    Consulta="""
    SELECT P.fecha_ingreso, S.Rol, P.residencia,P.rut,P.nombre_completo,P.nacionalidad,P.fecha_de_nacimiento,P.profesion,S.sueldo 
    FROM personas AS P 
    INNER JOIN Salarios AS S ON P.id_rol = S.id_salarios
    """
    df=pd.read_sql(Consulta,con=datos)

    print(df)
     
def PRE3():
    inicio = True
    while inicio:
        rut = input('Dame el RUT del trabajador (con guion): ')
        rut = str(rut)
        try:
            datos = sql.connect('DATA/db_personas.db')
            # Corrección en la concatenación de la consulta SQL
            consultaFIL = "SELECT * FROM personas as p WHERE p.rut='" + rut + "'"
            busq = pd.read_sql(consultaFIL, con=datos)
            print(busq)
            inicio = False
        except ValueError:
            print('ERROR: Valor incorrecto o no registrado')


def PRE4():
  PRE4A.example_contract()
  
def PRE5():
    PRE5A.example_contract()  

def PRE6A():
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

def PRE6B():
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

def PRE6C():
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

def mostrar_OPCIONES():
    print('1.Mostrar datos de Empleados')
    print('2.Mostrar datos de Empleados en Tabla (DataFrame)')
    print('3.Buscar Empleado por RUT')
    print('4.Generar Contrato con RUT')
    print('5.Generar Contrato en RANGO de Personas')
    print('6.Mostrar Grafico de Promedios de Sueldo por Profesion')
    print('7.Mostrar Grafico de distribucion de Profesiones')
    print('8.Mostrar Grafico de Cantidad de Trabajadores por Nacionalidad')
    print('9.SALIR')
    
def obtener_opcion():
    while True:
        opcion=input('Ingrese la opcion: ')
        try:
            opcion = int(opcion)
            if 1 <= opcion <= 9:
                return opcion
            else:
                print('Por favor, Ingrese un Correcto(Entre 1 y 9)')
        
        except ValueError:
            print('Porfavor Ingrese Un numero valido')


def bucle():
    while True:
        mostrar_OPCIONES()
        opcion=obtener_opcion()
        
        if opcion == 1:
            try:
                PRE1()
            except:
                print('Error Intente de nuevo') 
        
        elif opcion==2:       
            try:
                PRE2()
            except ValueError:
                print('Error Intente de nuevo') 
        
        elif opcion==3:       
            try:
                PRE3()
            except:
                print('Error Intente de nuevo')
        
        elif opcion==4:       
            try:
                PRE4()
            except:
                print('Error Intente de nuevo')                 
        
        elif opcion==5:       
            try:
                PRE5()
            except:
                print('Error Intente de nuevo')
        
        elif opcion==6:       
            try:
                PRE6A()
            except:
                print('Error Intente de nuevo')
        
        elif opcion==7:       
            try:
                PRE6B()
            except:
                print('Error Intente de nuevo')        
                
        elif opcion==8:       
            try:
                PRE6C()
            except:
                print('Error Intente de nuevo') 
        elif opcion== 9:
            print('Saliendo del Programa')
            break   
        
        
if __name__ =='__main__':
    bucle()
