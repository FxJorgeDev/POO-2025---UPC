  #EJERCICIO 1
""""
n = 8
if n % 2:
    print("EL numero es impar")
else:
    print("EL numero es par")"""
#EJERCICIO 2
""""
def invertir(num):
 num1 = str(num)
 num2 = num1[::-1]
 num3= int(num2)
 return num3

try:
 a = int(input("Ingrese el primer numero: "))
 b = int(input("Ingrese el primer numero: "))
except:
 print("ERROR, solo numeros enteros....")

if a > 99 and b > 99 :
  print("Unidad1: ", (a % 10))
  print("Decena1: ", ((a // 100) % 10) )
  print("Centena1: ", (a // 100))
 
  print("Unidad2: ", (b % 10))
  print("Decena2: ", ((b // 100) % 10) )
  print("Centena2: ", (b // 100))

  print(a, ' y ', invertir(a))
  print(b, ' y ', invertir(b))

  print(a,'+',b,'=', a + b)
  print(invertir(b),'+',invertir(a),'=', invertir(a) + invertir(b))

  print(a,invertir(b))
else:
 print("Los numeros tiene que de 3 cifras....")"""

#EJERCICIO 3
"""
try:
 arista = float(input("Ingrese la Arista del tetraedro: "))
except:
 print("Ingrese solo numeros....")

if arista > 0:
 area = (arista**2) * (3**0.5)
 print("Area: ",area)
 volumen = ((2**0.5) / 12)*arista**3
 print('Volumen:',volumen)
else:
 print("ERROR...")"""

# range(inicio,final,paso)
# al final tampoco toma el ultimo valor igual que el slicing

#EJERCICIO 5
""""
salario = float(input("Ingrese el salario mensual: "))
personas = int(input("Ingrese el numero de personas a cargo: "))
if personas == 1:
    if salario <= 500:
        linea = 'PREPAGO'
    elif salario > 500:
        salario = 'POSTPAGO'
elif personas >= 2 and personas <= 4:
    if salario <= 750:
        linea = 'PREPAGO'
    else: 
        linea =  'POSTPAGO'
else:
    if salario <= 1000:
        linea = 'PREPAGO'
    else:
        linea = 'POSTPAGO'

print("Tipo de linea al que puede acceder: ", linea) """

#EJERCICIO9
""""
try:
 clase = str(input("Clase de bus elegido: "))
except:
 print("ERROR..")

match clase:
 case 'economico':
  preciokm = (1.5)
 case 'medio':
  preciokm = (2.5)
 case 'lujo':
  preciokm = (3.5)
print("Precio x km de viaje: ",preciokm)
try:
 km = float(input("Numero de km del viaje: "))
 personas = int(input("Numero de personas reales: "))
except:
  print("ERROR")

if personas < 25:
 costo = (25.0 * preciokm) * km
 partes = costo/personas
else:
 costo = (personas*preciokm) * km
 partes = costo / personas

print("EL costo total por el viaje: ",costo)
print("El costo por persona: ", partes) """

#EJERCICIO 10

while True:
 costo = float(input("Ingrese el costo de la materia prima: "))
 codigo = str(input("Ingrese el codigo del (1,2,3,4,5,6): "))
 match codigo:
   case '1': 
    costomano = costo*0.80
   case '2':
    costomano = costo*0.85
   case '3':
    costomano = costo*0.75
   case '4':
    costomano = costo*0.75
   case '5':
    costomano = costo*0.80
   case '6':
    costomano = costo*0.85

 match codigo:
   case '1': 
    gastofab = costo*0.28
   case '2':
    gastofab = costo*0.30
   case '3':
    gastofab = costo*0.35
   case '4':
    gastofab = costo*0.28
   case '5':
    gastofab = costo*0.30
   case '6':
    gastofab = costo*0.35
 costopro = costo + costomano + gastofab 
 pv = costopro + (costopro*0.45)
 print("Costo mano de obra: ", costomano)
 print("Gasto de fabricacion: ", gastofab)
 print("Costo de produccion: " , costopro)
 print("Precio de venta: ", pv)
