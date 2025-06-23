
#EJERCICIO 1
"""""
class Loro:
    def __init__(self,nombre,edad):
        self.nombre = nombre
        self.edad = edad
    def volando(self):
        print(f"El loro {self.nombre} esta volando")
    def imprimir_datos(self):
        print(f"{self.nombre} tiene {self.edad} años")

loro1 = Loro('azul',10)
loro1.imprimir_datos()     

loro2 = Loro('Galan',15)
loro2.imprimir_datos() """


#EJERCICIO 2

""""
import math 
class Circulo:
    def __init__(self,radio):
        self.radio = radio
    def calcular_area(self):
        area = math.pi*self.radio**2
        print(area)
    def calcular_circunferencia(self):
        circunferencia = 2*math.pi*self.radio
        print(circunferencia)

#math.pi permite trabajar con el valor de PI
circulo1 = Circulo(10)
circulo1.calcular_area()
circulo1.calcular_circunferencia()
print()

circulo2 = Circulo(5)
circulo2.calcular_area()
circulo2.calcular_circunferencia()
print()

circulo3 = Circulo(25)
circulo3.calcular_area()
circulo3.calcular_circunferencia()
print()

"""

#EJERCICIO 3
""""
class CuentaBancaria:
    def __init__(self,nombre,saldo,interes):
        self.nombre = nombre
        self.saldo = saldo
        self.interes = interes
    def aplica_interes(self):
        self.saldo = self.saldo + (self.saldo*(self.interes/100)) 
        print(f"El usuario {self.nombre} tiene ahora {self.saldo} de saldo en su cuenta") 
        return self.saldo

Juan = CuentaBancaria('Juan de Arone',1000,3)
Juan.aplica_interes()
Juan1 = CuentaBancaria('Juan de Arone',Juan.aplica_interes(),2)
Juan1.aplica_interes()"""
#EJERCICIO 4
""""
class Tiket:
    def __init__(self,costo,hora):
        self.costo = costo
        self.hora = hora
    def metodo_str(self):
        print(f"Ticket ({self.costo},{self.hora})")
    def es_noche(self):
        if 18 < self.hora < 23:
            return True
        else:
            return False
    def total_descuento(self,n):
        if 5 <= n <= 9:
            self.costo = self.costo - (self.costo*0.10)
        elif n >= 10:
            self.costo = self.costo - (self.costo*0.20)
        print(f"Total a pagar {self.costo} por {n} boletos")
costo = float(input('Ingresa el costo del ticket: '))
hora = int(input('Ingrese la hora de compra: '))
ticket1 = Tiket(costo,hora)
ticket1.metodo_str()
n = int(input("cantidad de boletos: "))
print(f"Es de noche {ticket1.es_noche()}")
ticket1.total_descuento(n)  """

#EJERCICIO 5

""""
class Estudiante:
    def __init__(self,codigo,nombre,curso,notaparcial,notafinal):
        self.codigo = codigo
        self.nombre = nombre
        self.curso = curso
        self.notafinal = notafinal
        self.notaparcial = notaparcial
    def calcula_final(self):
        nota = self.notaparcial*0.4 + self.notafinal*0.6
        return nota

base_datos = []
while True:
   codigo = str(input("Codigo del alumno: "))
   if codigo.lower() == 'x':
       break
   else:
    nombre = str(input('Nombre del alumno: '))
    curso = str(input('Curso: '))
    while True:
        notaparcial = float(input('Nota del examen parcial: '))
        notafinal = float(input('Nota del examen final: '))
        if 0 < notafinal < 21 and 0 < notaparcial < 21:
            break
        else:
            print("ERROR EN LAS NOTAS....")
    alumno1 = Estudiante(codigo,nombre,curso,notaparcial,notafinal)
    nota_final = alumno1.calcula_final()
    print(f"LA NOTA DEL FINAL DEL ALUMNO: {nota_final:.2f}")
    base_datos.append({"Codigo": codigo,"Nombre": nombre,"Curso": curso, "Nota parcial": notaparcial,"Nota final":notafinal,"Promedio": nota_final })


print("------- REPORTE ------\n")
for alumno in base_datos:
    for clave,dato in alumno.items():
        print(f"{clave}: {dato}")
    print("--------------------------") """

#APUNTES DE CLASE SEMANA 6.2

# SET -> Asigna valores a valores privados
# GET -> Lee valores en atributos privados

#EJERCICIO 3 SEMANA 6.2 POR EL PROFE

""""
class CuentaBancaria:
    # CONSTRUCTOR
    def __init__(self,nombre,saldo,tasainteres):
        self.__nombre = nombre
        self.__saldo = saldo
        self.__tasainteres = tasainteres
    # METODOS DE ACCESO
    def get_nombre(self): # LEER VALORES
        return self.__nombre
    def set_nombre(self,nombre): # ESCRITURA O ASIGNAR VALORES
        self.__nombre = nombre       
    
    def get_saldo(self):
        return self.__saldo
    def set_saldo(self,saldo):
        self.__saldo = saldo

    def get_tasainteres(self):
        return self.__tasainteres
    def set_tasainteres(self,tasainteres):
        self.__tasainteres = tasainteres
    def aplica_interes(self):
        self.__saldo = self.__saldo + (self.__saldo * self.__tasainteres)/100

cuenta = CuentaBancaria("Juan de Arone",1000,3)
cuenta.aplica_interes()
print(f"Saldo es: {cuenta.get_saldo()}")
cuenta.set_tasainteres(2)
cuenta.aplica_interes()
print("Saldo es; ", cuenta.get_saldo())
   
"""



