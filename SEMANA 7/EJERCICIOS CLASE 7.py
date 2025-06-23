
# CREACION DE CLASES:



class Cuenta:
    def __init__(self,numcta,saldo):
        self.__numcta = numcta
        self.__saldo = saldo
    def get_numcta(self):
        return self.__numcta
    def get_saldo(self):
        return self.__saldo
    def set_retiro(self,retiro):
        self.__saldo -= retiro
    def set_deposito(self,deposito):
        self.__saldo += deposito

class Banco:
    def __init__(self,nombre):
        self.__nombre = nombre
    def get_banco(self):
        return self.__nombre
    def transferirDinero(self, ctaOrigen, ctaDestino, monto):
        # LA FUNCION isintance(obejto,clase) verifica si un objeto pertenece a una clase
        # ESPECICFICA, VERIFICA SI ctaOrigen y ctaDestino pertenezcana a la clase cuenta :)
        if not isinstance(ctaOrigen, Cuenta) or not isinstance(ctaDestino, Cuenta):
            print("Error: Ambos objetos deben ser instancias de la clase Cuenta.")
            return
        if ctaOrigen.get_numcta() != ctaDestino.get_numcta():
            if  ctaOrigen.get_saldo() >= monto:
                ctaOrigen.set_retiro(monto)
                ctaDestino.set_deposito(monto)
                print("Transferencia exitosa")
            else:
             print(f"Fondos insuficientes en cuenta {ctaOrigen.get_numcta()} ")
        else:
             print("No se puede transferir hacia si mismo")

Banco1 = Banco('BBVA')
Banco2 = Banco('BCP')

Cuenta1 = Cuenta(12345,5000)
Cuenta2 = Cuenta(56789,0)

Banco1.transferirDinero(Cuenta1,Cuenta2,500)

Cuenta1.get_saldo()
print(f"-------- TRANSFERENCIA EN EL BANCO {Banco1.get_banco()}--------")
print(f"Saldo en la cuenta Origen: {Cuenta1.get_saldo()}")
print(f"Saldo en la cuenta Destino: {Cuenta2.get_saldo()}")



                                                                               