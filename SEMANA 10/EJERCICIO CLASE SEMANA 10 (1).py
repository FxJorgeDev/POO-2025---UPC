class Administrador:
    def __init__(self,id_a:str,nombre:str):
        self.__id = id_a
        self.__nombre = nombre
    @property
    def id_admi (self):
        return self.__id
    @property
    def nombre(self):
        return self.__nombre
    def __str__(self):
        return f"IDAdministrador: {self.id_admi}, Nombre: {self.nombre}"

class Edificio:
    def __init__(self,id_e:str,direccion:str,administrador,junta,departamentos):
        self.__id_e = id_e
        self.__direccion = direccion
        self.__administrador = administrador
        self.__junta = junta
        self.__departamentos = []
        if isinstance(departamentos,list):
            for departamento in departamentos:
                self.agregar_departamento(departamento)
        else:
            print("se esperaba un objeto de tipo lista")
    @property
    def id_e (self):
        return self.__id_e
    @property
    def direccion (self):
        return self.__direccion
        
    def agregar_departamento(self,departamento):
        self.__departamentos.append(departamento)
        
    def listar_departamento(self):
        if len(self.__departamentos) == 0:
            print("NO HAY DEPARTAMENTOS REGISTRADOS")
        else:
            for departamento in self.__departamentos:
                print(f"DEPARTAMENTO: {departamento}")
    def listar_edificio(self):
        print("idEdificio: ", self.id_e, "Direccion: ", self.direccion)
        print(self.__administrador)
        self.__junta.listar_junta()
        self.listar_departamento()
        
class Departamento:
    def __init__(self,id_d:str,numero:int):
        self.__id_d = id_d
        self.__numero = numero
    @property
    def id_d(self):
        return self.__id_d
    @property
    def numero (self):
        return self.__numero
    def __str__(self):
        return f"IdDepartamento: {self.id_d}, Numero Habitacion: {self.numero}"
    
class JuantaPropietario:
    def __init__(self,id_j:str,fecha:str,propietarios):
        self.__id_j = id_j
        self.__fecha = fecha
        self.__propietarios = []
        if isinstance(propietarios,list):
            for propietario in propietarios:
                self.agregar_propietario(propietario)
        else:
            print("SE ESPERABA UN OBJETO DE TIPO LISTA")
                
    @property
    def id_j (self):
        return self.__id_j
    @property
    def fecha(self):
        return self.__fecha
    
    def agregar_propietario(self,propietario):
        self.__propietarios.append(propietario)
    def listar_propietarios(self):
        if len(self.__propietarios) == 0:
            print("NO HAY PROPIETARIOS REGISTRADOS")
        else:
            for propietario in self.__propietarios:
                print(f"PROPIETARIOS: {propietario}")
    def listar_junta(self):
        print("id Junta Propietario: ", self.id_j, "Fecha Creacion:", self.fecha)
        self.listar_propietarios()

class Propietario:
    def __init__(self,id_p:str,nombre:str):
        self.__id_p = id_p
        self.__nombre = nombre
    @property
    def id_p(self):
        return self.__id_p
    @property
    def nombre(self):
        return self.__nombre
    def __str__(self):
        return f"Id Propietario: {self.id_p}. Nombre: {self.nombre}"

        
departamentos = [Departamento("132",4),Departamento("140",5),Departamento("500",8),Departamento("456",10)]
propietarios = [Propietario("25","Nils H.A"),Propietario("150","Valentin"),Propietario("322","Matias Ramos"),Propietario("789","Bonny15")]   
objadmi= Administrador("1232","Elias Bolaños")
objjunta = JuantaPropietario("100","01/06/2025",propietarios)
objedificio = Edificio("1000","Chorillos - Mega Plaza",objadmi,objjunta,departamentos)
objedificio.listar_edificio()  
        