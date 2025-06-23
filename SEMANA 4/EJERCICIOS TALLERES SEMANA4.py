#EJERCICIO 1 TALLER
"""""
def menu():
  print("1: Añadir")
  print("2: Actualizar el puesto y salario ")
  print("3: Calcular el salario anual de un empleado")
  print("4: Mostrar la lista de empleados")
  print("5: Salir")
  opcion = -1
  while opcion < 1 or opcion > 5:
    try:
      opcion = int(input("Ingrese una opción: "))
    except:
      print("Opción inválida")
  return opcion

def agregar():
  dni = input("Ingrese el DNI del empleado: ")
  nombre = input("Ingrese el nombre del empleado: ")
  edad = int(input("Ingrese la edad del empleado: "))
  puesto = input("Ingrese el puesto del empleado: ")
  salario = float(input("Ingrese el salario del empleado: "))

  diccionario_empleados[dni] = {"nombre": nombre, "edad": edad, "puesto": puesto, "salario": salario}

def actualizarPuestoSalario():
  dni = input("Ingrese el DNI del empleado: ")
  if dni in diccionario_empleados.keys():
    puesto = input("Ingrese el nuevo puesto del empleado: ")
    salario = float(input("Ingrese el nuevo salario del empleado: "))
    diccionario_empleados[dni]["puesto"] = puesto
    diccionario_empleados[dni]["salario"] = salario
  else:
    print("Empleado no encontrado")

def calcularSalarioAnual():
  dni = input("Ingrese el DNI del empleado: ")
  if dni in diccionario_empleados.keys():
    salario = diccionario_empleados[dni]["salario"]
    salarioAnual = salario * 12
    if diccionario_empleados[dni]["edad"] > 50:
      salarioAnual *= 50
    print(f"El salario anual del empleado es: {salarioAnual}")
  else:
    print("Empleado no encontrado")

def listar():
  for clave,valor in diccionario_empleados.items():
    print(clave,valor)

def listarOrdenado():
  lista = list()
  for clave,valor in diccionario_empleados.items():
    aux = [valor["nombre"],valor["salario"],"Sin Bono"]
    if valor["edad"] > 50:
      aux[-1] = "Con Bono"
    lista.append(aux)# añadiendo una lista

  lista.sort()
  for l in lista:
    print(l)


def main():
  opcion = -1
  while opcion != 5:
    opcion = menu()
    if opcion == 1:
      agregar()
    elif opcion == 2:
      actualizarPuestoSalario()
    elif opcion == 3:
      calcularSalarioAnual()
    elif opcion == 4:
      listar()



diccionario_empleados = {}
opcion = -1
main()
listarOrdenado()"""

#EJERCICIOS PRACTICA
"""""
num = []
while True:
    numero = int(input('Ingrese un numero entero positivo: '))
    if numero > 0:
        num.append(numero)
    else:
        break
print(len(num))
print(num[-1])
print(num[::-1])     
if 5 in num:
    print('SI')
else:
    print('NO')
print(f"La cantidad de 5 es {num.count(5)}")"""
#EJERCICIO 7 SEMANA 3.02
""""
dnis = []
codes = []
while True:
  opcion = str(input('Desea continuar s/n:'))
  if opcion != 'n':
    dni = int(input('Ingrese DNI:'))
    while True:
      codigo = int(input('Ingrese codigo de suministro: '))
      if codigo > 99999 and codigo < 1000000:
        dnis.append(dni)
        codes.append(codigo)
        print('REGISTRADO')
        print()
        break
      else:
        print('ERROR CODE')
  else:
    break
print('N \t DNI \t CODIGO \n')
for i,dni in enumerate(dnis,1):
  print(i,'\t',dnis[i-1],'\t',codes[i-1])"""

