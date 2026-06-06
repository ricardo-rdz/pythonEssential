from persona import Persona

class Alumno(Persona):

    def __init__(self):
        self.__carrera = ""
        self.__promedio = 0

    def set_carrera(self, carrera):
        self.__carrera = carrera

    def set_promedio(self, promedio):
        self.__promedio = promedio

    def get_carrera(self):
        return self.__carrera

    def get_promedio(self):
        return self.__promedio