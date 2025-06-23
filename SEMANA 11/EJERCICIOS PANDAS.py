import pandas as pd
from random import randint
# nombre_variable = pd.Series(DATA,INDEX,DTYPE,NAME) -> sintaxis para crear cuadros de pandas
# DATA-> PÚEDE SER UNA LISTA,TUPLA,DICCIONARIO,ETC
# INDEX->SON LOS VALORES QUE IDENTIFICAN A UN DATO EN ESPECIAL..POR DEFECTO SON NUMEROS
# DTYPE-> MUETSTRA EL TIPO DE DATO QUE GUARDA LA TABLA
# NAME -> EL NOMBRE DE TODA TABLA...NOSOTROS LO PODEMOS PONER CUALQUIER NOMBRE
""""
lista = ["Jorge","Nickol","Jhon","Valentin","Nils","Eder","Yorch","Marife","Alex","Brayan"]
indices = []
for i in range(len(lista)):
    if  i < 6:
        i = str(i)
        indice = "A" + i
        indices.append(indice)
    else:
        i = str(i)
        indice = "B" + i
        indices.append(indice)
datos = pd.Series(lista,index=indices,dtype=str,name="DATOS PRUEBA")
print(datos)
print(f"{datos.size} Datos")
print(datos.index)
print(datos.dtype)

for i in datos:
    print(i,end="  ")
print()
for indice,valor in enumerate(datos):
    print(["[",indice,"]: ",valor])"""


"""
lista_numeros = []
tamanio = randint(1,10)
for i in range(tamanio):
    lista_numeros.append(randint(1,10))
indices = []
for i in range(tamanio):
    if  i < 6:
        i = str(i)
        indice = "A" + i
        indices.append(indice)
    else:
        i = str(i)
        indice = "B" + i
        indices.append(indice)
serie_numeros = pd.Series(lista_numeros,indices)
print(f"Cantidad de datos: {serie_numeros.count()}")
print(f"La suma de datos (En enteros se suman los numeros):{serie_numeros.sum()}")
print(f"El mayor valor: {serie_numeros.max()}")
print(f"El menor valor: {serie_numeros.min()}")
print(f"La media de la serie: {serie_numeros.mean()}")
print(f"Suma Acumulada:\n{serie_numeros.cumsum()}")
print(f"Frecuencia de Datos:\nValor\tCantidad:\n{serie_numeros.value_counts()}")
print(f"Varianza de datos: {serie_numeros.var():.2f}")
print(f"Desviacion Estandar: {serie_numeros.std():.2f}")
# AL NOSOTROS HACER OPERACIONES CON SERIES, ALTERAMOS REALMENTE LOS VALORES QUE ESTAN DENTRO DE LAS SERIES...UNO POR UNO
serie_por10 = serie_numeros * 10
print("Serie por 10:")
print(serie_por10)
serie_entre10 = serie_numeros / 10
print("Serie entre 10:")
print(serie_entre10)
serie_potencia = serie_numeros.pow(2)
print("Serie elevado al cuadrado: ")
print(serie_potencia)
serie_Residuo = serie_numeros % 2
print("El residuo de la serie divido entre 2:")
print(serie_Residuo) 

def factorial(n):
    fact = 1
    for i in range(1,n+1):
        fact *= i
    return fact
# nombre_serie.apply(funcion_a_aplicar) -> sintaxis para aplicar una funcion a una serie de pandas
serie_con_funcion = serie_numeros.apply(factorial)
print("FUNCION FACTORIAL APLICADO A LA SERIE")
print(serie_con_funcion)
print("ORDENAMINETO DE DATOS EN FORMA ASCENDENTE:")
print(serie_numeros.sort_values())
print("ORDENAMINETO DE DATOS EN FORMA DESCENDENTE:")
print(serie_numeros.sort_values(ascending=False)) """

""""
lista_str = ["Jorge"," Nickol"," Jhon"," Valentin"," Nils"," Eder"," Yorch"," Marife"," Alex"," Brayan"]
indices = []
for i in range(len(lista_str)):
    if  i < 6:
        i = str(i)
        indice = "A" + i
        indices.append(indice)
    else:
        i = str(i)
        indice = "B" + i
        indices.append(indice)

serie_str = pd.Series(lista_str,indices,dtype=str)
print(serie_str)
print(f"Cantidad de datos: {serie_str.count()}")
print(f"Concatenacion progresiva:\n {serie_str.cumsum()} ")
print(f"Aplicando la funcion UPPER a la serie str:\n{serie_str.apply(str.upper)}")
"""
import os

if not os.path.exists("PRIMER CSV.csv"):
    diccionario = ({"integrante:": ["juan","pepe","maria","Luis","Jorge","Alex","Yorch","Jhon"],
                "edad": [28,30,34,23,18,20,42,12],
                "sexo": ["m","f","f","m","m","m","m","f"],
                "profesion": ["ingeniero","medico","abogado","contador","estudiante","estudiante","Medico","piloto"]})

    ejemplo_pd = pd.DataFrame(diccionario)
    ejemplo_pd.to_csv("PRIMER CSV.csv",sep=",",index=True)
    print("SE GUARDARON LOS DATOS")
else:
    print("ARCHIVO YA CREADO")

if not os.path.exists("PRIMER EXCEL.xlsx"):
    diccionario = ({"integrante:": ["juan","pepe","maria","Luis","Jorge","Alex","Yorch","Jhon"],
                "edad": [28,30,34,23,18,20,42,12],
                "sexo": ["m","f","f","m","m","m","m","f"],
                "profesion": ["ingeniero","medico","abogado","contador","estudiante","estudiante","Medico","piloto"]})

    ejemplo_pd = pd.DataFrame(diccionario)
    ejemplo_pd.to_excel("PRIMER EXCEL.xlsx",sheet_name="datos",index=False)
    print("SE AGREGARON LOS DATOS")
else:
    print("ARCHIVO YA EXISTENTE")
# el r antes de la direccion corrige errores de interpretacion de python
direccion_excel = r"C:\Users\ASUS\Downloads\PRIMER_EXCEL_Actualizado.xlsx"
excel_pd = pd.read_excel(direccion_excel)
excel_pd_hojas = pd.ExcelFile(direccion_excel)
print(excel_pd)
print(excel_pd_hojas.sheet_names)
print(excel_pd.columns)

cont = 0
for i in range(len(excel_pd)):
    cont += excel_pd.loc[i,"edad"]
print(f"Edad acumulado {cont}")

contm = 0
contf = 0
for i in range(len(excel_pd)):
    if excel_pd.loc[i,"sexo"] == "m":
        contm += 1
    if excel_pd.loc[i,"sexo"] == "f":
        contf += 1
print(f"En la tabla hay {contm} varones")
print(f"En la tabla hay {contf} mujeres")
contupc=(excel_pd["universidad"] == 'upc').sum()
contcato=(excel_pd["universidad"] == 'cato').sum()
contpucp=(excel_pd["universidad"] == 'pucp').sum()
contsmp=(excel_pd["universidad"] == 'smp').sum()
print(f"Estudiantes de UPC: {contupc}")
print(f"Estudiantes de Cato: {contcato}")
print(f"Estudiantes de PUCP: {contpucp}")
print(f"Estudiantes de SMP: {contsmp}")

