
#EJERCICIO 6 SEMANA 3.1

""""
def menu():
 print("[1] Pulgadas")
 print('[2] Yardas')
 print('[3] Millas')
 print('[4] Milimetros')
 print('[5] Centimetros')
 print('[6] Metros')
 print('[7] Resumen')
 print('[8] Salir')
 
def conver():
    lista2 =[]
    lista3=[]
    cont =0
    while True: 
     menu()
     cont +=1
     conver = input('Desea convertir a:')
     if conver == '7':
        break
     pies = float(input('Ingrese la medida en pies: '))
     lista2.append(pies)
     match conver:
         case '1':
             medida = 'pulgadas'
             lista2.append(medida)
             pulgadas = pies*12
             convertido = pulgadas
             lista3.append(convertido)
             print(pulgadas)
         case '2':
             medida = 'yardas'
             lista2.append(medida)
             yardas = pies*0.33
             convertido = yardas
             lista3.append(convertido)
             print(yardas)
         case '3':
             medida = 'Millas'
             lista2.append(medida)
             millas = 0.0002 * pies
             lista3.append(convertido)
             convertido = millas
             print(millas)
         case '4':
             medida = 'Milimetros'
             lista2.append(medida)
             milimetros = pies * 304.8
             convertido = milimetros
             lista3.append(convertido)
             print(milimetros)
         case '5':
             medida = 'Centimetros'
             lista2.append(medida)
             centimetros = pies * 30.48
             convertido = centimetros
             lista3.append(convertido)
             print(centimetros)
         case '6':
             medida = 'metros'
             lista2.append(medida)
             metros = pies * 0.3048
             convertido = metros
             lista3.append(convertido)
             print(metros)
             
    print(cont-1)
    print(lista2)
    print(lista3)
       
conver()"""
    
#EJERCICIOS ACTUZALIZADO SEMANA 3.4
""""
from random import randint

num = int(input('Ingrese el tamaño de la lista: '))
lista = []
if num < 50:
 for i in range(num):
  lista.append(randint(1,101))
else:
 print('ERROR...')
 
print(lista)
for i in range(num-1):
    if lista[i+1]>lista[i]:
        print(lista[i], end=' ')
    else:
        print(lista[i], end='\n')
print(lista[num-1])"""


#EJERCICIOS PRACTICAS SEMANA 3 Y 4
 
#EJERCICIO 4 SEMANA 03.03
""""
num = int(input('Ingrese un numero menor a 10: '))

for i in range(num):
    for j in range(1,i+2):
        print(j,end=' ')
    print() """

#EJERCICIO 5 SEMANA 3.03
""""
num = int(input('Ingrese el tamaño: '))
char = (input('Ingrese caracter: '))

for i in range(num):
    for x in range(i+1,num+1):
        print(char,end='')
    print()"""

#EJERCICIO 6 SEMANA 3.03
""""
num = int(input('Ingrese N: '))
for i in range(num):
    if i == 0 or i == num - 1:
        print("* " * num)
    else:
        print("*" + "  " * (num - 2) + " *")"""

#EJERCICIO PRACTICA PC 1

def sumatoria (x,n):
  cont = 0
  cont2 = 1
  contador = 0.0
  while True:
     cont += 1
     cont2 += 1
     if cont2 != n:
      suma = +(cont2**3)/((cont)+x)**0.5 - ((cont2)**3)/((cont)+x)**0.5
      contador += suma
     else:
       break
  return contador

n = int(input('Ingrese n: '))
x = int(input('Ingrese X: '))
print(sumatoria(x,n))