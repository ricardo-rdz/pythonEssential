from persona import Persona

class Profesor(Persona):

    def __init__(self):
        self.__horas= 0
        self.__pago = 0

    def set_horas(self, horas):
        self.__horas = horas

    def set_pago(self, pago):
        self.__pago = pago

    def get_horas(self):
        return self.__horas

    def get_pago(self):
        return self.__pago