class Pastel:

    def __init__(self):
        self.__sabor = ""
        self.__precio = 0
        self.__tam = 0

    def set_sabor(self,s):
        self.__sabor = s

    def set_precio(self,p):
        self.__precio = p

    def get_sabor(self):
        return self.__sabor

    def get_tam(self):
        return self.__tam

    def get_precio(self):
        return self.__precio

    def descuento(self, d):
        descuento = self.__precio * (d / 100)
        return self.__precio - descuento


    
p1 = Pastel()
p1.set_sabor("fresa")
p1.set_precio(250)
    
print(p1.get_sabor())
print(p1.get_precio())
print(p1.descuento(10))
