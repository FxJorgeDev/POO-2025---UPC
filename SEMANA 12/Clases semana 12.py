import numpy as np

# array -> crea un vector con los valores de la lista
"""vector = np.array([1,2,-1,4,9])
print(vector)
for i in vector:
    print(i) """

# El (size =....) indica el tamanio de creacion del vector depende la cantidad que le pongas
"""vector = np.random.randint(10,99,size = 5)
# Operaciones con vectores, en cada operacion los valores del vector cambian...
print(f"\n{vector}")
vector = vector ** 2
print(f"\n{vector}")
vectorResiduos = vector % 2
print(f"\n{vectorResiduos}")
vector = vector + 10
print(f"\n{vector}")
vector = vector - 2
print(f"\n{vector}")
vector = vector * 3
print(f"\n{vector}")
vector = vector / 2
print(f"\n{vector}") """

""""
vector1 = np.random.randint(1,9,size=5)
vector2 = np.random.randint(1,9,size=5)
print(f"\n{vector1}")
print(f"{vector2}")
print(f"\nSuma: {vector1 + vector2}")
print(f"Resta: {vector1 - vector2}")
print(f"Multiplicación: {vector1 * vector2}")
print(f"División: {(vector1 / vector2)}")
print(vector1)
print(vector2) """

"""lista = np.random.randint(1,100,size=20)
vector = np.array(lista)
print(f"- Suma de todos los elementos: {np.sum(vector)}\n")
print(f"- Promedio de todos los elementos: {np.mean(vector)}\n")
print(f"- El mayor de todos los elementos: {np.max(vector)}\n")
print(f"- El menor de todos los elementos: {np.min(vector)}\n")
fila = 2
columna = 10
# el reshape(fila,columna) crea un matriz de acuerdo al vector al que se indica
matriz = vector.reshape(fila,columna)
print(f"- Cambiando la forma del vector a una matriz {fila}x{columna}\n{matriz}")"""
"""
vector = np.array([[[1,11], [3,2,]], [[3,6], [2,4]]])
print(f"Número de dimensiones: {vector.ndim}")
print(f"Forma: {vector.shape}")
print(f"Tamaño: {vector.size}")
print(f"Tipo: {vector.dtype}")
print(f"Arreglo:\n{vector}")
for valor in np.nditer(vector):
    print(f"Elemento:{valor}")"""

vector2 = np.array([[1,2,9,4],[23,6,7,10]])
print(vector2)
print(f"{"Indices":6} {"valores":7}")
for idx,valor in np.ndenumerate(vector2):
    print(f"{idx} {valor:^7}")
print("ELIMINACION DE VALORES")
#el np,delete(vector,posicion en el vector, sin indices -> en un mismo bloque de codigo se puede borrar varios elementos) -> sirve para señalar el vector a borrar
vector2 = np.delete(vector2,[4,7])
print(vector2)

print("AGREGANDO VALORES")
# sintaxis-> np.insert(nombre_vector,posicion,valor a insertar)
print("se agrego 54 en la primera posicion")
vector2 = np.insert(vector2,0,54)
print(vector2)
print("se agrego 20 en la cuarta posicion")
vector2 = np.insert(vector2,3,20)
print(vector2)
print("se agrego 100 en la ultima posicion")
vector2 = np.insert(vector2,len(vector2),100)
print(vector2)
for idx,valor in np.ndenumerate(vector2):
    print(f"{idx} {valor:^7}")
print("ORDENAMIENTO EN ARREGLOS CON NUMPY")
#utilizando sort
vector3 = np.random.randint(10,99,size=5)
print(f"vector:{vector3}")
vector3.sort()
print(f"Vector: {vector3}")
print(f"\nORDENADO DESCENDENTEMENTE")
print(f"Vector:{vector3[::-1]}")
print("Ordenamiento con np.sort no altera vector original")

#utilizando sort
vector4 = np.random.randint(10,99,size=5)
print(vector4)
print("\nOrdenando Ascendentemente")
print(f"vector:{np.sort(vector4)}")
print("\Ordenado Descendentemente")
print(f"Vector:{np.sort(vector4)[::-1]}")
      
