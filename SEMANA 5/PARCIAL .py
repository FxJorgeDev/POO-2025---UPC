from datetime import datetime
from random import randint

datos = {}

def regis_jugador():

    hora = (datetime.now())
    horaactual = hora.strftime('%d%m%Y%H%M%S')
    print("\nLLAVE:",horaactual)

    nombre=input("Ingrese su nombre:").strip()
    while True:
        try:
            edad=int(input("Ingrese su edad (10-85):"))
            if  0 < edad <=85:
                break
            else:
                print("ERROR, edad fuera de rango...")
        except ValueError:
            print("Por favor ingrese una valida")

    lanzamiento = int(randint(1,6))
    posicionprevia = int(1) ##FALTA IMPLEMENTAR
    posicionfinal = int(posicionprevia+lanzamiento) ##FALTA IMPLEMENTAR ##FALTA IMPLEMENTAR


    datos[horaactual]= [(nombre,edad),(lanzamiento,posicionprevia,posicionfinal),(),(),()]
    return nombre

def mostrar_reglas():
    print('\n--- ¿CÓMO JUGAR? ---')
    print("---Objetivo---")
    print("-Avanzar desde el casillero 1 hasta el 40 lanzando un dado de 6 caras.")
    print("-Puedes ganar si llegas exactamente al casillero 40.")
    print("-Si excedes el casillero 40, rebotas hacia atrás.")
    print("-Puedes abandonar en cualquier momento, o perder si caes en el pozo envenenado y sacas un número impar.\n")

    print("---Obstáculos del tablero---")
    print("- Serpiente (casillas 5-10): Retrocede 3 casilleros.")
    print("- Sacrificio (casillas 11-20): Lanza el dado nuevamente y retrocede ese número.")
    print("- Inundación (casillas 21-29): Vuelve al inicio.")
    print("- Pozo Envenenado (casillas 30-37): Lanza el dado. Si es impar, pierdes. Si es par, sigues jugando.")
    print("---Restriccion---")
    print("-Los obstáculos estarán separados al menos por 3 casilleros.\n")


def menu_principal():
        print("\n--- MENÚ PRINCIPAL ---")
        print("1. ¿Cómo jugar?")
        print("2. Ingresa datos del jugador")
        print("3. Nuevo juego")
        print("4. Iniciar el juego")
        print("5. Partidas ganadas/perdidas/abandonadas")
        print("6. Promedio de lanzamientos por partida")
        print("7. Resultados de Jugadores")
        print("8. Salir")


def resu_jugadores():

    if not datos:
        print("\nNo hay jugadores registrados todavía.")
        return

    print("\n--- RESUMEN DE JUGADORES REGISTRADOS ---")
    for clave, contenido in datos.items():
        nombre, edad = contenido[0]
        print(f"- Fecha/Hora: {clave} | Nombre: {nombre} | Edad: {edad}")
opcion = -1
while True:
    menu_principal()
    opcion = int(input("Selecciona una opción: "))
    if  0 < opcion  < 9:
        match opcion:
            case 1:
                mostrar_reglas()
            case 2:
                regis_jugador()
            case 3:
                pass
            case 7:
                resu_jugadores()
            case 8:
                print("Gracias por jugar")
    else:
        print("Opcion no valida")