class Motor:

    def __init__(self):
        self.__marca = ""
        self.__serie = ""
        self.__caballos = 0

    def set_marca(self, m):
        self.__marca = m

    def set_serie(self, s):
        self.__serie = s
    
    def set_caballos(self, c):
        self.__caballos = c

    def get_marca(self):
        return self.__marca

    def get_serie(self):
        return self.__serie

    def get_caballos(self):
        return self.__caballos



