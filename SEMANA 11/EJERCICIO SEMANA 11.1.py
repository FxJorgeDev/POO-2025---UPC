
#EJERCICIO 1 
"""
class Proveedor:
    def __init__(self, ruc, razon, categoria, direccion, telefono):
        self.__ruc = ruc
        self.__razon = razon
        self.__categoria = categoria
        self.__direccion = direccion
        self.__telefono = telefono

    @property
    def ruc(self): return self.__ruc

    @property
    def razon(self): return self.__razon

    @property
    def categoria(self): return self.__categoria

    @property
    def direccion(self): return self.__direccion

    @property
    def telefono(self): return self.__telefono

    def __str__(self):
        return f"RUC: {self.ruc}, Razón: {self.razon}, Categoría: {self.categoria}, Dirección: {self.direccion}, Teléfono: {self.telefono}"


class Producto:
    def __init__(self, id, nombre, tipo, cantidad, categoria, anio, precio, proveedor):
        self.__id = id
        self.__nombre = nombre
        self.__tipo = tipo
        self.__cantidad = cantidad
        self.__categoria = categoria
        self.__anio = anio
        self.__precio = precio
        self.__proveedor = proveedor if isinstance(proveedor, Proveedor) else None

    @property
    def id(self): return self.__id

    @id.setter
    def id(self, nuevo): self.__id = nuevo

    @property
    def nombre(self): return self.__nombre

    @property
    def tipo(self): return self.__tipo

    @property
    def cantidad(self): return self.__cantidad

    @cantidad.setter
    def cantidad(self, nueva): self.__cantidad = nueva

    @property
    def categoria(self): return self.__categoria

    @property
    def anio(self): return self.__anio

    @property
    def precio(self): return self.__precio

    @precio.setter
    def precio(self, nuevo): self.__precio = nuevo

    @property
    def proveedor(self): return self.__proveedor

    def vencido(self):
        return self.anio < 2025

    def __str__(self):
        return f"ID: {self.id}, Nombre: {self.nombre}, Tipo: {self.tipo}, Cantidad: {self.cantidad}, Categoría: {self.categoria}, Año: {self.anio}, Precio: {self.precio}, Proveedor: [{self.proveedor}]"
proveedores = []
productos = []

def registrar_proveedor():
    ruc = input("RUC: ")
    razon = input("Razon social: ")
    categoria = input("Categoria: ")
    direccion = input("Direccion: ")
    telefono = input("Telefono: ")
    proveedores.append(Proveedor(ruc, razon, categoria, direccion, telefono))

def registrar_producto():
    id = input("ID: ")
    nombre = input("Nombre: ")
    tipo = input("Tipo (polvo/líquido): ")
    cantidad = int(input("Cantidad: "))
    categoria = input("Categoría (A/B/C): ")
    anio = int(input("Año: "))
    precio = float(input("Precio: "))
    ruc_proveedor = input("RUC del proveedor: ")

    proveedor = next((p for p in proveedores if p.ruc == ruc_proveedor), None)
    if proveedor:
        productos.append(Producto(id, nombre, tipo, cantidad, categoria, anio, precio, proveedor))
    else:
        print("Proveedor no encontrado")

def modificar_producto():
    nombre = input("Nombre del producto a modificar: ")
    for prod in productos:
        if prod.nombre == nombre:
            prod.cantidad = int(input("Nueva cantidad: "))
            prod.id = input("Nuevo ID: ")
            prod.precio = float(input("Nuevo precio: "))
            print("Producto actualizado")
            return
    print("Producto no encontrado")

def mostrar_productos():
    for prod in productos:
        print(prod)

def mostrar_por_categoria():
    cat = input("Categoría: ")
    for prod in productos:
        if prod.categoria == cat:
            print(prod)

def eliminar_herbalife():
    global productos
    productos = [p for p in productos if p.proveedor.razon.lower() != "herbalife"]
    print("Productos Herbalife eliminados")

def eliminar_vencidos():
    global productos
    productos = [p for p in productos if not p.vencido()]
    print("Productos vencidos eliminados")

def mostrar_por_categoria_y_proveedor():
    for p in productos:
        if p.categoria == "A" and p.proveedor.razon.lower() == "natura":
            print(p)

def mostrar_productos_por_rango():
    n = int(input("Cuantos productos desea mostrar?: "))
    for i in range(min(n, len(productos))):
        print(productos[i])

def menu():
    opciones = {
        "1": registrar_producto,
        "2": registrar_proveedor,
        "3": modificar_producto,
        "4": eliminar_herbalife,
        "5": mostrar_productos,
        "6": mostrar_por_categoria_y_proveedor,
        "7": eliminar_vencidos,
        "8": mostrar_productos_por_rango
    }

    while True:
        print("\n===== MENU =====")
        print("1. Insertar Producto")
        print("2. Insertar Proveedor")
        print("3. Modificar Productos")
        print("4. Eliminar Productos Herbalife")
        print("5. Mostrar Productos")
        print("6. Mostrar productos cat. A y proveedor Natura")
        print("7. Eliminar Productos Vencidos")
        print("8. Mostrar N productos")
        print("9. Salir")
        opcion = input("Opcion: ")
        if opcion == "9": break
        elif opcion in opciones:
            opciones[opcion]()
        else:
            print("Opción inválida")
menu()"""

