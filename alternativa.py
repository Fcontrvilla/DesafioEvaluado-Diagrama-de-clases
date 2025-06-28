

class Alternativa:
    def __init__(self, contenido: str, ayuda: str = None):
        self.__contenido = contenido
        self.__ayuda = ayuda  #opcional

    @property
    def contenido(self) -> str:   #lee contenido
        return self.__contenido

    @contenido.setter
    def contenido(self, new_contenido: str):  #modifica contenido
        self.__contenido = new_contenido

    @property
    def ayuda(self) -> str:     #lee ayuda
        return self.__ayuda

    @ayuda.setter
    def ayuda(self, new_ayuda: str):   #modifica ayuda
        self.__ayuda = new_ayuda

    def mostrar_alternativa(self):    #muestra contenido y ayuda si hay
        if self.__ayuda:
            print(f"---contenido: {self.__contenido} (Ayuda: {self.__ayuda})")
        else:
            print(f"---contenido: {self.__contenido}")