#EJERCICIO 6

class Cliente:
    def __init__(self,nombre,dni,direccion,numero,correo,preferente):
        self.__dni = dni
        self.__nombre = nombre
        self.__numero = numero
        self.__direccion = direccion
        self.__correo = correo
        self.__preferente = preferente

    def get_nombre(self):
        return self.__nombre
    def set_nombre(self,nuevo):
        self.__nombre = nuevo

    def get_dni(self):
        return self.__dni
    def set_dni(self,nuevo):
        self.__dni = nuevo

    def get_direccion(self):
        return self.__direccion
    def set_direccion(self,nuevo):
        self.__direccion = nuevo

    def get_numero(self):
        return self.__numero
    def set_numero(self,nuevo):
        self.__numero = nuevo

    def get_correo(self):
        return self.__correo       
    def set_correo(self,nuevo):
        self.__correo = nuevo

    def get_clientePreferente(self):
        return self.__preferente
    
    def set_clientePreferente(self, nuevo):
        self.__preferente = nuevo

    def __str__(self):
        return (f"Nombre: {self.__nombre} \t Dni: {self.__dni} \t Direccion: {self.__direccion} \t Numero: {self.__numero} \t Correo: {self.__correo} \t Preferente: {self.__preferente}")

class BaseClientes:
    def __init__(self):
        self.datos = []

    def registrar_Clientes(self,Cliente):
        self.datos.append(Cliente)

    def actualizar_Cliente(self,dni,cliente_nuevo):
        for i in range(len(self.datos)):
            if self.datos[i].get_dni() == dni:
                self.datos[i] = cliente_nuevo
            else:
                print("USUARIO NO REGISTRADO...")

    def eliminar_cliente(self,dni):
        for cliente in self.datos:
            if cliente.get_dni() == dni:
                self.datos.remove(cliente)
                print("== CLIENTE ELIMINADO CON EXITO ==\n")
            else:
                print("USUARIO NO ENCONTRADO...")

    def mostrar(self):
        print("DNI\tNombre\tDireccion\tTelefono\tCorreo\Preferente\n")
        for cliente in self.datos:
            print(cliente)
            
    def buscar_cliente(self,nombre):
        print("DNI\tNombre\tDireccion\tTelefono\tCorreo\Preferente\n")
        for cliente in self.datos:
            if cliente.get_nombre().lower() == nombre.lower():
                print(cliente)
            else:
                print("NO ENCONTRADO..")

def menu():
    print("\n----- MENU DE BANCO ------\n")
    print("1. Añadir Clientes")
    print("2. Buscar Clientes")
    print("3. Actualizar Clientes")
    print("4. Eliminar Clientes")
    print("5. Listar todos los Clientes")
    print("6. Terminar")
    opcion = -1
    while opcion < 1 or opcion > 6:
        try:
            opcion = int(input('Ingrese una opcion: '))
        except:
            print("ERROR, solo valores numeros...")
    return opcion
 
def llenar_datos(caso="ingresar",dni="123"):
    if caso == "ingresar":
        dni=""
        while len(dni) != 8 or not dni.isdigit():
            dni = input("Ingrese el DNI: ")
            if len(dni) != 8:
                print("ERROR... El DNI tiene 8 digitos..")
    nombre = input("Ingrese el nombre: ")
    direccion = input("Ingrese la dirrecion: ")
    numero = input('Ingrese el numero: ')
    correo = nombre + "@empsac.com"
    preferente = bool(int(input("Ingrese si es cliente preferente (1:si 2:no): ")))
    cliente = Cliente(nombre,dni,direccion,numero,correo,preferente)
    print(" REGISTRO EXITOSO......")
    return cliente

def main():
    DatosClientes = BaseClientes()
    opcion = -1
    while opcion != 6:
        opcion = menu()             
        match opcion:
            case 1:
                cliente = llenar_datos()
                DatosClientes.registrar_Clientes(cliente)
            case 2:
                nombre = input("Ingrese el Nombre a buscar: ")
                DatosClientes.buscar_cliente(nombre)
            case 3:
                dni = input("Ingrese el Dni a buscar: ")
                cliente = llenar_datos("actualizar",dni)
                DatosClientes.actualizar_Cliente(dni,cliente)
            case 4:
                dni = input("Ingrese el DNI: ")
                DatosClientes.eliminar_cliente(dni)
            case 5:
                DatosClientes.mostrar()
            case 6:
                print("SALIENDO DEL PROGRAMA......")
                break


main()