from collections import deque
from cliente import Cliente
from cuenta import Cuenta

class Cajero:
    def __init__(self):
        self.__fila = deque()

        cli1 = Cliente()
        cli1.set_nombre("Juan")
        cli1.set_telefono(123456789)
        cuenta1 = Cuenta()
        cli1.set_cuenta(cuenta1)

        cli2 = Cliente()
        cli2.set_nombre("Maria")
        cli2.set_telefono(987654321)
        cuenta2 = Cuenta()
        cli2.set_cuenta(cuenta2)

        cli3 = Cliente()
        cli3.set_nombre("Pedro")
        cli3.set_telefono(555555555)
        cuenta3 = Cuenta()
        cli3.set_cuenta(cuenta3)

        cli4 = Cliente()
        cli4.set_nombre("Ana")
        cli4.set_telefono(111111111)
        cuenta4 = Cuenta()
        cli4.set_cuenta(cuenta4)

        cli5 = Cliente()
        cli5.set_nombre("Luis")
        cli5.set_telefono(222222222)
        cuenta5 = Cuenta()
        cli5.set_cuenta(cuenta5)

    def pasar(self):
            
        while self.__fila:
            cliente = self.__fila.popleft()
            print("bienvenido: ", cliente.get_nombre())

            opc = ""

        while opc != "4":
            print("1. Abonar")
            print("2. Retirar")
            print("3. Consultar saldo")
            print("4. Salir")

            opc = input("Seleccione una opcion: ")

            if opc == "1":
                        cantidad = float(input("Ingrese la cantidad a abonar: "))
                        cliente.get_cuenta().abonar(cantidad)
                        print("Cantidad abonada: ", cantidad)

            elif opc == "2":
                        cantidad = float(input("Ingrese la cantidad a retirar: "))
                        cliente.get_cuenta().retirar(cantidad)

            elif opc == "3":
                        saldo = cliente.get_cuenta().consultarSaldo()
                        print("Saldo actual: ", saldo)

            elif opc == "4":
                        print("Gracias por su visita, vuelva pronto!")


