class Pagina:
    def __init__(self):
        self.__URL = ""
        self.__tituloPagina = ""
        
    def set_URL(self, URL):
        self.__URL = URL
        
    def set_tituloPagina(self, tituloPagina):
        self.__tituloPagina = tituloPagina
        
    def get_URL(self):
        return self.__URL
    
    def get_tituloPagina(self):
        return self.__tituloPagina
    
    def visitarPagina(self, URL):
        self.__URL = URL
        print("Visitando la página:", self.__URL)
        print("El título de la página es:", self.__tituloPagina)
        
    
        
        