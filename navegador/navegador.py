from pagina import Pagina
from queue import LifoQueue

class Navegador():
    def __init__(self):
        
        
        pag1 = Pagina()
        pag1.set_URL("www.google.com")
        pag1.set_tituloPagina("Google")

        pag2 = Pagina()
        pag2.set_URL("www.facebook.com")
        pag2.set_tituloPagina("Facebook")
        
        pag3 = Pagina()
        pag3.set_URL("www.youtube.com")
        pag3.set_tituloPagina("YouTube")
        
        self.paginas = LifoQueue()
        self.paginas.put(pag1)
        self.paginas.put(pag2)
        self.paginas.put(pag3)
        
        self.paginas2 = LifoQueue()
        self.paginas2.put(pag3)
        self.paginas2.put(pag2)
        self.paginas2.put(pag1)
        
    def adelante(self):
        if(self.paginas2.empty()):
            print("No hay páginas siguientes.")
        else:
            pagina = self.paginas2.get()
            print("Avanzando a la página:", pagina.get_URL())
            print("El título de la página es:", pagina.get_tituloPagina())
        
    def atras(self):
        if(self.paginas.empty()):
            print("No hay páginas anteriores.")
        else:
            pagina = self.paginas.get()
            print("Regresando a la página:", pagina.get_URL())
            print("El título de la página es:", pagina.get_tituloPagina())

        
        