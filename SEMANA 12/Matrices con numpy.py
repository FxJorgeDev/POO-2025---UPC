import numpy as np
"""""
matriz = np.array([[1,3,5,7],[2,4,6,8]])
print(f"Matriz:{matriz}")
M=3
#Creacion de matriz inicializada en ceros
matrizceros=np.zeros((M,M))
print(f"MATRIZ CON PURO CEROS:\n {matrizceros}")
#Creacion de una matriz identidad
matrizidentidad = np.eye(M)
print(f"MATRIZ IDENTIDAD;\n{matrizidentidad}")
#Matriz con unos
matrizuno = np.ones((M,M))
print(f"MATRIZ CON PUROS UNO:\n{matrizuno}")
#Matriz con un valor especifico -> np.full((fila,columna),valor especifico)
matriz_especifico = np.full((M,M),5)
print(f"MATRIZ CON VALOR ESPECIFICO:\n {matriz_especifico}")
#Creando matriz Aleatoria
matrizaleatoria = np.random.rand(M,M)
print(f"MATRIZ DE MANERA ALEATORIA:\n{matrizaleatoria}")
#Creando matriz normal
matriz_normal = np.random.randn(M,2)
print(f"MATRIZ NORMAL:\n{matriz_normal}")

#Generar un matriz de 4x5 con valores entew 10 a 99
fila = 20
col = 10
tamanio = fila*col
vector = np.random.randint(10,99,tamanio)
matriz_generada = vector.reshape(fila,col)
print(f"MATRIZ GENERADA:\n {matriz_generada}") """
#CREAR UNA MATRIZ DE TAMANIO 20, EN DONDE EN LOS CASILLEROS PARES HAYA VALORES RANDOM ENTRE 2 A 9 Y EN LOS CASILLEROS IMPARES
#VALORES ENTRE 10 A 15
import random
import pandas as pd
vector = []
for i in range(20):
    if i % 2 == 0:
        vector.append(random.randint(2,9))
    else:
        vector.append(random.randint(10,15))
matriz = np.array(vector).reshape(4,5)
print(matriz)

# EJERCICIOS DE PANDAS SERIES
def agregar_nombre():
    valor = str(valor)
    return valor + "jorge"
serie_str= pd.Series(["jorge ","jorge ","nickol ","nickol ","Jhon "])
print(serie_str.cumsum())
print(serie_str.value_counts())
print(serie_str.str.upper())

serie_float=pd.Series([1.1,4.5,8.7,5.6,65.5])
print(serie_float.cumsum())
print(serie_float.pow(2))
