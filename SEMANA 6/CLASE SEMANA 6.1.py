#EJERCICIO 1 DEL PPT

"""""
class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def imprimir(self):
        print("Coordenada del punto")
        print(f"({self.x}, {self.y})")
    def imprimir_cuadrante(self):
        if self.x == 0 and self.y == 0:
         print('EN el origen')
        elif self.x == 0 and self.y == 0:
         print('EN EL EJE')
        elif self.x > 0 and self.y > 0:
         print("Primer cuadrange")
        elif self.x < 0 and self.y > 0:
         print("Segundo cuadrante")
        elif self.x < 0 and self.y < 0:
         print("Tercer cuadrante")
        else:
            print("Cuarto cuadrante")
# Programa principal
punto1 = Punto(0, -2)
punto1.imprimir()
punto1.imprimir_cuadrante() """


#EJERCICIO 3 PPT

class Cuenta:
    def __init__(self,numcta, saldo):
     self.numcta = numcta
     self.saldo = saldo
    def deposito(self, monto):
        self.saldo += monto
    def retiro(self, retiro):
        self.saldo -= retiro
    def imprime_saldo(self):
        print(f"Saldo de Cuenta: {self.numcta} es {self.saldo}")
        
class Banco:
    def __init__(self, nombre):
        self.nombre = nombre
    def transferirDinero(self, ctaOrigen, ctaDestino, monto):
        if ctaOrigen.numcta != ctaDestino.numcta:
            if ctaOrigen.saldo >= monto:
                ctaOrigen.retiro(monto)
                ctaDestino.deposito(monto)
                print("Transferencia exitosa")
            else:
             print(f"Fondos insuficientes en cuenta {ctaOrigen.numCta} ")
        else:
             print("No se puede transferir hacia si mismo")
             
# Programa Principal
banco = Banco("MI BANCO")
print(f"\nBanco: {banco.nombre}")
cuenta1 = Cuenta(123, 1000)
cuenta1.imprime_saldo()
cuenta2 = Cuenta(345, 300)
cuenta2.imprime_saldo()
banco = Banco("BBVA")
banco.transferirDinero(cuenta1, cuenta2, 300)
print(f"\nBanco: {banco.nombre}")
cuenta1.imprime_saldo()
cuenta2.imprime_saldo()