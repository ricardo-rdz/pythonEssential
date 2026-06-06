class Cliente:
    def __init__(self):
        self.__nombre = ""
        self.__telefono = 0
        self.__cuenta = None

    def set_nombre(self, nombre):
        self.__nombre = nombre

    def set_telefono(self, telefono):
        self.__telefono = telefono
    
    def set_cuenta(self, cuenta):
        self.__cuenta = cuenta

    def get_nombre(self):
        return self.__nombre

    def get_telefono(self):
        return self.__telefono

    def get_cuenta(self):
        return self.__cuenta
