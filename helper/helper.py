class Helper:
    
    def __init__(self):
        self.__texto = ""
        
    def set_texto(self, texto):
        self.__texto = texto
        
    def get_texto(self):
        return self.__texto
    
    def contarCaracteres(self):
        return len(self.__texto)
    
    def contarVocales(self):
        vocales = "aeiouAEIOU"
        acumulator = 0
        
        for letra in self.__texto:
            if letra in vocales:
                acumulator += 1
        return acumulator
    
    def contarConsonantes(self):
        vocales = "aeiouAEIOU"
        acumulator = 0
        
        for letra in self.__texto:
            if letra not in vocales:
                acumulator += 1
        return acumulator
    
    def voltearCadena(self):
        return self.__texto[::-1]
            
            
            
        
        
    def cambiarPalabraOtraEnCadena(self, str1, str2):
        primeraPalabra = self
        palabraRemplazada = str2
        
        
        return 
        
        
        
    