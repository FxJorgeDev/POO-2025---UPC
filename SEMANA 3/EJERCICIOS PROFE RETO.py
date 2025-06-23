 
 #EJERCICIO 1
 
"""""
lista = []
while True:
    try:
      num = int(input("Ingrese numeros enteros hasta que introduzaca 0: "))
    except:
        print("Solo enteros y no caracteres....")
    if num != 0:
      lista.append(num)
    else:
        break
 
nega = sum ( x < 0 for x in lista)
posi = sum(x > 0 for x in lista)
print("Numeros leidos = ", len(lista))
print("Numero mayor = ", max(lista))
print("Numero menor = ", min(lista))
print("Numeros Positivos = ", posi)
print("Numeros Negativos = ", nega)
print("El promedio de los numeros = ", sum(lista) / len(lista)) """

#EJERCICIO 3

""""
def inv(num):
 num1 = str(num)
 num2 = num1[::-1]
 num3 = int(num2)
 return num3

try:
  num = int(input("Ingrese N:"))
except:
    print("Solo numeros.....")
    
print("El numero invertido es: ", inv(num))"""

#EJERCICIO 4
""""
while True:
  num = int(input("Ingrese el numero: "))
  if num > 0 and num < 11:
     break
  else:
     print("ERROR...")


for x in range(1,num + 1):
 for y in range(1,x + 1):
     print(y, end=' ')
 print()"""

#EJERCICIO 5

try:
 num = int(input("Ingrese un numero: "))
 char = (input("Ingrese un caracter: "))
except:
 print("ERROR...")

if num > 0 and num < 11:
 for x in range(num,0,-1):
  print(char * x)

else:
 print("Un numero entre el rango anterior....")