#EJERCICIO 2

class Equilatero:
    def __init__(self,lado:int,caracter:str):
        self.__lado = lado
        self.__caracter = caracter
    @property
    def lado (self): return self.__lado
    @property 
    def caracter (self):return self.__caracter
    def dibujar (self):
        for i in range (self.lado):
            espacios = " " * (self.lado - i - 1)
            if i == 0:
                print(espacios + self.caracter)
            elif i == self.lado -1:
                print(self.caracter * (2 * i  + 1))
            else:
                print(espacios + self.caracter + " " * (2*i-1) + self.caracter)
class Rectangulo:
    def __init__(self,lado1:int,lado2:int,caracter:str):
        self.__lado1 = lado1
        self.__lado2 = lado2
        self.__caracter = caracter
    @property
    def lado1 (self): return self.__lado1
    @property
    def lado2 (self): return self.__lado2
    @property 
    def caracter (self):return self.__caracter
    def dibujar(self):
        for fila in range (self.lado1):
            for col in range(self.lado2):
                if fila == 0 and col == 0:
                    print(self.caracter, end = "")
                elif col == 0 and fila < self.__lado1:
                    print(self.caracter, end = "")
                elif fila == self.lado1 - 1:
                    print(self.caracter,end="")
                elif col == round ((fila / (self.lado1 -1)) * (self.lado2 -1)): 
                    print(self.caracter,end="")
                else:
                    print(" ",end="")
            print()
def menu():
    print("=== MENU PRINCIPAL ===")
    print("1. Triangulo Equilatero")
    print("2. Triangulo Rectangulo")
    print("3. Salir")
    opcion = -1
    while opcion < 1 or opcion > 3:
        opcion = int(input("Ingrese Opcion: "))
    return opcion

def main():
    opcion = -1
    while True:
        opcion = menu()
        match opcion:
            case 1:
                while True:
                    lado = int(input("Ingrese el lado del Triangulo (Valor entero entre 5 a 100): "))
                    if  5 < lado < 100:
                        break
                    else:
                        print("Lado fuera de Rango")
                caracter = str(input("Ingrese el caracter a dibujar: "))
                obj1 = Equilatero(lado,caracter)
                obj1.dibujar()
            case 2:
                while True:
                    lado1 = int(input("Ingrese el lado 1 del triangulo (Valor entero entre 5 a 100): "))
                    lado2 = int(input("Ingrese el lado 2 del triangulo (Valor entero entre 5 a 100): "))
                    if 5<lado1 < 100 and 5 < lado2 < 100:
                        break
                    else:
                        print("ERROR Lados fuera de rango")
                caracter = str(input("Ingrese el caracter a dibujar: "))
                obj1 = Rectangulo(lado1,lado2,caracter)
                obj1.dibujar()
            case 3:
                break
    print("Saliendo del programa...")
main()