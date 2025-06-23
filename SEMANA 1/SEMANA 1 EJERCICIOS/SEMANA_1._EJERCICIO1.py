# EJERCICIO 1

"""print("Ingrese un valor de x: ")
x = float(input())
formula = x**4 + x**3 + 2*x**2 - x + 11

print("El resultado es ", formula )"""

# EJERCICIO 2

"""print("Ingrese un valor de x: ")
x = float(input())
formula = 13*x**3 + 1/2*x**1/2-x+3
print("El resultado es ", formula ) """

#EJERCICIO 3

"""a = float(input("Ingrese el valot de a: "))
b = float(input("Ingrese el valot de b: "))
c = float(input("Ingrese el valot de c: "))
expresionA= ((b * b) - (4 * a * c)) / (2 * a)
expresionB= (b * b - 4 * a * c) / (2 * a)
expresionC= b * b - 4 * a * c / 2 * a
expresionD= (b * b) - (4 * a * c / 2 * a)
expresionE= 1/2 * b
expresionF= b/2
print ("Resultado de expresion A: ", expresionA)
print ("Resultado de expresion B: ", expresionB)
print ("Resultado de expresion C: ", expresionC)
print ("Resultado de expresion D: ", expresionD)
print ("Resultado de expresion E: ", expresionE)
print ("Resultado de expresion F: ", expresionF)"""

#EJERCICIO 7
"""
try:
  seg = int(input("Ingrese la cantidad de segundos: "))
  print("Segundos Totales = ",seg)
  horas = int(seg / 3600)
  print("Horas",horas)
  minutos = int((seg % 3600) / 60)
  print("Minutos" , minutos)
  segundos = int((seg % 3600) % 60)
  print("Segundos", segundos)
except ValueError:
    print("ERROR, Ingrese un numero entero.............") """

   #EJERCICIO 8

""" try:

   far = float(input("Ingrese la temperatura en Fahrenheint: "))
   cel = (far-32)/1.8
   print("Los grados Fahrenheint ingresados ", far)
   print ("Los grados Fahreint ingresados, en Celsius es " , cel)
except ValueError:
   print("Error, ingrese solo un numero entero...........")"""


   #EJERCICIO 9

"""nombre = input("Ingrese su nombre: ")
apellidos= input("Ingrese sus apellidos: ")
try:
      edad = int( input("Ingrese su edad: "))
      print(nombre, end=' - ')
      print(apellidos, end=' - ')
      print(edad)
except ValueError:
     print("ERROR, Las edades son solo enteras.......")"""

     #EJERCICIO 10
"""
nombre = input("Ingresa su nombre: ")
apellidos = input("Ingresa su apellido: ")
try:
     edad = int ("Ingrese su edad: ")
     print("Nombre ", nombre)
     print("Apellidos ", apellidos)
     print("Edad: ", edad)
except ValueError:
    print("La edad ingresada solo es un numero entero")"""

    #EJERCICIO 11
"""
pi= 3,141592
rad= float(input("Ingresa el angulo en radianes: "))
sex= rad*180 / pi
grados = int(sex)
print("El angulo ingresado en radianes, en Sexagesimales es: " , sex)
aux1 = (sex-grados)*60
minutos = int(aux1)
aux2 = (aux1 - minutos)*60
segundos = int(aux2)

print("Minutos: ",minutos)
print("Segundos: ", segundos)"""


#EJERCICIO 12

horas = int(input("Ingrese la hora (0-23): "))
minutos = int(input("Ingrese los minutos (0-59): "))
segundos = int(input("Ingrese los segundos (0-59): ")) 
segundos += 1 
segundos = segundos % 60
minutos += segundos // 60
minutos = minutos % 60 
horas += minutos // 60
horas = horas % 24
print(f"La nueva hora es: {horas}:{minutos}:{segundos}")


 



        
 



