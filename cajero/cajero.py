import threading
import random
import time
from collections import deque


# =========================
# CLASE CUENTA
# =========================
class Cuenta:

    def __init__(self, saldo_inicial):
        self._saldo = saldo_inicial

    # GET
    @property
    def saldo(self):
        return self._saldo

    # SET con validación
    @saldo.setter
    def saldo(self, nuevo_saldo):

        if nuevo_saldo < 0:
            print("El saldo no puede ser negativo")
        else:
            self._saldo = nuevo_saldo

    def consultar(self):
        return self._saldo

    def abonar(self, cantidad):

        if cantidad > 0:
            self._saldo += cantidad
            return True

        return False

    def retirar(self, cantidad):

        if cantidad <= self._saldo:
            self._saldo -= cantidad
            return True

        return False


# =========================
# CLASE CLIENTE
# =========================
class Cliente:

    def __init__(self, nombre, cuenta):
        self._nombre = nombre
        self._cuenta = cuenta

    @property
    def nombre(self):
        return self._nombre

    @property
    def cuenta(self):
        return self._cuenta


# =========================
# CLASE CAJERO (HILO)
# =========================
class Cajero(threading.Thread):

    def __init__(self, nombre_cajero, cola_clientes):
        super().__init__()
        self.nombre_cajero = nombre_cajero
        self.cola_clientes = cola_clientes

    def run(self):

        while True:

            try:
                cliente = self.cola_clientes.popleft()
            except IndexError:
                print(f"\n{self.nombre_cajero} terminó su fila.")
                break

            self.atender_cliente(cliente)

    def atender_cliente(self, cliente):

        print(f"\n{self.nombre_cajero} atiende a {cliente.nombre}")

        operacion = random.choice([
            "retirar",
            "abonar",
            "consultar"
        ])

        tiempo = random.randint(1, 10)

        time.sleep(tiempo)

        if operacion == "consultar":

            print(
                f"{cliente.nombre} consulta saldo: "
                f"${cliente.cuenta.consultar()}"
            )

        elif operacion == "abonar":

            cantidad = random.randint(100, 1000)

            cliente.cuenta.abonar(cantidad)

            print(
                f"{cliente.nombre} abonó ${cantidad}"
            )

            print(
                f"Nuevo saldo: ${cliente.cuenta.saldo}"
            )

        elif operacion == "retirar":

            cantidad = random.randint(100, 3000)

            if cliente.cuenta.retirar(cantidad):

                print(
                    f"{cliente.nombre} retiró ${cantidad}"
                )

                print(
                    f"Saldo restante: "
                    f"${cliente.cuenta.saldo}"
                )

            else:

                print(
                    f"{cliente.nombre} intentó retirar "
                    f"${cantidad}"
                )

                print(
                    "Fondos insuficientes"
                )


# =========================
# FUNCIÓN PRINCIPAL
# =========================
def main():

    cola_clientes = deque()

    # Crear clientes
    nombres = [
        "Ana",
        "Luis",
        "Carlos",
        "María",
        "Pedro",
        "Sofía",
        "Elena",
        "Miguel",
        "Laura",
        "Jorge"
    ]

    for nombre in nombres:

        saldo_inicial = random.randint(500, 5000)

        cuenta = Cuenta(saldo_inicial)

        cliente = Cliente(nombre, cuenta)

        cola_clientes.append(cliente)

    # Crear 3 cajeros
    cajero1 = Cajero("CAJERO 1", cola_clientes)
    cajero2 = Cajero("CAJERO 2", cola_clientes)
    cajero3 = Cajero("CAJERO 3", cola_clientes)

    # Iniciar hilos
    cajero1.start()
    cajero2.start()
    cajero3.start()

    # Esperar que terminen
    cajero1.join()
    cajero2.join()
    cajero3.join()

    print("\nTodos los clientes fueron atendidos")


# =========================
# EJECUCIÓN
# =========================
if __name__ == "__main__":
    main()