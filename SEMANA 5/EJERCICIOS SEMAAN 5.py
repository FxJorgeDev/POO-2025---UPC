#EJERCICIO 1
""""
numeros = []

while True:
 num = int(input('Ingrese numero: '))
 if num != 0 and num > 0:
  numeros.append(num)
 else:
  print('ERROR...')
  for pos in range(0,len(numeros)):
   for j in range(len(numeros)-pos-1):
    if numeros[j] > numeros[j+1]:
     aux = numeros[j]
     numeros[j]=numeros[j+1]
     numeros[j+1] = aux
 if num == 0:
  break

print(numeros)"""



#EJERCICIO 2

texto = str(input('Ingrese Texto: '))

recuentos = {}

for palabra in texto:
    if palabra in recuentos:
        recuentos[palabra] +=1
    else:
        recuentos[palabra] = 1

for palabra,repeticiones in recuentos.items():
    print(f"{palabra*repeticiones, "==" ,{repeticiones}}")