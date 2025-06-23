from datetime import datetime
import time
from random import randint
import os
import shutil
import json


class Jugador:
    def __init__(self, nombre, edad, emoji):
        self.__nombre = nombre
        self.__edad = edad
        self.__emoji = emoji
        self.__posicion = 1
        self.__estado = "en juego"
        self.__lanzamientos = 0

    @property
    def nombre(self):
        return self.__nombre

    @property
    def edad(self):
        return self.__edad

    @property
    def emoji(self):
        return self.__emoji

    @property
    def posicion(self):
        return self.__posicion

    @posicion.setter
    def posicion(self, pos):
        self.__posicion = pos

    def avanzar_lanzamiento(self):
        self.__lanzamientos += 1

    @property
    def lanzamientos(self):
        return self.__lanzamientos

    @property
    def estado(self):
        return self.__estado

    @estado.setter
    def estado(self, estado):
        self.__estado = estado


class Trampas:
    def __init__(self):
        self.__serpiente = randint(5, 11)
        self.__sacrificio = randint(11, 21)
        self.__inundacion = randint(21, 30)
        self.__pozo = randint(30, 38)

    def mostrar_obstaculos(self):
        print_centrado(f"Serpiente 🐍 : Casillero {self.__serpiente}")
        print_centrado(f"Sacrificio 🩨 : Casillero {self.__sacrificio}")
        print_centrado(f"Inundacion 🌊 : Casillero {self.__inundacion}")
        print_centrado(f"Pozo 🕳   : Casillero {self.__pozo}")

    def verificar_obstaculo(self, posicion):
        if posicion == self.__serpiente:
            print_centrado("Te atrapo la serpiente 🐍, retrocedes 3 casillas")
            time.sleep(1)
            return posicion - 3
        elif posicion == self.__sacrificio:
            dado = randint(1, 6)
            print_centrado(f"Sacrificio 🩨: retrocedes {dado} casillas")
            time.sleep(1)
            return posicion - dado
        elif posicion == self.__inundacion:
            print_centrado("Una inundación 🌊 te lleva al inicio")
            time.sleep(1)
            return 1
        elif posicion == self.__pozo:
            dado = randint(1, 6)
            print_centrado("Caíste en un pozo 🕳")
            time.sleep(1)
            if dado % 2 == 1:
                print_centrado("Perdiste el juego")
                time.sleep(1)
                return -1
            else:
                print_centrado("Te salvaste esta vez...")
                time.sleep(1)
        return posicion

    def obtener_obstaculos(self):
        return {
            self.__serpiente: "🐍",
            self.__sacrificio: "🩨",
            self.__inundacion: "🌊",
            self.__pozo: "🕳"
        }


class Tablero:
    def __init__(self):
        self.__trampas = Trampas()
        self.__trampas.mostrar_obstaculos()

    def mostrar_obstaculos(self):
        self.__trampas.mostrar_obstaculos()

    def verificar_obstaculo(self, posicion):
        return self.__trampas.verificar_obstaculo(posicion)

    def obtener_obstaculos(self):
        return self.__trampas.obtener_obstaculos()


class Juego:
    def __init__(self):
        self.__jugadores = []
        self.__tablero = None
        self.__emojis_usados = set()
        self.__partidas = self.cargar_historial()

    def cargar_historial(self):
        if os.path.exists("historial.json"):
            try:
                with open("historial.json", "r") as archivo:
                    return json.load(archivo)
                
            except (json.JSONDecodeError, IOError) as e:
                print_centrado(f"⚠️ Error al cargar historial: {e}")
                return {}
        return {}
            
    def guardar_historial(self):
        with open("historial.json", "w") as archivo:
            json.dump(self.__partidas, archivo)

    def mostrar_historial(self):
        if not self.__partidas:
            print_centrado("📬 No hay partidas registradas.")
            return
        print_centrado("📋 Historial de partidas:")
        for clave, datos in self.__partidas.items():
                fecha = datetime.strptime(clave, '%d%m%Y%H%M%S').strftime('%d/%m/%Y %H:%M:%S')
                print_centrado(f"{fecha} - {datos['nombre']} - {datos['resultado']} - 🎲 {datos['lanzamientos']} lanzamientos")

    def agregar_jugador(self, jugador):
        if jugador.emoji in self.__emojis_usados:
            print_centrado("Ese emoji ya ha sido usado. Elige otro.")
            return False
        self.__jugadores.append(jugador)
        self.__emojis_usados.add(jugador.emoji)
        return True

    def nuevo_tablero(self):
        self.__tablero = Tablero()

    def jugar(self):
        if not self.__tablero or not self.__jugadores:
            print_centrado("Faltan jugadores o tablero no generado")
            return

        ganador_encontrado = False
        while any(j.estado == "en juego" for j in self.__jugadores) and not ganador_encontrado:
            for jugador in self.__jugadores:
                if jugador.estado != "en juego":
                    continue
                print_centrado(f"\nTurno de: {jugador.nombre} {jugador.emoji}")
                self.imprimir_tablero(jugador)
                entrada = input(f"{jugador.nombre}, presiona Enter para lanzar o escribe 'salir': ")
                if entrada.lower() == "salir":
                    jugador.estado = "abandonada"
                    continue

                dado = randint(1, 6)
                jugador.avanzar_lanzamiento()
                print_centrado(f"🎲 Dado: {dado}")
                nueva_pos = jugador.posicion + dado

                if nueva_pos > 40:
                    exceso = nueva_pos - 40
                    nueva_pos = 40 - exceso
                    print_centrado(f"Te pasaste, retrocedes a {nueva_pos}")

                if nueva_pos == 40:
                    print_centrado("¡Felicidades, ganaste!")
                    jugador.estado = "ganada"
                    jugador.posicion = 40
                    ganador_encontrado = True
                    break

                nueva_pos = self.__tablero.verificar_obstaculo(nueva_pos)
                if nueva_pos == -1:
                    jugador.estado = "perdida"
                    continue

                jugador.posicion = nueva_pos

        for jugador in self.__jugadores:
            estado = jugador.estado
            llave = datetime.now().strftime('%d%m%Y%H%M%S')
            self.__partidas[llave] = {
                "nombre": jugador.nombre,
                "resultado": estado,
                "lanzamientos": jugador.lanzamientos
            }
            print_centrado(f"Resultado de {jugador.nombre}: {estado}")

        self.guardar_historial()

    def imprimir_tablero(self, jugador_actual):
        columnas = 10
        contador = 1
        posiciones = {j.posicion: j.emoji for j in self.__jugadores if j.estado == "en juego"}
        obstaculos = self.__tablero.obtener_obstaculos()

        for fila1 in range(4):
            print_centrado("+----" * columnas + "+")
            fila1 = ""
            for col in range(columnas):
                celda = f"{contador:2}"
                if contador in posiciones:
                    celda = posiciones[contador]
                elif contador in obstaculos:
                    celda = obstaculos[contador]
                fila1 += f"| {celda:^2} "
                contador += 1
            fila1 += "|"
            print_centrado(fila1)
        print_centrado("+----" * columnas + "+")



