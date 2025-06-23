class Persona:
    __registro = 0
    __conta_anios = 0
    def __init__(self,nombre:str,edad:int):
        self.nombre = nombre
        self.edad = edad
        Persona.__registro += 1
        Persona.__conta_anios += edad
    @classmethod
    def get_registros(cls):
        return cls.__registro
    @classmethod
    def get_anios(cls):
        return cls.__conta_anios
    @classmethod
    def set_registro(cls,registro):
        cls.__registro = registro
        
Persona1 = Persona('nils',20)
print(f"N° Regstros: {Persona.get_registros()}")
print(f"Contador Anios: {Persona.get_anios()}")

Persona.set_registro(1)

Persona2 = Persona("bolanios",15)
print(f"N° Regstros: {Persona.get_registros()}")
print(f"Contador Anios: {Persona.get_anios()}")

