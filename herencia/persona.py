class Persona:

    def __init__(self):
        self.__nombre = ""
        self.__correo = ""
        self.__telefono = ""
        self.__id = 0

    def set_nombre(self, nombre):
        self.__nombre = nombre

    def set_correo(self, correo):
        self.__correo = correo

    def set_telefono(self, telefono):
        self.__telefono = telefono

    def set_id(self, id):
        self.__id = id

    def get_nombre(self):
        return self.__nombre

    def get_correo(self):
        return self.__correo

    def get_telefono(self):
        return self.__telefono

    def get_id(self):
        return self.__id
        