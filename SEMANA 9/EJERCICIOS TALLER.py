""""
class Telefono:
    lista = [] # es una forma de guardar datos dentro de la misma clase
    # se llamada Atributos de clase
    def __init__(self,marca,modelo,color):
        self.marca = marca # lo que esta dentro del constructor son atriubutos de instancia
        self.modelo = modelo
        self.color = color
    def __str__(self):
        return(f"Marca: {self.marca} Modelo: {self.modelo} Color: {self.color}")
    def agregar(self,obj_telefono):
        self.lista.append(obj_telefono)
    def imprimir(self):
        for elemento in self.lista:
            print(elemento)"""

#EJERCICIO 1
""""
class Encomienda:
    __base = {}
    def __init__(self,codigo,remitente,destinatario,direccion,peso,volumen,costo_peso,costo_volumen):
        self.__codigo = codigo
        self.__remitente = remitente
        self.__destinatario = destinatario
        self.__direccion = direccion
        self.__peso = peso
        self.__volumen = volumen
        self.__costo_peso = costo_peso
        self.__costo_volumen = costo_volumen
    @property
    def codigo (self):
        return self.__codigo
    @property
    def remitente (self):
        return self.__remitente
    @property
    def destinatario (self):
        return self.__destinatario
    @property
    def direccion (self):
        return self.__direccion
    @property
    def peso (self):
        return self.__peso
    @property
    def volumen (self):
        return self.__volumen
    @property
    def costo_peso (self):
        return self.__costo_peso
    @property
    def costo_volumen (self):
        return self.__costo_volumen
    def __str__(self):
        return f"{self.codigo} {self.remitente} {self.destinatario}{self.direccion}{self.peso}{self.volumen}{self.__costo_peso}{self.__costo_volumen}"
    
    @codigo.setter
    def codigo(self,nuevo):
        self.__codigo = nuevo
    def imprimir(self):
        print(self.codigo)
        print(self.remitente)
        print(self.destinatario)
        print(self.direccion)
        print(self.peso)
        print(self.volumen)
        print(self.__costo_peso)
        print(self.__costo_volumen)
        print(f"costo por envio: {self.valor_envio()}")
    def costo_peso(self):
       return self.__peso * self.__costo_peso
    def costo_volumen(self):
        return self.__volumen * self.__volumen
    def valor_envio(self):
        return self.costo_volumen() + self.costo_peso()
    def agregar(self,objeto):
        self.__base [self.__codigo] = objeto
    def mostrar(self):
        for clave, valor in self.__base.items():
            print(f"====={clave}=====")
            valor.imprimir()

obje1 = Encomienda(123,'jorge','nicol','smp',3,5,7,2)
obje2 = Encomienda(13,'nicol','Jorge','chorillos',10,5,8,2)
obje1.agregar(obje1)
obje2.agregar(obje2)
obje1.mostrar() """


#EJERCICIO 2
""""
class Terreno:
    __datos = {}
    contador = 0
    @classmethod
    def datos (self):
        return self.__datos
    def __init__(self,id,ubi,area,valor_c,valor_p):
        self.__id = id
        self.__ubi = ubi
        self.__area = area
        self.__valor_c = valor_c
        self.__valor_p = valor_p
    @property
    def id (self):
        return self.__id
    @property
    def ubi(self):
        return self.__ubi
    @property
    def area (self):
        return self.__area
    @property
    def valor_c (self):
        return self.__valor_c
    @property
    def valor_p (self):
        return self.__valor_p
    
    @id.setter
    def id(self,nuevo):
        self.__id = nuevo
    @area.setter
    def area(self,nuevo):
        self.__area = nuevo
    @valor_c.setter
    def valor_c (self,nuevo):
        self.__valor_c = nuevo
    @valor_p.setter
    def valor_p (self,nuevo):
        self.__valor_p = nuevo

    def valor_predial(self):
        return self.__area *self.__valor_p 
    def valor_comercial(self):
        return self.__area *self.__valor_c
    def margen_ganancia(self):
        return self.valor_comercial() + self.valor_predial()  
    def agregar(self,obj):
        if obj.id in self.__datos:
            print("EL CODIGO YA EXISTE")
        else:
           Terreno.__datos[self.id] =  obj
           Terreno.contador += 1
           print("AGREGADO")
    def imprimir(self):
        print(self.ubi)
        print(self.area)
        print(self.valor_c)
        print(self.valor_p)
        print(f"Valor Predial: {self.valor_predial()}")
        print(f"Valor Comercial: {self.valor_comercial()}")
        print(f"Margen de Ganancia: {self.margen_ganancia()}")
    def mostrar(self):
        for clave,valor in Terreno.__datos.items():
            print(f"==== {clave} =====")
            valor.imprimir()

terreno1 = Terreno(123,"Chorillos",30.3,10,4)
terreno2 = Terreno(123,"SMP",30.3,10,4)
terreno1.agregar(terreno1)
terreno2.agregar(terreno2)
terreno1.mostrar()
print(f"En total se registraron: {Terreno.contador} terrenos") """

#EJERCICIO 3

