"""""
# PROPERTY -> Es una funcion ya implementada en el python que sirve como geters y seters 
# es una mala practica pero reemplaza el de poner set y get por clase o objeto

class Cliente1: 
    def __init__(self,dni,nombre):
        self.__nombre = nombre
        self.__dni = dni
    # get_nombre
    def get_nombre(self):
        return self.__nombre
    # get_ dni
    def get_dni(self):
        return self.__dni
    # set_nombre
    def set_nombre(self,nuevo_nombre):
        self.__nombre = nuevo_nombre
    # set_dni
    def set_dni(self,nuevo_dni):
        self.__dni = nuevo_dni

# con @property
class Cliente: 
    def __init__(self,dni,nombre):
        self.__nombre = nombre
        self.__dni = dni
    @property
    def nombre(self):
        return self.__nombre
    @property
    def dni(self):
        return self.__dni
    
    # ESA SINTAXIS PARA SETTERS CON @property
    @nombre.setter
    def nombre(self,nuevo_nombre):
        self.__nombre = nuevo_nombre
    @dni.setter
    def dni(self,nuevo_dni):
        self.__dni = nuevo_dni

p = Cliente(12345678,"Juan")
print("DATOS")
print(p.dni)
print(p.nombre)

print("ACTUALIZANDO DATOS")
p.dni = 567889
p.nombre = 'Jose'

print(p.dni)
print(p.nombre)  """

# EJERCICIO 1
"""
import math
class TroncoCono:
    def __init__(self,r1,r2,altura):
        self.__r1 = r1
        self.__r2 = r2
        self.__altura = altura
    def calcular_generatriz(self):
        return math.sqrt(math.pow(self.__altura,2) + math.pow(self.__r1 - self.__r2,2))
    
    def calcular_volumen(self):
        volumen = (math.pi * self.__altura)/3*(math.pow(self.__r1,2) + math.pow(self.__r2,2) + self.__r1 * self.__r2 )
        return volumen
    
    def calcular_area(self):
        generatriz = self.calcular_generatriz() # self.___ el metodo dentro una de misma clase a retornar -> asi se usa un metodo dentro de una misma clase
        area = math.pi * (self.__r1**2 + self.__r2**2 + generatriz*(self.__r1 + self.__r2))
        return area
    
    def __str__(self):
        print("==================================")
        return f"r1: {self.__r1} \nr2: {self.__r2} \nAltura: {self.__altura} \nVolumen: {self.calcular_volumen():.2f} \nArea: {self.calcular_area():.2f} "
        

objeto1 = TroncoCono(2,3,4)


print(objeto1)
print(f"Volumen: {objeto1.calcular_volumen():.2f}")
print(f"Area: {objeto1.calcular_area():.2f}")

objeto2 = TroncoCono(6,8,4)
objeto3 = TroncoCono(10,13,4)

print(objeto1)
print(objeto2)
print(objeto3)

"""
#EJERCICIO 2

class Laptop:
    def __init__(self,marca,chip,precioBase,pantalla='Normal'):
        self.marca = marca
        self.chip = chip
        self.precioBase = precioBase
        self.pantalla = pantalla
        self.preciofinal = 0

    def calcular_preciofinal(self):
        if self.chip == 'i5':
          return self.precioBase * 0.10
        elif self.chip == 'i7':
            return self.precioBase * 0.15
        return 0
    def precio_pantalla(self):
        if self.pantalla == 'Tactil':
            return self.precioBase*0.05
        return 0
    def preciofinal(self):
        self.preciofinal = self.precioBase + self.calcular_preciofinal() + self.precio_pantalla()
        return self.preciofinal()
    
    def __str__(self):
        return (f"Marca: {self.marca}\nChip: {self.chip}\nPantalla:{self.pantalla}\nPrecioBase:{self.precioBase}\nPrecio Final: {self.preciofinal()}")

obj1= Laptop("HP",'i3',2000,'Tactil')
obj2= Laptop("HP",'i5',2000)
obj3= Laptop("HP",'i7',2000,'Tactil')

print(obj1)
print(obj2)
print(obj3)

