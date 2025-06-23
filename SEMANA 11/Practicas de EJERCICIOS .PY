from abc import ABC, abstractmethod
class Atack:
    @abstractmethod
    def atacar (self):
        pass
class Cuartel:
    def __init__(self,codigo:str,nombre:str):
        self.__codigo = codigo
        self.__nombre = nombre
        self.__unidades = []
    def agregar_unidad(self,unidad:Atack):
        if isinstance(unidad,Atack):
            self.__unidades.append(unidad)
        else:
            print("se esperaba una clase unidad como variable")
    @property
    def codigo (self):
        return self.__codigo
    @property
    def nombre (self):
        return self.__nombre
    def mostrar_unidades (self):
        print(f"\nCuartel:{self.nombre}")
        print("Unidades Asignadas:")
        for unidad in self.__unidades:
            print(f" {unidad} - Ataque: {unidad.atacar()}")
    def calcular_capa (self):
        total = 0
        cont = 0
        for unidad in self.__unidades:
            if isinstance(unidad,Soldado):
                total += unidad.grado
                cont += 1
        if cont == 0:
            print("ERROR DIVISION ENTRE O")
        else:
            return total / cont
class Soldado(Atack):
    def __init__(self,nombre:str,grado:int):
        self.__nombre = nombre
        self.__grado = grado
    @property
    def nombre (self):
        return self.__nombre
    @property
    def grado (self):
        return self.__grado
    def atacar (self):
        return "piu"
    def __str__(self):
        return f"Soldado: {self.nombre} Grado: {self.grado}"
class Tanque(Atack):
    def __init__(self,modelo:str,torreta):
        self.__modelo = modelo
        self.__torreta = torreta
    @property
    def modelo (self):
        return self.__modelo
    def atacar (self):
        return "pow"
    def __str__(self):
        return f"Tanque Modelo: {self.modelo} con {self.__torreta}"
class Torreta:
    def __init__(self,modelo_t,tipo):
        self.__modelo =  modelo_t
        self.__tipo = tipo
    @property
    def modelo (self):
        return self.__modelo
    @property
    def tipo (self):
        return self.__tipo
    def __str__(self):
        return f"Modelo: {self.modelo} y tipo de municion {self.tipo}"

torreta1 = Torreta("M1A1", "Explosiva")
tanque1 = Tanque("Abrams", torreta1)
soldado1 = Soldado("Juan", 8)
soldado2 = Soldado("Pedro", 5)

cuartel = Cuartel("BR-01", "Fuerte Amazonas")
cuartel.agregar_unidad(tanque1)
cuartel.agregar_unidad(soldado1)
cuartel.agregar_unidad(soldado2)

soldado2 = Soldado("Pedro", 4)
soldado3 = Soldado("Juan", 1)
tanque2 = Tanque("M1 Abrams", Torreta("T100", "Explosiva"))
cuartel1 = Cuartel("BR01", "Fuerte Lima")
cuartel1.agregar_unidad(soldado1)
cuartel1.agregar_unidad(tanque2)
cuartel1.agregar_unidad(soldado2)
cuartel1.agregar_unidad(soldado3)

cuartel.mostrar_unidades()
print(f"Capacidad total de ataque (soldados): {cuartel.calcular_capa():.2f}")
cuartel1.mostrar_unidades()
print(f"Capacidad total de ataque (soldados): {cuartel1.calcular_capa():.2f}")