from random import randint,choice
class Vuelo:
    __pasajero_turista = []
    __pasajero_clase = []
    conta_clase = 0
    conta_turista = 0
    conta_pasajero = 0
    conta_turistap = 0
    def __init__(self,numero_v:int,hora_s:str,hora_l:str,ciudad_s:str,ciudad_l:str):
        self.__numero_v = numero_v
        self.__hora_s = hora_s
        self.__hora_l = hora_l
        self.__ciudad_s = ciudad_s
        self.__ciudad_l = ciudad_l
    @property
    def numero_v (self):
        return self.__numero_v
    @property
    def hora_s(self):
        return self.__hora_s
    @property
    def hora_l(self):
        return self.__hora_l
    @property
    def ciudad_s(self):
        return self.__ciudad_s
    @property
    def ciudad_l(self):
        return self.__ciudad_l
    
    @numero_v.setter
    def numero_v(self,nuevo):
        self.__numero_v = nuevo

    def agregar_pasajeros_turistas(self,pasajero):
        if len(self.__pasajero_turista) != 52:
            Vuelo.__pasajero_turista.append(pasajero)
            Vuelo.conta_turistap += 1
            Vuelo.conta_turista += pasajero.edad
            print("PASAJERO - CLASE TURISTA - REGISTRADO")
        else:
            print("PASAJES DE CLASE TURISTA LLENOS")
    def agregar_pasajeros_clase(self,pasajero):
        if len(self.__pasajero_clase) != 8:
           Vuelo.__pasajero_clase.append(pasajero)
           Vuelo.conta_pasajero += 1
           Vuelo.conta_clase += pasajero.edad
           print("PASAJERO - PRIMERA CLASE - REGISTRADO")
        else:
            print("PASAJES DE PRIMERA CLASE LLENOS")
    def mostrar(self):
        for pasajero in self.__pasajero_turista:
            pasajero.mostrar_datos()
        for pasajero in self.__pasajero_clase:
            pasajero.mostrar_datos()
    def datos_vuelo(self):
        print()
        print("===== DATOS DEL VUELO ===== ")
        print(f"Numero de Vuelo: {self.numero_v}")
        print(f"Hora de Salida: {self.hora_s}")
        print(f"Hora de Llegada: {self.hora_l}")
        print(f"Ciudad de Salida: {self.ciudad_s}")
        print(f"Ciudad de Llegada: {self.ciudad_l}")
        print()
        print("=== DATOS DE PASAJEROS ===== ")
    def promedio_clase(self):
        print(f"Cantidad de Pasajeros Primera Clase: {Vuelo.conta_pasajero}")
        print(f"Suma de Edades de Pasajeros Primera Clase: {Vuelo.conta_clase}")
        return f"Promedio de edad de los Pasajeros de Primera: {Vuelo.conta_clase / Vuelo.conta_pasajero:.2f}"
    def promedio_turista(self):
        print(f"Cantidad de Pasajeros Clase Turista: {Vuelo.conta_turistap}")
        print(f"Suma de Edades de Pasajeros Clase Turista: {Vuelo.conta_turista}")
        return f"Promedio de edad de los Pasajeros de Clase Turista: {Vuelo.conta_turista / Vuelo.conta_turistap:.2f}"
class Pasajero:
    def __init__(self,nombre,edad,tipo_v):
        self.__nombre = nombre
        self.__edad = edad
        self.__tipo_v = tipo_v
    @property
    def nombre(self):
        return self.__nombre
    @property
    def edad(self):
        return self.__edad
    @property
    def tipo_v(self):
        return self.__tipo_v
    def mostrar_datos(self):
        print(f"Nombre Pasajero: {self.nombre}")
        print(f"Edad: {self.edad}")
        print(f"Tipo de Vuelo: {self.tipo_v}")
        print()

Vuelo1 = Vuelo(123,"10:30","12:00","Lima","Buenos Aires")
nombres = ["Jhon","Nicol","Nils","Valentin","Alex","Elias","Alexis","Atilio","Yadira"]
cantidad = int(input("Ingresa la capacidad de Asientos del Avion: "))

for i in range(cantidad):
    nombre = choice(nombres)
    edad = randint(18,65)
    tipo_vuelo = randint(1,2)
    if tipo_vuelo == 1:  
        if len(Vuelo1._Vuelo__pasajero_clase) < 8:
            pasajero = Pasajero(nombre, edad, "Primera Clase")
            Vuelo1.agregar_pasajeros_clase(pasajero)
        elif len(Vuelo1._Vuelo__pasajero_turista) < 52:
            pasajero = Pasajero(nombre, edad, "Clase Turista")
            Vuelo1.agregar_pasajeros_turistas(pasajero)
        else:
            print("TODOS LOS ASIENTOS ESTÁN LLENOS")
            break
    else:  
        if len(Vuelo1._Vuelo__pasajero_turista) < cantidad - 8:
            pasajero = Pasajero(nombre, edad, "Clase Turista")
            Vuelo1.agregar_pasajeros_turistas(pasajero)
        else:
            print("PASAJES DE CLASE TURISTA LLENOS")

Vuelo1.datos_vuelo()
Vuelo1.mostrar()
print()
print(Vuelo1.promedio_clase())
print()
print(Vuelo1.promedio_turista())