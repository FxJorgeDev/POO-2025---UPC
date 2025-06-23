
#EJERCICIO 4 
class Representante:
    def __init__(self, dni, edad, nhijos, ingresos, propiedad):
        self.__dni = dni
        self.__edad = edad
        self.__nhijos = nhijos
        self.__ingresos = ingresos
        self.__propiedad = propiedad

    # Métodos de acceso GET
    def get_dni(self):
        return self.__dni
    def get_edad(self):
        return self.__edad
    def get_nhijos(self):
        return self.__nhijos
    def get_ingresos(self):
        return self.__ingresos
    def get_propiedad(self):
        return self.__propiedad

    # Métodos de acceso SET
    def set_dni(self, nuevo):
        self.__dni = nuevo
    def set_edad(self, nuevo):
        self.__edad = nuevo
    def set_nhijos(self, nuevo):
        self.__nhijos = nuevo
    def set_ingresos(self, nuevo):
        self.__ingresos = nuevo
    def set_propiedad(self, nuevo):
        self.__propiedad = nuevo

    def calificacion(self):
         return self.get_edad() + self.get_nhijos() + (self.get_ingresos() / self.get_propiedad())


    def calificacion_nivel(self):
        c = self.calificacion()
        if 0 < c < 151:
            return 35000.00
        elif 150 < c < 351:
            return 45000.00
        else:
            return 60000.00

class Base:
    def __init__(self):
        self.__base = []

    def agregar_datos(self, representante):
        self.__base.append(representante)

    def listado_base(self):
        print("DNI:\tN.Hijos:\tCalificación:")
        for i in self.__base:
            print(f"{i.get_dni()}\t{i.get_nhijos()}\t\t{i.calificacion():.2f}")

    def listado_credito(self, monto_credito):
        print("DNI\tCalificación")
        for i in self.__base:
            if i.calificacion_nivel() >= monto_credito:
                print(f"{i.get_dni()}\t{i.calificacion():.2f}")

    def listado_hijos(self, hijos):
        print("DNI\tN. Hijos")
        for i in self.__base:
            if i.get_nhijos() >= hijos:
                print(f"{i.get_dni()}\t{i.get_nhijos()}")

    def buscar_dni(self, dni_buscar):
        encontrado = False
        for i in self.__base:
            if i.get_dni() == dni_buscar:
                print("DNI\tN. Hijos")
                print(f"{i.get_dni()}\t{i.get_nhijos()}")
                encontrado = True
        if not encontrado:
            print("NO ENCONTRADO")

def menu():
    print("\n==== MENU PRINCIPAL =====")
    print("1. Ingresar Datos")
    print("2. Listado de Representantes")
    print("3. Representantes que alcanzan un crédito")
    print("4. Mostrar por N° de hijos")
    print("5. Buscar por DNI")
    print("6. Salir\n")

Base_datos = Base()

while True:
    menu()
    try:
        opcion = int(input("Ingrese su Opción: "))
    except ValueError:
        print("Debe ingresar un número válido.")
        continue
    if opcion == 6:
        print("Saliendo del Programa...")
        break
    elif opcion == 1:
        print("\n=== REGISTRO DE DATOS ===")
        dni = int(input("Ingrese el DNI: "))
        edad = int(input("Ingrese Edad: "))
        nhijos = int(input("Ingrese Número de hijos menores de edad: "))
        ingresos = float(input("Ingrese el monto de sus ingresos: "))
        propiedad = int(input("Ingrese los m2 de la propiedad: "))
        objeto = Representante(dni, edad, nhijos, ingresos, propiedad)
        Base_datos.agregar_datos(objeto)
    elif opcion == 2:
        Base_datos.listado_base()
    elif opcion == 3:
        monto = float(input("Ingrese el monto mínimo del crédito: "))
        Base_datos.listado_credito(monto)
    elif opcion == 4:
        hijos = int(input("Ingrese la cantidad mínima de hijos: "))
        Base_datos.listado_hijos(hijos)
    elif opcion == 5:
        dni_buscar = int(input("Ingrese el DNI a buscar: "))
        Base_datos.buscar_dni(dni_buscar)
    else:
        print("Opción no válida. Intente de nuevo.")