#EJERCICO 6 SEMANA 3.02
"""

def menu():

  print('MENU DE OPCIONES  \n')
  print('[1] Pulgadas')
  print('[2] Yardas')
  print('[3] Millas')
  print('[4] Milimetros')
  print('[5] Centimetros')
  print('[6] Metros')
  print('[7] Resumen')
  print('[8] Salir')

def conver():
  pies = [] 
  opcion = -1
  medida = []
  convertido = []
 
  while True: 
    opcion = int(input('Ingrese su opcion: '))
    if opcion != 7:
     dato = float(input('Ingrese la medida: '))
     match opcion:
      case 1:
       print(dato * 12)
       convertido.append(dato*12)
       pies.append(dato)
       medida.append('Pulgadas')
      case 2:
       print(dato*0.33)
       convertido.append(dato*0.33)
       pies.append(dato)
       medida.append('Yardas')
      case 3:
       print(dato*0.0002)
       convertido.append(dato*0.0002)
       pies.append(dato)
       medida.append('Millas')
      case 4:
       print(dato*305.8)
       convertido.append(dato*305.8)
       pies.append(dato)
       medida.append('Milimetros')
      case 5:
       print(dato*30.48)
       convertido.append(dato*30.48)
       pies.append(dato)
       medida.append('Centimetros')
      case 6:
       print(dato*0.3048)
       convertido.append(dato*0.3048)
       pies.append(dato)
       medida.append('Metros')
      case 8:
        break
    else: 
      print('Nro\tPies\tConvertir a \t Convertido \n')
      for i,pie in enumerate(pies,1):
         print(f" {i} \t {pies[i-1]} \t {medida[i-1]} \t{convertido[i-1]} \n ")

opcion = -1
menu()
conver()"""""

#EJERCICIO 9 SEMANA 3.02
""""
from random import randint

numeros = []
for i in range(50):
    numeros.append(randint(1,11))
print(numeros)
print()
print('NUMERO \t FRECUENCIA')
for numero in numeros:
    print(f'  {numero} \t {numeros.count(numero)}')"""
#EJERCICIO 2 SEMANA 3.03
"""""
# Pedimos al usuario ingresar el número de términos
N = int(input("Ingrese N: "))

# Inicializamos la suma
suma = 0

# Calculamos la suma con signos alternados
for i in range(N):
    termino = ((-1) ** i) * (1 / (2 ** i))
    suma += termino

# Mostramos el resultado
print("La suma es:", suma)"""


#EJERCICIO 5 SEMANA 3.03
"""""
n = int(input('Ingrese N: '))
caracter = str(input('Ingrese caracter: '))

for i in range(n):
    for j in range(i-1,n-1):
        print(caracter,end=' ')
    print()"""

#EJERCICIO 3 SEMANA 4.0
"""
texto = str("¡ El joven iba caminando por la calle, cuando de pronto se tropezó con algo de gran tamaño a " 
"la altura de sus rodillas!. Miró para abajo y se encontró con algo  que no esperaba: un gran baúl de madera. ¿Quién habría dejado un baúl de \
esas características en medio de la calle...? Al instante, miles de pensamientos\
le vinieron a la cabeza: Me pregunto si se lo habrán olvidado o lo habrán\
abandonado voluntariamente; el dueño podría ser un médico, o un mago, o un\
anticuario; no sé si lo estarán buscando o ya lo darán por perdido; y lo más\
importante: ¡muero por saber qué tiene adentro!”. Después de mucho meditar\
-sin dejar de mirar el baúl en ningún momento-, decidió seguir camino (haría de\
cuenta que nunca lo había visto).")

def funciones(texto):
    signoletras = ['.',',',':',';',"!","¡"]
    txt = []
    txt.append(texto)
    texto2 = texto.lower
    print(texto2)
    print()
    for palabra in texto:
        for i in signoletras:
            if palabra == signoletras:
                txt.pop(i)

    print(txt)
    
funciones(texto)"""

