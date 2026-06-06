class Auto:
    def __init__(self):
        self.__marca = ""
        self.__modelo = ""
        self.__color = ""
        self.__motor = None

    def set_marca(self, m):
        self.__marca = m

    def set_modelo(self, mo):
        self.__modelo = mo

    def set_color(self, c):
        self.__color = c

    def set_motor(self, motor):
        self.__motor = motor

    def get_marca(self):
        return self.__marca

    def get_modelo(self):
        return self.__modelo

    def get_color(self):
        return self.__color

    def get_motor(self):
        return self.__motor