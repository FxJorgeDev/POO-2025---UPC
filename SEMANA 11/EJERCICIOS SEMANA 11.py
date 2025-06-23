"""class India:
    def capital1(self):
       print(f"La capital es NUEVA DELI")
    def moneda(self):
        print( f"La moneda es el RUPIA")
    def lenguaje(self):
        print( f"El lenguaje es el HINDI")
class EEUU:
    def capital1(self):
        print( f"La capital es WASHIGTON")
    def moneda(self):
        print( f"La moneda es el DOLLAR")
    def lenguaje(self):
        print(f"El lenguaje es el INGLES")

obj_eeuu = EEUU()
obj_india = India()
for pais in (obj_eeuu,obj_india):
    pais.capital1()
    pais.moneda()
    pais.lenguaje()"""
    
#EJERCICIO 1
""""
class Bicicleta:
    lista_bici = []
    def __init__(self, material,ruedas,cantidad):
        self.__material = material
        self.__ruedas = ruedas
        self.__cantidad = cantidad
    @property
    def material (self):
        return self.__material
    @property
    def cantidad (self):
        return self.__cantidad
    @property
    def ruedas (self):
        return self.__ruedas
    def imprimir (self):
        return f"Material: {self.material}, Ruedas: {self.ruedas}, Cantidad; {self.cantidad}"
    def agregar_bici(self,bici):
        if isinstance(bici,Montaniera) or isinstance(bici,Ruta) or isinstance(bici,Urbana):
            self.lista_bici.append(bici)
            print("BICICLETA AGREGADA CON EXITO")
        else:
            print("ERROR")
    def mostrar_lista(self):
        for bici in self.lista_bici:
            print(bici)
class Montaniera(Bicicleta):
    def __init__(self, material, ruedas, cantidad,tipo):
        super().__init__(material, ruedas, cantidad)
        self.__precio_base = 1450
        if tipo == "rigidas":
            self.__tipo = 250
            self.suspension = "rigidas"
        elif tipo == "delantera":
            self.__tipo = 295
            self.suspension = "delantera"
        elif tipo == "doble":
            self.__tipo = 600
            self.suspension = "doble"
    @property
    def tipo (self):
        return self.__tipo
    @property
    def precio_base(self):
        return self.__precio_base
    def calcular_precio (self):
        return self.__precio_base + self.__tipo
    def mostrar(self):
        print(f"{super().imprimir()} Tipo de Suspension: {self.suspension}, Precio Final: {self.calcular_precio():.2f}")
    
class Ruta(Bicicleta):
    def __init__(self, material, ruedas, cantidad,tipo_m):
        super().__init__(material, ruedas, cantidad)
        self.__precio_base = 2500
        if tipo_m == "drop":
            self.__tipo_m = self.precio_base * 0.05
            self.manubrio = "Drop-Bar"
        elif tipo_m == "regular":
            self.__tipo_m = self.precio_base * 0.075
            self.manubrio = "Regular-Bar"
        
    @property
    def tipo (self):
        return self.__tipo_m
    @property 
    def precio_base (self):
        return self.__precio_base
    def calcular_precio (self):
        return self.precio_base + self.__tipo_m
    def mostrar(self):
        print(f"{super().imprimir()}, Tipo de Manubrio: {self.manubrio}, Precio FInal; {self.calcular_precio():.2f}")

class Urbana(Bicicleta):
    def __init__(self, material, ruedas, cantidad,canastilla):
        super().__init__(material, ruedas, cantidad)
        self.__precio_base = 900
        if canastilla == "si":
            self.__canastilla = 115
            self.opcion = "si"
        else:
            self.__canastilla = 0
            self.opcion = "no"
        
    @property
    def canastilla (self):
        return self.__canastilla
    @property
    def precio_base (self):
        return self.__precio_base
    def calcular_precio(self):
        return self.precio_base + self.__canastilla
    def mostrar(self):
        print(f"{super().imprimir()}, Canastilla: {self.opcion}, Precio Final: {self.calcular_precio():.2f}")

obj_1 = Montaniera("Aluminio",2,2,"delantera")
obj_2 = Montaniera("Aluminio",2,4,"doble")
obj_3 = Ruta("Aluminio",2,4,"drop")
obj_4 = Ruta("Aluminio",2,4,"regular")
obj_5 = Urbana("Aluminio",2,2,"si")
obj_6 = Urbana("Aluminio",2,4,"no")
lista = [obj_1,obj_2,obj_3,obj_4,obj_5,obj_6]
for e in lista:
    e.mostrar()
mayor = obj_1 
menor = obj_1 
for e in lista:
    if e.calcular_precio() > mayor.calcular_precio():
        mayor = e
    if e.calcular_precio() < mayor.calcular_precio():
        menor = e
print("BICICLETA CON MAYOR PRECIO")
print(mayor.calcular_precio())
print("BICICLETA CON MENOR PRECIO")
print(menor.calcular_precio()) """

# EJERCICIO 2
from random import randint
class Persona:
    def __init__(self,nombre,edad,sexo,peso,altura):
        self.__nombre = nombre
        self.__edad = edad
        self.__sexo = sexo
        self.__peso = peso
        self.__altura = altura
        self.__dni = None
        
    def generar_dni(self):
        inicio = str(randint(0,9))
        resto = str(randint(1000000,9999999))
        self.__dni = inicio + resto
        return self.__dni
    @property
    def nombre (self):
        return self.__nombre
    @property
    def dni (self):
        return self.__dni
    @property
    def edad (self):
        return self.__edad
    @property
    def sexo(self):
        return self.__sexo
    @property
    def peso(self):
        return self.__peso
    @property
    def altura(self):
        return self.__altura
    
    @sexo.setter
    def sexo (self,nuevo):
        self.__sexo = nuevo
    @peso.setter
    def altura (self,nuevo):
        self.__altura = nuevo
    
    def calcular_IMC (self):
        return (self.peso / self.altura ** 2)
    def valor_peso(self):
        if self.calcular_IMC() > 25:
            return 1
        elif self.calcular_IMC() < 18:
            return -1
        else:
            return 0
    def es_mayor(self):
        controlador = False
        if self.edad > 18:
            controlador = True
        return controlador
    def __str__(self):
        return f"Nombre: {self.nombre}, Edad: {self.edad}, DNI: {self.generar_dni()}, Sexo: {self.sexo}, Peso: {self.peso}, Altura: {self.altura}, IMC: {self.calcular_IMC()}, Es mayor: {self.es_mayor()}, Valor de Peso: {self.valor_peso()}"

obj_1 = Persona("Alex",20,"Mujer",50,1.20)
print(obj_1)