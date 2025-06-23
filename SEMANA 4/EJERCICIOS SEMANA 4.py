#EJERCICIO 1 SEMANA 04
""""
jugadores = {
             "Numero ": [1,22,4,6,17,10,13,23,9,20,18],
             "Nombre ": ["Pedro Gallese","Alexander Callens","Anderson Santamaría","Marcos Lopez",
                         "Luis Advincula","Christin Cueva","Renato Tapia","Pedro Aquino",
                         "Gianluca Lapadula","Edison Flores","Andre Carrillo"],}

print(f"Los jugaores titulares fueron {jugadores['Numero ']}{jugadores["Nombre "]} los 11 de GARECA")

jugadores["Numero "][2] = 5
jugadores["Nombre "][2] = "Carlos Zambrano"

print(end=' ')
print(f"Primer jugador sustituido, el equipo queda asi {jugadores['Nombre ']}")

jugadores["Numero "][5] = 8
jugadores["Nombre "][5]= "Sergio Peña"
jugadores["Numero "][7] = 24
jugadores["Nombre "][7]= "Alex Valera"
jugadores["Numero "][8] = 30
jugadores["Nombre "][8]= "Raul Ruidiaz"
jugadores["Numero "][9] = 16
jugadores["Nombre "][9]= "Christofer Gonzales"
jugadores["Numero "][10] = 26
jugadores["Nombre "][10]= "Yordy Reina"

print("EL EQUIPO CON LOS CAMBIOS REALIZADOS: ", sep=' ')
print(f"{jugadores['Numero ']}")
print(f"LOS 11 EN LA CANCHA {jugadores["Nombre "]}",sep=' ')

lista = list(jugadores["Numero "])
lista.sort()
print('Ordenado de forma Ascendente: ',lista,sep=' ',)

listanombres = list(jugadores["Nombre "])
listanombres.sort(reverse=False)
print("Nombres ordanados en orden Alfabetico",listanombres,sep=' \n')"""

#EJERCICIO 2 SEMANA 04

def convertir_pies(valor, opcion):
    conversiones = {
        1: ("Pulgadas", valor * 12),
        2: ("Yardas", valor * 0.3333),
        3: ("Millas", valor * 0.0002),
        4: ("Milímetros", valor * 304.8),
        5: ("Centímetros", valor * 30.48),
        6: ("Metros", valor * 0.3048),
    }
    return conversiones.get(opcion, ("", 0))


def mostrar_menu():
    print("\nMenú de Conversión:")
    print("[1] Pulgadas")
    print("[2] Yardas")
    print("[3] Millas")
    print("[4] Milímetros")
    print("[5] Centímetros")
    print("[6] Metros")
    print("[7] Resumen")
    print("[8] Salir")


def mostrar_resumen(historial):
    print("\nConversión de medidas de pies a")
    print(f"{'Nro':<5} {'Pies':<10} {'Convertir a':<15} {'Convertido'}")
    for i, (pies, unidad, resultado) in enumerate(historial, start=1):
        print(f"{i:<5} {pies:<10} {unidad:<15} {round(resultado, 2)}")


def main():
    historial = []

    while True:
        mostrar_menu()
        try:
            opcion = int(input("Seleccione una opción: "))
        except ValueError:
            print("Por favor, ingrese un número válido.")
            continue

        if opcion == 8:
            print("¡Hasta luego!")
            break
        elif opcion == 7:
            mostrar_resumen(historial)
        elif 1 <= opcion <= 6:
            try:
                pies = float(input("Ingrese la cantidad en pies: "))
                unidad, convertido = convertir_pies(pies, opcion)
                historial.append((pies, unidad, convertido))
                print(f"{pies} pies equivalen a {round(convertido, 2)} {unidad}")
            except ValueError:
                print("Entrada inválida. Ingrese un número.")
        else:
            print("Opción no válida. Intente de nuevo.")


if __name__ == "__main__":
    main()
