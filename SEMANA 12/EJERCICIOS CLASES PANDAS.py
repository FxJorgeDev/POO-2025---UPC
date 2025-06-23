# EJERCICIO 1
import pandas as pd
import numpy as np
import os
from datetime import datetime
import matplotlib.pyplot as plt
""""
codigo = [1,2,3,4]
#if not os.path.exists("PRIMER CSV.csv")
diccionario_zoo = ({"Nombre":["Simba","Pablo","Lucho","kira"],
                    "Especie":["Leon","Tucan","Tigre","Delfin"],
                    "Fecha Ingreso":["1/5/2020","12/07/2021","15/4/2022","3/6/2019"],
                    "Zonas":["Mamiferos","Aves","Mamiferos","Acuaticos"],
                    "Visitas":[5000,3000,6000,7000],
                    "Estado":["Saludable","Saludable","En tratamiento","Saludable"],
                    "Alimentacion":["Carne","Frutas","Carne","Pescado"]})
diccionario_zonas = ({"Zonas":["Mamiferos","Aves","Acuaticos","Reptiles"],
                    "Descripcion": ["Zona dedicada a los mamiferos","Zona de las aves tropicales","Zona de animales acuaticos","Zona de las serpientes y las reptiles"]})
excel_pd = pd.DataFrame(diccionario_zoo,index=codigo)
zonas = pd.DataFrame(diccionario_zonas)
with pd.ExcelWriter("zoologico.xlsx") as writer:
    excel_pd.to_excel(writer,sheet_name="animales",index=False)
    zonas.to_excel(writer,sheet_name="zonas",index=False)
excel_zonas = pd.read_excel("zoologico.xlsx",sheet_name="zonas")
excel_animales = pd.read_excel("zoologico.xlsx",sheet_name="animales")
def mostrar():
    print("=== ANIMALES ===")
    print(excel_animales)
    print("=== zONAS ===")
    print(excel_zonas)

def datos_menor_mayor():

    animal_visitas = excel_animales["Visitas"].max() 
    resultado_mayor = excel_animales[excel_animales["Visitas"] == animal_visitas]
    print("====DATOS DEL ANIMAL CON MAYOR CANTIDAD DE VISITAS====")
    if not resultado_mayor.empty:
        print(resultado_mayor.to_string(index=False))
    else:
        pass
    print()
    animal_visitas = excel_animales["Visitas"].min()
    resultado_menor = excel_animales[excel_animales["Visitas"] == animal_visitas]
    print("====DATOS DEL ANIMAL CON MENOR CANTIDAD DE VISITAS===")
    if not resultado_menor.empty:
        print(resultado_menor.to_string(index=False))
    else:
        pass
def busqueda_por_especie():
        print("==== BUSQUEDA DE ANIMALES X ESPECIES ====")
        especie = input("Ingrese la especie del zoo a buscar: ")
        resultado_busqueda = excel_animales[excel_animales["Especie"] == especie]
        if not resultado_busqueda.empty:
            print(resultado_busqueda.to_string(index=True))
        else:
            print("NO SE ENCONTRO LA ESPECIE")

def busqueda_por_fecha(): 
    print("=== BUSQUEDA DE ANIMALES POR FECHAS ===")
    excel_animales["Fecha Ingreso"] = pd.to_datetime(excel_animales["Fecha Ingreso"],dayfirst=True)
    while True:
        try:
            fecha_inicio = input("Ingrese el fecha de inicio la busqueda (dd/mm/yyyy): ")
            fecha_final = input("Ingrese el fecha final la busqueda (dd/mm/yyyy): ")
            fecha_inicio = datetime.strptime(fecha_inicio,"%d/%m/%Y")
            fecha_final = datetime.strptime(fecha_final,"%d/%m/%Y")
            break
        except:
            print("ERROR EN LAS FECHAS  ")
    resultado_fecha = excel_animales[(excel_animales["Fecha Ingreso"] >= fecha_inicio) & (excel_animales["Fecha Ingreso"] <= fecha_final)]
    if not resultado_fecha.empty:
        print(resultado_fecha.to_string(index=False))
    else:
        print("NO HAY REGISTRO DE INGRESO EN ESAS FECHAS")

def animal_por_zona():
    print("=== ANIMALES POR ZONA ===")
    zona = input("Ingrese la zona a buscar: ")
    resultado_zona = excel_animales[excel_animales["Zonas"] == zona]
    print(f"Zona de {zona}")
    if not resultado_zona.empty:
        print(resultado_zona.to_string(index=True))
    else:
        print("No hay registro de animales en esa zona")
def grafico():
    cont_m = (excel_animales["Zonas"] == "Mamiferos").sum()
    cont_a = (excel_animales["Zonas"] == "Aves").sum()
    cont_ac = (excel_animales["Zonas"] == "Acuaticos").sum()
    cont_r = (excel_animales["Zonas"] == "Reptiles").sum()

    zonas_lista = ["Mamiferos", "Aves", "Acuaticos", "Reptiles"]
    cantidad = [cont_m,cont_a,cont_ac,cont_r]
    plt.bar(zonas_lista,cantidad,color = "blue")
    plt.title("=== GRAFICO DE BARRAS SENCILLO CON MATPLOPT ===")
    plt.xlabel("Zonas")
    plt.ylabel("Cantidad")
    plt.grid(axis="y", linestyle="--", alpha=0.6)
    plt.show()
def menu():
    print("=== MENU ZOOLOGICO ===")
    print("1. Mostrar Animales y zonas del Zoo")
    print("2. Mostrar Animal con Mayor y menor numero de Visitas")
    print("3. Busqueda por Especie")
    print("4. Busqueda por rango de fechas")
    print("5. Busqueda por Zona")
    print("6. Grafico de barras por zonas")
    print("7. Salir")
    opcion = -1
    while opcion < 0 or opcion > 7:
        try:
            opcion = int(input("Ingrese su opcion: "))
            if opcion > 0 and opcion < 8:
                return opcion
            else:
                print("Opcion fuera de rango")
            break
        except:
            print("ERROR OPCION")
def main():
    while True:
        opcion = menu()
        match opcion:
            case 1:
                mostrar()
            case 2:
                datos_menor_mayor()
            case 3:
                busqueda_por_especie()
            case 4:
                busqueda_por_fecha()
            case 5:
                animal_por_zona()
            case 6:
                grafico()
            case 7:
                break
    print("Saliendo del programa...")
main() """


