import json
import os
import shutil
import time
import csv
from datetime import datetime
from random import randint

class Jugador:
    def __init__(self, nombre, edad, emoji):
        self.__nombre = nombre
        self.__edad = edad
        self.__emoji = emoji
        self.__posicion = 1
        self.__estado = "en juego"
        self.__lanzamientos = 0

    @property
    def nombre(self): return self.__nombre
    @property
    def edad(self): return self.__edad
    @property
    def emoji(self): return self.__emoji
    @property
    def posicion(self): return self.__posicion
    @posicion.setter
    def posicion(self, valor): self.__posicion = valor
    @property
    def lanzamientos(self): return self.__lanzamientos
    @property
    def estado(self): return self.__estado
    @estado.setter
    def estado(self, valor): self.__estado = valor

    def avanzar_lanzamiento(self): self.__lanzamientos += 1

class Trampas:
    def __init__(self):
        self.__serpiente = randint(5, 11)
        self.__sacrificio = randint(11, 21)
        self.__inundacion = randint(21, 30)
        self.__pozo = randint(30, 38)

    def verificar_obstaculo(self, pos):
        if pos == self.__serpiente:
            print_centrado("🐍 Te atrapa una serpiente. Retrocedes 3 casillas.")
            return pos - 3
        elif pos == self.__sacrificio:
            d = randint(1, 6)
            print_centrado(f"🩸 Sacrificio: retrocedes {d} casillas.")
            return pos - d
        elif pos == self.__inundacion:
            print_centrado("🌊 Inundación. Vuelves al inicio.")
            return 1
        elif pos == self.__pozo:
            d = randint(1, 6)
            print_centrado("🕳 Pozo... lanzando dado...")
            if d % 2 == 1:
                print_centrado("💀 Has perdido.")
                return -1
            print_centrado("😮 Te salvaste.")
        return pos

    def obtener_obstaculos(self):
        return {
            self.__serpiente: "🐍",
            self.__sacrificio: "🩸",
            self.__inundacion: "🌊",
            self.__pozo: "🕳"
        }

class Tablero:
    def __init__(self):
        self.__trampas = Trampas()
    def verificar_obstaculo(self, pos): return self.__trampas.verificar_obstaculo(pos)
    def obtener_obstaculos(self): return self.__trampas.obtener_obstaculos()

class Estadisticas:
    @staticmethod
    def promedio_lanzamientos(partidas):
        if not partidas:
            return 0
        total = sum(p["lanzamientos"] for p in partidas.values())
        return total / len(partidas)

    @staticmethod
    def exportar_a_csv(partidas, archivo="historial.csv"):
        with open(archivo, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["Fecha", "Jugador", "Resultado", "Lanzamientos"])
            for fecha, datos in partidas.items():
                writer.writerow([
                    datetime.strptime(fecha, '%d%m%Y%H%M%S').strftime('%Y-%m-%d %H:%M:%S'),
                    datos["nombre"], datos["resultado"], datos["lanzamientos"]
                ])

