""""
class Pastel:
    cont_calorias = 0
    def __init__(self,nombre,cantidad,precio):
        self.__nombre = nombre
        self.__cantidad = cantidad
        self.__precio = precio
        self.__lista_pastel = []
        self.__lista_ingredientes = []
    @property
    def nombre (self):
        return self.__nombre
    @property
    def cantidad(self):
        return self.__cantidad
    @property
    def precio(self):
        return self.__precio
    
    @cantidad.setter
    def cantidad(self,nuevo):
        self.__cantidad = nuevo
    @precio.setter
    def precio(self,nuevo):
        self.__precio = nuevo
    
    def agregar_pastel(self,pastel):
        if isinstance(pastel,Pastel):
            self.__lista_pastel.append(pastel)
        else:
            print("SE ESPERABA UN DATO CLASE PASTEL")
    def agregar_ingredientes(self,ingredientes):
        self.__lista_ingredientes.append(ingredientes)
    def cont_ingredientes(self):
        return len(self.__lista_ingredientes)
    
    def contar_calorias(self):
        for ingredientes in self.__lista_ingredientes:
            cont = ingredientes.cantidad * ingredientes.calorias
            self.cont_calorias += cont
        return self.cont_calorias
    def mostrar(self):
        for ingrediente in self.__lista_ingredientes:
            print(ingrediente)
class Ingredientes:
    cont_ingredientes = 0
    def __init__(self,nombre,unidad,cantidad,calorias):
        self.__nombre=nombre
        self.__unidad= unidad
        self.__cantidad= cantidad
        self.__calorias= calorias
    @property
    def nombre (self):
        return self.__nombre
    @property
    def unidad (self):
        return self.__unidad
    @property
    def cantidad (self):
        return self.__cantidad
    @property
    def calorias(self):
        return self.__calorias
    @property
    def cantidad_ingredientes(self):
        return self.cont_ingredientes
    def __str__(self):
        return f"Ingrediente: {self.nombre}, Cantidad: {self.cantidad}, Unidad de Medida: {self.unidad}, Calorias: {self.calorias}"

    
harina = Ingredientes("Harina",'gramos',1000,3.50)
azucar = Ingredientes("Azucar",'gramos',500,4)

pastel1 = Pastel("Chocolate",5,2000)
pastel1.agregar_ingredientes(harina)
pastel1.agregar_ingredientes(azucar)

print(pastel1.mostrar())
print(pastel1.cont_ingredientes())
print(pastel1.contar_calorias())
"""
#EJERCICIO 2

class Usuario:
    def __init__(self,nombre,dni):
        self.__nombre = nombre
        self.__dni = dni
    @property
    def nombre(self):
        return self.__nombre
    @property
    def dni (self):
        return self.__dni
    def __str__(self):
        return f"Nombre: {self.nombre}, DNI: {self.dni}"

class Pelicula:
    def __init__(self,nombre,director,duracion):
        self.__nombre = nombre
        self.__director = director
        self.__duracion = duracion
    @property
    def nombre (self):
        return self.__nombre
    @property
    def director (self):
        return self.__director
    @property
    def duracion (self):
        return self.__duracion
    def __str__(self):
        return f"Nombre Pelicula; {self.nombre}, Director: {self.director}, Duracion: {self.duracion}"

class Prestamo:
    
    def __init__(self,pelicula,usuario,fecha_p,fecha_d):
        self.__fecha_p = fecha_p
        self.__fecha_d = fecha_d
        if isinstance(usuario,Usuario) and isinstance(pelicula,Pelicula):
            self.__usuario = usuario
            self.__pelicula = pelicula
            self.__prestamos = {}
        else:
            print("SE ESPERABA UN DATO CLASE USUARIO y UN DATO TIPO PELICULA")
    def get_Titulo(self):
        return self.__pelicula.nombre
    def get_NombreUsuario(self):
        return self.__usuario.nombre
    def get_DNI(self):
        return self.__usuario.dni
    def get_fecha_prestamo(self):
        return self.__fecha_p
    def get_fecha_devolucion(self):
        return self.__fecha_d
    def agregar_prestamos(self,usuario,pelicula):
        self.__prestamos[usuario.dni] = pelicula
    def mostrar_prestamos(self):
        if len(self.__prestamos) == 0:
            print("no hay prestamos")
        else:
            for usuario,pelicula in self.__prestamos.items():
                print(f"Usuario: {self.__usuario} Pelicula: {self.__pelicula}")

pelicula1 = Pelicula("La vida de Brian","Terry Jones","94 minutos")
usuario1 = Usuario("Antonio Rojas",55555555)

prestamo1 = Prestamo(pelicula1,usuario1,"20240606","20240610")
prestamo1.agregar_prestamos(usuario1,pelicula1)
prestamo1.mostrar_prestamos()
        