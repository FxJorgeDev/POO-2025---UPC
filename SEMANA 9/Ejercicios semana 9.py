"""class Cuenta:
    def __init__(self,num:int,saldo:float):
       self.__num = num      
       self.__saldo = saldo
    def get_num(self):
            return self.__num
    def get_saldo(self):
            return self.__saldo
    def set_num(self,nuevo):
            self.__num = nuevo
    def deposito(self,nuevo):
            self.__saldo += nuevo
    def retiro(self,nuevo):
            self.__saldo -= nuevo
    def __str__(self):
        return (f"N° Cuenta: {self.__num} Saldo: {self.__saldo}")

class Banco:
    def __init__(self,nombre:str):
        self.__nombre = nombre
    def get_nombre(self):
        return self.__nombre
    def transferir(self,ctaO,ctaD,monto):
        if ctaO.get_saldo() < monto:
            print("Saldo insuficiente...")
        else:
            ctaD.deposito(monto)
            ctaO.retiro(monto)
            print("TRANSFERENCIA EXITOSA")

    def get_transferir(self):
        return self.__transferir
bank = Banco("BCP")
cuenta1 = Cuenta(12345678,500)
cuenta2 = Cuenta(87654321,1000)
print(cuenta1)
print(cuenta2)
monto = float("Ingrese Monto a Transferir: ")
bank.transferir(cuenta1,cuenta2,monto)
print(cuenta1)
print(cuenta2)
print(bank.get_transferir)"""



""""

class Cuenta:
    def __init__(self,num:int,saldo:float):
       self.__num = num      
       self.__saldo = saldo
    @property
    def num(self):
            return self.__num
    def saldo(self):
            return self.__saldo
    def retiro(self,nuevo):
            self.__saldo -= nuevo
    def deposito(self,nuevo):
            self.__saldo += nuevo
    def __str__(self):
        return (f"N° Cuenta: {self.__num} Saldo: {self.__saldo}")

class Banco:
    def __init__(self,nombre:str):
        self.__nombre = nombre
    @property
    def nombre(self):
        return self.__nombre
    
    def transferir(self,ctaO,ctaD,monto):
        if isinstance(ctaO, Cuenta) and isinstance(ctaD,Cuenta):
            if ctaO.saldo() < monto:
             print("Saldo insuficiente...")
            else:
                ctaD.deposito(monto)
                ctaO.retiro(monto)
                print("TRANSFERENCIA EXITOSA")
        else:
            print("ERROR DE TIPO CLASES")

    
bank = Banco("BCP")
cuenta1 = Cuenta(12345678,500)
cuenta2 = Cuenta(87654321,1000)
print(cuenta1)
print(cuenta2)
monto = float(input("Ingrese Monto a Transferir: "))
bank.transferir(cuenta1,bank,monto)
print(cuenta1)
print(cuenta2)

            
    """


#EJERCICIO 4 CLASE SEMANA 09-10-11

class Representante:
    def __init__(self,dni:str,edad:int,hijos:int,ingresos:float,propiedad:float):
     self.__dni = dni
     self.__hijos = hijos
     self.__ingresos= ingresos
     self.__propiedad = propiedad
     self.__edad = edad
     self.__calificacion = edad + hijos + ((ingresos) / propiedad + 1)
    @property
    def dni (self):
       return self.__dni
    @property
    def hijos(self):
       return self.__hijos
    @property
    def edad(self):
       return self.__edad
    @property
    def ingresos(self):
       return self.__ingresos
    @property
    def propiedad(self):
       return self.__propiedad
    @property
    def calificacion(self):
       return self.__calificacion
    
    @ingresos.setter
    def ingresos(self,nuevo):
       self.__ingresos = nuevo
    @propiedad.setter
    def propiedad(self,nuevo):
       self.__propiedad = nuevo
    @hijos.setter
    def hijos(self,nuevo):
       self.__hijos= nuevo
    def calificacion_otorgada(self):
       if 0 < self.__calificacion < 150:
          return 3500000
       elif 151 < self.__calificacion < 350:
          return 4500000
       else:
          return 6000000
    @property
    def monto (self):
       return self.calificacion_otorgada()
    def __str__(self):
       return (f"DNI: {self.dni}, Edad: {self.edad}, Hijos: {self.hijos}, Ingresos: {self.ingresos}, Propiedad: {self.propiedad}, Calificación: {self.calificacion:.2f}, Monto Asignado: {self.monto}")
