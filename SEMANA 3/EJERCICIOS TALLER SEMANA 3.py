""""
lista = ["Jorge",'Castillo',18]

print(f'Posicion 1: {lista[0]}')

for x in lista:
    print(x)

tupla = {'12','13','16','34'}

for x in tupla:
    print(x)"""

#EJERCICIO 1 

# LE AGREGAMOS EN RANDOM PARA YA NO ESTAR INGRESANDO DATOS, SE GENERA ALEATORIAMENTE
"""from random import randint
while True:
 try:
   codigo = int(randint(1000000000,10000000000))
 except:
   print('ERROR...')
 if codigo > 999999999 and codigo < 10000000000:
   break
 else:
   print("ERROR EL CODIGO ES DE 10 DIGITOS") 

print('EL CODIGO DEL TRABAJDOR: ',codigo)
codigo1 = str(codigo)
TTTT = codigo1[0:4]
HH = codigo1[4:6]
MM = codigo1[6:8]
SS = codigo1[8:11]

print('CODIGO DEL TRABAJADOR: ', TTTT)
print('HORA DE ENTRADA: ', HH)
print('MINUTO DE ENTRADA: ', MM)
print("SEGUNDOS DE ENTRADA: ",SS) """

#EJERCICIO 2:
"""""

def grafico(n):
 for i in range(n):
   for espacio in range(n-i):
      print(end='  ')
   for j in range(i+1):
     print(end='* ')
   print()

cont=0  
while True:

 sd = str(input('Desea continuar S/N: ' )) 
 cont += 1
 if sd.upper() != 'S':
   break
 try:
    n = int(input('Ingrese el tamaño que desee entre 2 a 9: '))
 except:
   print("ERROR....")

 if n < 10 and n > 1:
   grafico(n)

 else:
    print("EL RANGO DEL TAMAÑO ES ENTRE 2 A 9...")


print(f'Se hicieron {cont-1} dibujos')"""
  

#EJERCICIO 3:

#La funcion ORD() te bota el codigo aschii donde se encuentra un caracter ingresado

#La funcion CHR() es lo contrario, con esta funcion puedes imprimir el caracter ingresando en codigo
"""print(ord('A'))
print(chr(45))"""

def ingresar():
 n = -1
 while n < 2 or n > 9:
  try:
     n = int(input('Ingresa el tamaño del dibujo: '))
  except:
     print('ERROR...')
 return n

def graficos(n):
  for i in range(n):
    letra = 'A'
    for j in range(n-i):
      print(letra, end=' ')
      letra_numero = ord(letra) + 1
      letra = chr(letra_numero)

    for espacio in range(i * 2):
      print(end='  ')
    
    letra = 'A'
    for j in range(n-i):
      print(letra, end=' ')
      letra_numero = ord(letra) + 1
      letra = chr(letra_numero)
    print()

def consultar_usuario():
 cont = 0
 while True:
  cont += 1
  n = ingresar()
  graficos(n)
  sd = input('Desea Continuar S/N: ')
  if sd.upper() != 'S':
     break
 print(f'Se hicieron {cont} dibujos')


consultar_usuario()

