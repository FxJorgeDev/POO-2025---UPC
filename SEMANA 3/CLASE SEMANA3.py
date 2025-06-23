"""""
c = list("ELIAS BOL AÑOS")
print(type(c))
print(c)
print(c.count('O'))

l =  c.pop(5)
print(l)

for caracter in c:
    print(caracter)

import random
for i in  range(100):
 print(random.randint(1,25),end=" ")

cadena = "ELIAS BOL AÑOS"
if "OL" in cadena:
    print("SI")
else:
    print("NO")"""
    
#EJERCICIO 1
""""
list1 = list(range(1,11,))
print(list1)
list2 = list1[::-1]
print(list2)"""

#EJERCICIO 2
"""
lista = []
while True:
 numeros = int(input("INGRESE LOS VALORES DE LAS LISTAS (CON 0 SE ACABA): "))
 if numeros > 0 and numeros != 0 :
    lista.append(numeros)
 else:
      break

print(lista)
print(len(lista))
print(lista[-1])
print(lista[::-1])"""

 #EJERCICIO 3

import random
lista = []
lista2 = []
for i in range(50):
    lista.append(random.randint(1,100,))
print(lista, end=' ')


lista2.append(lista * 2)
print(lista2,end=' ')