#EJERCICIO 2 SEMANA 4.0
""""
def menu():

  print('MENU DE OPCIONES  \n')
  print('[1] Pulgadas')
  print('[2] Yardas')
  print('[3] Millas')
  print('[4] Milimetros')
  print('[5] Centimetros')
  print('[6] Metros')
  print('[7] Resumen')
  print('[8] Salir')

def conver(resultados):
  opcion = -1
  resultados = {}
  while True: 
    opcion = int(input('Ingrese su opcion: '))
    if opcion != 7:
     dato = float(input('Ingrese la medida: '))
     resultados['id'][0] = 1
     match opcion:
        case 1:
         print(dato * 12)
         resultados['Convertido']['id'] = dato*12
         resultados['medida']['id'] = 'Pulgadas'
        case 2:
         print(dato*0.33)
         resultados['Convertido']['id'] = dato*0.33
         resultados['medida']['id'] = 'Yardas'
        case 3:
         print(dato*0.0002)
         resultados['Convertido']['id'] = dato*0.0002
         resultados['medida']['id'] = 'Millas'
        case 4:
          print(dato*305.8)
          resultados['Convertido']['id'] = dato*305.8
          resultados['medida']['id'] = 'Milimetros'
        case 5:
         print(dato*30.48)
         resultados['Convertido']['id'] = dato*30.48
         resultados['medida']['id'] = 'Centimetros'
        case 6:
         print(dato*0.3048)
         resultados['medida']['id'] = 'Metros'
         resultados['Convertido']['id'] = dato*0.3048
        case 8:
         break
     
    
    else: 
     print(resultados)
menu()
resultados = {}
conver()
print()
"""

#EJERCICIO 1 SEMANA 4.02
"""""
nombres = []
resultados = {}
cantidad = int(input('Ingrese la cantidad de alumnos:'))
for numero in range(cantidad):
   alumno = input('Ingrese el nombre del alumno: ')
   nota = int(input('Ingrese nota del alumno:'))
   notas = []
   while nota >= 0:
      nota = int(input('Ingrese nota del alumno:'))
      notas.append(nota)
      nombres.append(alumno)
for alumno in nombres:
    resultados[alumno] = resultados.get(alumno)
resultados[alumno] = notas.copy()

for nombre, nota in resultados.items():
  print(f"Alumno %s de promedio %f " % (nombre,sum(notas)/len(notas)))"""


#EJERCICIO 4 TALLER PROGRA

import re

def imprimir(texto):
  print('============================')
  print(texto)

def eliminarSignoPuntuacion(texto):
  texto = re.sub(r'[^\w\s]', '', texto)
  imprimir(texto)
  return texto

def convertirTodoMinuscula(texto):
  texto = texto.lower()
  imprimir(texto)
  return texto

def contarApariciones():
  diccionario = {}
  lista = texto.split()
  for palabra in lista:
    diccionario[palabra] = diccionario.get(palabra,0)+1
  print(f'Cantidad por palabra: {diccionario}')
  
  return diccionario

def ordenarPoApariciones(diccionario):
  lista = list()
  for clave,valor in diccionario.items():
    if valor > 1:
      lista.append((valor,clave))

  lista.sort(reverse=True)
  for valor,clave in lista:
    print(clave,valor)


texto = """
¡ El joven iba caminando por la calle, cuando de pronto se tropezó con algo de
gran tamaño a la altura de sus rodillas!. Miró para abajo y se encontró con algo
que no esperaba: un gran baúl de madera. ¿Quién habría dejado un baúl de
esas características en medio de la calle...? Al instante, miles de pensamientos
le vinieron a la cabeza: "Me pregunto si se lo habrán olvidado o lo habrán
abandonado voluntariamente; el dueño podría ser un médico, o un mago, o un
anticuario; no sé si lo estarán buscando o ya lo darán por perdido; y lo más
importante: ¡muero por saber qué tiene adentro!”. Después de mucho meditar
-sin dejar de mirar el baúl en ningún momento-, decidió seguir camino (haría de
cuenta que nunca lo había visto)
"""

imprimir(texto)
texto = eliminarSignoPuntuacion(texto)
texto = convertirTodoMinuscula(texto)
diccionario = contarApariciones()
print()
print('ORDENADO POR APARICIONES \n ============')
ordenarPoApariciones(diccionario)