# EJERCICIO 3 DE CLASE CON LA LIBRERIA MATPLOT

excel_comu = pd.read_excel(r"C:\Users\ASUS\Downloads\Empresas_Telecomunicaciones.xlsx")
excel_comu.to_excel("Empresas_Telecomunicaciones.xlsx",index=False)
csv_comu = excel_comu.to_csv("Empresas_Telecomunicaciones.csv",index=False)
print(excel_comu.info())
nombre = str(input("Ingresa Nombre de la empresa: "))
periodo = str(input("Periodo: "))
altas = int(input("Altas: "))
bajas = int(input("Bajas: "))
perdida = int(input("Perdidas: "))
codigo = nombre[0:3].upper() + periodo
nuevos_datos = pd.DataFrame({"Codigo":[codigo],
                            "Empresa":[nombre],
                            "Periodo":[periodo],
                            "Altas":[altas],
                            "Bajas":[bajas],
                            "Perdidas":[perdida]})
# el pd.concat agrega los datos ingresados manualmente y los llena al excel
excel_comu = pd.concat([excel_comu,nuevos_datos])
# esta linea guarda los datos ingresadps en la dirrecion misma del excel donde queremos agregar..si queremos agregar a otra direccion o otro excel solo cambiamos la direccion
excel_comu.to_excel(r"C:\Users\ASUS\Downloads\Empresas_Telecomunicaciones.xlsx",index=False)

print(excel_comu)
print()
print("== DATAFRAME DE PERDIDAS ===")
excel_perdida = pd.DataFrame(excel_comu["Perdidas"])
print(excel_perdida)
print(excel_perdida.info())
print()
print("=== GRAFICO EN MATPLOT CON PERDIDAS ===")
empresa = str(input("Ingresa nombre de la empresa a graficar perdidas: "))

df_empresa = excel_comu[excel_comu["Empresa"] == empresa].copy()
df_empresa["Perdidas"] = df_empresa["Perdidas"].str.replace('%', '', regex=False)
df_empresa["Perdidas"] = pd.to_numeric(df_empresa["Perdidas"], errors="coerce")

# dp.groupby -> lo que hace es armar grupos con las llaves y el reset index pues ordenalos idices
df_agrupado = df_empresa.groupby("Periodo")["Perdidas"].sum().reset_index()

# Ordenar por año si no están en orden
df_agrupado = df_agrupado.sort_values("Periodo")
# Graficar
plt.figure(figsize=(8, 5))
plt.bar(df_agrupado["Periodo"].astype(str), df_agrupado["Perdidas"], color ="orange",edgecolor="black")
plt.title(f"Evolución de Pérdidas por Año - Empresa {empresa}")
plt.xlabel("Año")
plt.ylabel("Pérdidas Acumuladas")
plt.grid(axis="y",linestyle="--", alpha=0.5)
plt.tight_layout()
plt.show()