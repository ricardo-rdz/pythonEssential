class Cuenta:

    def __init__(self):
        self.__saldo = 0

    def abonar(self, cantidad):
        self.__saldo += cantidad

    def retirar(self, cantidad):
        if (cantidad > self.__saldo):
            print("Fondos insuficientes")
        else:
            self.__saldo -= cantidad
            print("cantidad retirada: ", cantidad)

    def consultarSaldo(self):
        return self.__saldo