class Juego:
    def __init__(self):
        self.__jugadores = []
        self.__emojis_usados = set()
        self.__tablero = None
        self.__partidas = self.cargar_historial()

    def cargar_historial(self):
        if os.path.exists("historial.json"):
            with open("historial.json", "r") as f:
                return json.load(f)
        return {}

    def guardar_historial(self):
        with open("historial.json", "w") as f:
            json.dump(self.__partidas, f, indent=4)
        Estadisticas.exportar_a_csv(self.__partidas)

    def agregar_jugador(self, jugador):
        if jugador.emoji in self.__emojis_usados:
            print_centrado("Emoji ya en uso.")
            return False
        self.__jugadores.append(jugador)
        self.__emojis_usados.add(jugador.emoji)
        return True

    def nuevo_tablero(self): self.__tablero = Tablero()

    def jugar(self):
        if not self.__tablero or not self.__jugadores:
            print_centrado("⚠️ Agrega jugadores y crea tablero.")
            return
        ganador = False
        while not ganador and any(j.estado == "en juego" for j in self.__jugadores):
            for jugador in self.__jugadores:
                if jugador.estado != "en juego":
                    continue
                input(f"{jugador.nombre} ({jugador.emoji}), Enter para lanzar: ")
                dado = randint(1, 6)
                jugador.avanzar_lanzamiento()
                print_centrado(f"🎲 Dado: {dado}")
                nueva_pos = jugador.posicion + dado
                if nueva_pos > 40:
                    nueva_pos = 40 - (nueva_pos - 40)
                    print_centrado(f"🎯 Te pasaste. Retrocedes a {nueva_pos}")
                if nueva_pos == 40:
                    print_centrado("🎉 ¡Ganaste!")
                    jugador.estado = "ganada"
                    jugador.posicion = 40
                    ganador = True
                    break
                nueva_pos = self.__tablero.verificar_obstaculo(nueva_pos)
                if nueva_pos == -1:
                    jugador.estado = "perdida"
                else:
                    jugador.posicion = nueva_pos

        for j in self.__jugadores:
            llave = datetime.now().strftime('%d%m%Y%H%M%S')
            self.__partidas[llave] = {
                "nombre": j.nombre,
                "resultado": j.estado,
                "lanzamientos": j.lanzamientos
            }
        self.guardar_historial()

    def mostrar_historial(self):
        if not self.__partidas:
            print_centrado("No hay partidas registradas.")
            return
        for k, v in self.__partidas.items():
            fecha = datetime.strptime(k, '%d%m%Y%H%M%S').strftime('%d/%m/%Y %H:%M:%S')
            print_centrado(f"{fecha} | {v['nombre']} | {v['resultado']} | {v['lanzamientos']} lanzamientos")

    def mostrar_jugadores(self):
        for j in self.__jugadores:
            print_centrado(f"{j.nombre} ({j.edad}) {j.emoji}")

def print_centrado(txt):
    ancho = shutil.get_terminal_size((80, 20)).columns
    for linea in txt.split("\n"):
        print(linea.center(ancho))

def elegir_emoji(ya_usados):
    emojis = ["🐱", "🐶", "🐸", "🐵", "🦊", "🐯", "🐼"]
    disponibles = [e for e in emojis if e not in ya_usados]
    while True:
        for i, em in enumerate(disponibles, 1):
            print(f"{i}. {em}")
        op = input("Elige un emoji (número): ")
        if op.isdigit() and 1 <= int(op) <= len(disponibles):
            return disponibles[int(op)-1]

def menu():
    juego = Juego()
    while True:
        print_centrado("\n--- MENÚ PRINCIPAL ---")
        print("1. Agregar jugador")
        print("2. Nuevo tablero")
        print("3. Iniciar juego")
        print("4. Ver historial")
        print("5. Ver jugadores")
        print("6. Promedio de lanzamientos")
        print("7. Salir")

        opcion = input("Selecciona una opción: ")
        if opcion == "1":
            nombre = input("Nombre: ")
            edad = int(input("Edad: "))
            emoji = elegir_emoji(juego._Juego__emojis_usados)
            j = Jugador(nombre, edad, emoji)
            if juego.agregar_jugador(j):
                print_centrado(f"✅ {nombre} agregado.")
        elif opcion == "2":
            juego.nuevo_tablero()
            print_centrado("🆕 Tablero creado.")
        elif opcion == "3":
            juego.jugar()
        elif opcion == "4":
            juego.mostrar_historial()
        elif opcion == "5":
            juego.mostrar_jugadores()
        elif opcion == "6":
            prom = Estadisticas.promedio_lanzamientos(juego._Juego__partidas)
            print_centrado(f"📊 Promedio: {prom:.2f} lanzamientos.")
        elif opcion == "7":
            print_centrado("Gracias por jugar 🎮")
            break
        else:
            print("❌ Opción inválida.")

if __name__ == "__main__":
    menu()