def print_centrado(texto):
    ancho = shutil.get_terminal_size().columns
    for linea in texto.split('\n'):
        print(linea.center(ancho))


def elegir_emoji(juego):
    opciones = ["👑", "🐸", "🐱", "🐶", "🦊", "🐵", "🐼"]
    disponibles = [e for e in opciones if e not in juego._Juego__emojis_usados]

    while True:
        print("Elige tu emoji:")
        for idx, emoji in enumerate(disponibles, 1):
            print(f"{idx}. {emoji}")
        try:
            eleccion = int(input("Selecciona un número: "))
            if 1 <= eleccion <= len(disponibles):
                return disponibles[eleccion - 1]
        except ValueError:
            pass
        print("Opción inválida, intenta otra vez.")


def menu_principal():
    print_centrado("\n--- MENÚ PRINCIPAL ---")
    print_centrado("1. ¿Cómo jugar?")
    print_centrado("2. Ingresa datos del jugador")
    print_centrado("3. Nuevo juego")
    print_centrado("4. Iniciar el juego")
    print_centrado("5. Partidas ganadas/perdidas/abandonadas")
    print_centrado("6. Promedio de lanzamientos por partida")
    print_centrado("7. Jugadores registrados")
    print_centrado("8. Ver ultima partida registrada")
    print_centrado("9. Salir")

if __name__ == "__main__":
    
    while True:
        menu_principal()
        opcion = input("Selecciona una opción (1-9): ")
        if opcion == "1":
            print_centrado("Cada jugador lanza un dado para avanzar en un tablero de 40 casillas. ¡Evita los obstáculos y llega a la meta!")
        elif opcion == "2":
            if 'juego' not in locals():
                juego = Juego()
            nombre = input("Nombre del jugador: ")
            while True:
                try:
                    edad = int(input("Edad del jugador: "))
                    if 10 <= edad <= 85:
                        break
                    else:
                        print("Edad fuera de rango")
                except ValueError:
                    print("Edad inválida")
            emoji = elegir_emoji(juego)
            jugador = Jugador(nombre, edad, emoji)
            juego.agregar_jugador(jugador)
            print_centrado(f"Jugador {jugador.nombre} {jugador.emoji} Registrado")

        elif opcion == "3":
            if 'juego' not in locals():
                print_centrado("Primero ingresa jugadores.")
            else:
                juego.nuevo_tablero()
                print_centrado("Nuevo juego creado")

        elif opcion == "4":
            if 'juego' not in locals():
                print_centrado("Primero ingresa jugadores.")
            else:
                juego.jugar()

        elif opcion == "5":
            if "juego" in locals():
                juego.mostrar_historial()
            else:
                juego = Juego()
                juego.mostrar_historial()
        elif opcion == "6":
            if 'juego' in locals() and juego._Juego__partidas:
                total = sum(p['lanzamientos'] for p in juego._Juego__partidas.values())
                promedio = total / len(juego._Juego__partidas)
                print_centrado(f"Promedio de lanzamientos por partida: 🎲 {promedio:.2f}")
            else:
                print_centrado("📬 No hay partidas para calcular promedio.")

        elif opcion == "7":
            if 'juego' in locals() and juego._Juego__jugadores:
                print_centrado("👥 Jugadores registrados:")
                for j in juego._Juego__jugadores:
                    print_centrado(f"{j.nombre} ({j.edad} años) {j.emoji}")
            else:
                print_centrado("📬 No hay jugadores registrados.")

        elif opcion == "8":
            if 'juego' in locals() and juego._Juego__partidas:
                ultima = max(juego._Juego__partidas)
                datos = juego._Juego__partidas[ultima]
                fecha = datetime.strptime(ultima, '%d%m%Y%H%M%S').strftime('%d/%m/%Y %H:%M:%S')
                print_centrado("🕓 Última partida:")
                print_centrado(f"{fecha} - {datos['nombre']} - {datos['resultado']} - 🎲 {datos['lanzamientos']} lanzamientos")
            else:
                print_centrado("📬 No hay partidas aún.")

        elif opcion == "9":
            print_centrado("Gracias por jugar 🌿 ¡Hasta pronto!")
            break

        else:
            print_centrado("❗ Opción inválida, intenta de nuevo.")
