
dict = {

    1: {'Pedro Gallese','Arquero'},
    22: ('Alexander Callens','Defensa'),
    4:('Anderson Santamaria','Defensa'),
    6: ('Marcos Lopez','Lateral'),
    17:('Luis Advincula','Lateral'),
    10: ('Cristian Cueva','Lateral'),
    13: ('Renato Tapia','Mediocampista'),
    23: {'Pedro Aquino','Medio Campista'},
    9: ('Gianluca Lapadula','Delantero'),
    20: ('Edison Flores','Extremo'),
    18: ('Andre Carillo','Extremo')
}

"""print(f"Numero \n {dict.keys()} \t Nombre \n {dict.values()}, ")"""
dict.pop(4)
dict[5] = ('Carlos Zambrano','Defensa')
dict.pop(10)
dict[8] = 'Sergio Peña','Medio campista'
dict.pop(9)
dict[30] = 'Raul Ruidiaz','Delantero'
dict.pop(18)
dict[26] = 'Yordi reina','Delantero'
print(dict)
dict[23]= {'Pedro Aquino','Delantero'}
print(dict)
