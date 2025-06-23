#EJERCICIO 4
""""
from random import randint

listanum = []
for i in range(20):
  listanum.append(randint(1,101))

print(listanum)

print("PROMEDIO:",sum(listanum)/len(listanum))

impar = 0
par = 0
for x in listanum:
  if x % 2 == 0:
    par += 1
  else:
    impar += 1
print(par)  
print(impar)"""

#EJERCICIO 5

lista1=[]
lista2=[]
lista3=[]
lista4=[]
def horas(num):
 horas = num// 3600
 return horas

def minutos(num):
 minutos = (num % 3600) // 60
 return minutos
def segundos(num):
  segundos =  (num % 3600) % 60
  return segundos

while True:
 try:
   sd = str(input('Desea continuar: '))
 except:
   print("SOLO NUMEROS....")
 if sd == 'si':
     num = int(input('Ingrese la cantidad de segundos: '))
     if num > 0:
       horas(num)
       minutos(num)
       segundos(num)
       print('Horas: ',horas(num))
       print('Minutos: ',minutos(num))
       print('Segundos: ',segundos(num))
       lista1.append(num)
       lista2.append(horas(num))
       lista3.append(minutos(num))
       lista4.append(segundos(num))
     else:
       print("ERROR...")
 else:
    break
 
print(lista1,lista2,lista3,lista4)

