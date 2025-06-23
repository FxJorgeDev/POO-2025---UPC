#EJERCICIOS DE CLASES SEMANA 4.2

#EJERCICIO 1

""""
alumnos = {}

cantidad = int(input('Ingrese la cantidad de alumnos: '))

for num in range(cantidad):
    nombre = str(input('Nombre del alumno: '))
    while nombre in alumnos:
        print('Alumno ya existe')
        nombre = str(input('Nombre del alumno: '))
    notas = []
    nota = int(input('Ingrese la nota del alumno: '))
    while nota >= 0:
        notas.append(nota)
        nota = int(input('Ingrese la nota del alumno: '))
    alumnos[nombre] = notas.copy()    

for nombre,notas in alumnos.items():
    print(" %s ha obtenido de promedio de %f " % (nombre, sum(notas)/len(notas)))"""

#EJERCICIO 2
"""""
agenda = {}
while True:
    print('\n ')
    print('1. Agregar/Modificar ')
    print('2. Buscar')
    print('3. Borrar')
    print('4. Listar')
    print('5. Salir')

    opcion = int(input('INGRESE LA OPCION: '))
    if opcion == 1:
        nombre = input('Ingrese el nombre: ')
        if nombre in agenda:
            print('%s ya existe y su telefono es %s' %(nombre,agenda[nombre]))
            opcion = input('Presiona s si quieres modificar, Otra tecla para continuar....')
            if opcion == 's':
                numero = input('Ingrese nuevo numero: ')
                agenda[nombre] = numero
        else:
                numero = input('Ingrese el numero: ')
                agenda[nombre] = numero
    elif opcion == 2:
        cadena = input('inicial del nombre de la persona a buscar: ')
        for nombre,numero in agenda.items():
            if nombre.startswith(cadena):
                print('Numero de telefono de %s es el %s ' % (nombre,agenda[nombre]))
    elif opcion == 3:
        nombre = input('Nombre a borrar: ')
        if nombre in agenda:
            opcion = input('Presione s para borrar, otra letra para continuar....')
            if opcion == 's':
                del agenda[nombre] 
        else:
            print('NO EXISTE LA PERSONA....')
    elif opcion == 4:
        for nombre, numero in agenda.items():
            print(nombre, '->', numero)
    elif opcion == 5:
        break
    """

#EJERCICIO TOPOS CON MATRICES

import random

matriz = []

for f in range(10):
    lista = []
    for c in range(15):
        lista.append(random.randint(1,3))
    matriz.append(lista)

for f in range(10):
    for c in range(15):
        print(matriz[f][c], ' ', end= '')
    print()
frecuencia = []

for cultivos in range(1,4):
    contador = 0
    for f in range(10):
        for c in range(15):
            if matriz[f][c] == cultivos:
                contador += 1
    frecuencia.append(contador)

maximo = max(frecuencia)
minimo = min(frecuencia)
print(frecuencia)
print('Cultivo que mas se repite: ')
for i in range(3):
    if frecuencia[i] == maximo:
        print(i+1)
print('Cultivo que menos se repite: ')
for i in range(3):
    if frecuencia[i] == minimo:
        print(i+1)
    
print('Guarida de topo: ')

for f in range(1,9):
    for c in range (1,14):
        if matriz[f][c-1] == 2 and matriz[f][c+1] == 2 and matriz[f-1][c] == 3 and matriz[f+1][c] == 1:
            print('Fila ', f ,' Columna',c) 

#EJERCICIO EXTRA
""""
cadena = str(input("Ingrese la cadena a leer: "))
diccionario = {}
cont1 = -1
for char in cadena:
    if char == diccionario:
       diccionario[char] += 1
    else:
        diccionario[char] = 1

for char,repeticiones in diccionario.items():
    print(char, '->', repeticiones)"""

#EJERCICIO 3 SEMANA 4
"""
texto = str( '¡ El joven iba caminando por la calle, cuando de pronto se tropezó con algo de gran tamaño a la altura de sus rodillas!.  ' \
'Miró para abajo y se encontró con algo que no esperaba: un gran baúl de madera. ¿Quién habría dejado un baúl de esas características en medio de la calle...? Al instante, miles de pensamientos le vinieron a la cabeza: "Me pregunto si se lo habrán olvidado o ' \
'lo habrán abandonado voluntariamente; el dueño podría ser un médico, o un mago, o un anticuario; no sé si lo estarán buscando o ya lo darán por perdido; y lo más importante: ¡muero por saber qué tiene adentro!”. Después de mucho meditar '
'-sin dejar de mirar el baúl en ningún momento-, decidió seguir camino (haría de cuenta que nunca lo había visto):')




def general(texto):
    texto1 = str(texto.lower())
    print(texto1)

    signosletras = ['.',',','!','¡',',',':',';']
    texto2 = []
    for palabras in texto:
        for signo in signosletras:
            if signo == palabras: 
                 texto2.append(palabras)
            else:
                continue
    texto2.append(palabras)
    print(texto2)


print("\nTEXTO SIN SIGNOS DE PUNTUACION \n",general(texto))

"""