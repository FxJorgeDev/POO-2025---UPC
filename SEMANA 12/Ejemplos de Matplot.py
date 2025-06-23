import matplotlib.pyplot as plt
import pandas as pd

x=[1,2,3,4,5]
y = [10,15,8,12,18]

# sintaxis -> plt.plot(list1,lista2,
# label=etiqueta leyenda,
# color=color para la grafica en ingles,
# linestyle=tipo de linea
# marker= marca los puntos ("x","o","^"))
plt.title("PRIMERA GRAFICA")
plt.plot(x,y,label="ventas",color="blue",linestyle="-",marker="s")
plt.xlabel("Semana")
plt.ylabel("Ventas")
plt.legend()
# EL plt.grid -> imprime lineas cuadradas en el grafico
plt.grid(True)

#plt.savefig(r"C:\Users\ASUS\Pictures\GRAFICO.png",dpi=500) 
"el sintaxis ese guarda el archivo impreso por consola en un archivo en en ordenador"
# este comando imprime la grafica en consola
plt.show()
# plt.title(ahi el nombre de la grafica)


x = [1,2,3,4,5]
y1 = [5,7,6,8,7]
y2 = [2,3,4,2,5]
plt.plot(x,y1,label = "A",color="green",linestyle="-",marker="s")
plt.plot(x,y2,label = "B",color="black",linestyle="--",marker="o")
plt.title("== VARIACION DE PRECIOS SEGUNDO GRAFICO == ")
plt.ylabel("dias")
plt.xlabel("ventas")
plt.legend()
plt.grid()
plt.show()