class Base:
   def __init__(self):
      self.__base = []

   def agregar_datos(self,repre):
      self.__base.append(repre)

   def listar(self):
      for representante in self.__base:
         print(representante)

   def buscar_dni(self,dni):
      encontrado = False
      for repre in self.__base:
        if dni == repre.dni:
           print("== ENCONTRADO ===")
           print(repre)
           encontrado = True
      if not encontrado:
           print("NO SE ENCONTRO DNI")
   def monto_alcanzado(self,monto):
      for repre in self.__base:
         if repre.monto > monto:
            print(repre)
   def dni_ya_registrado(self, dni):
    for repre in self.__base:
        if repre.dni == dni:
            return True
    return False

   @property
   def cantidad(self):
      return len(self.__base)
   def monto_2hijos(self):
      contador = 0
      cont_repre = 0
      for repre in self.__base:
         if repre.hijos >= 2:
            contador += repre.monto
            cont_repre += 1
      return (f"MONTO TOTAL QUE SE DESEMBOLSARA: {contador} por {cont_repre} representantes con 2 o mas hijos")

base_Datos = Base()
def registrar():
    while True:
        dni = input("Ingrese DNI (8 dígitos numéricos): ")
        if dni.isdigit() and len(dni) == 8:
            if base_Datos.dni_ya_registrado(dni):
             print("DNI YA REGISTRADO")
            else:
               break
        else:
               print("ERROR: DNI inválido.")

    while True:
        try:
            edad = int(input("Ingrese su edad: "))
            if 18 < edad < 101:
                break
            else:
                print("RANGO DE EDAD NO PERMITIDA")
        except:
            print("LA EDAD DEBE SER EN NÚMEROS")

    while True:
        try:
            hijos = int(input("Ingrese la cantidad de hijos menores a 18: "))
            if 0 < hijos < 11:
                break
            else:
                print("RANGO DE HIJOS NO PERMITIDA")
        except:
            print("LOS HIJOS DEBEN SER UN NÚMERO")

    ingreso = float(input("¿Cuál es su ingreso familiar mensual?: "))
    propiedad = float(input("¿La medida de su propiedad en m²?: "))

    r1 = Representante(dni, edad, hijos, ingreso, propiedad)
    base_Datos.agregar_datos(r1)
    print("REGISTRO EXITOSO:")
    print(r1)


def menu():
   print("=== MENU PRINCIPAL ===")
   print("1. Registrar")
   print("2. Monto de Credito")
   print("3. Obtener Monto total por 2 o mas hijos")
   print("4. Buscar DNI")
   print("5. Listar")
   print("6 Salir")
   opcion= -1
   while opcion < 1 or opcion > 6:
      try:
        opcion = int(input("Ingrese su opcion: "))
        break
      except:
        print("ERROR OPCION")
   return opcion
def main():
   while True:
      opcion = menu()
      match opcion:
         case 1:
            registrar()
         case 2:
            try:
                monto = float(input("Ingrese el Monto a evaluar: "))
                base_Datos.monto_alcanzado(monto)
            except:
               print("ERROR MONTO")
         case 3:
            if base_Datos.cantidad != 0:
               print(base_Datos.monto_2hijos())
            else:
               print("AUN NO HAY REPRESENTANTES REGISTRADOS")
         case 4:
            if base_Datos.cantidad != 0:
                while True:
                    dni = input("Ingrese DNI a buscar: ")
                    if len(dni) == 8:
                     break
                    else:
                     print("DNI DE 8 DIGITOS")
                base_Datos.buscar_dni(dni)
            else:
                print("AUN NO HAY REPRESENTANTES REGISTRADOS")
         case 5:
            if base_Datos.cantidad != 0:
               print("LISTADO REPRESENTANTES")
               base_Datos.listar()
            else:
               print("NO HAY REPRESENTANTES REGISTRADOS")
         case 6:
            print("SALIENDO DEL PROGRAMA")
            break
         
base_Datos = Base()      
main() 
        