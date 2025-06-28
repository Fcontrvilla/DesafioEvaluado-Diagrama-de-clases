

class ListadoRespuestas:
    def __init__(self, usuario, respuestas):
        
        self.__usuario = usuario
        self.__respuestas = respuestas

    @property
    def usuario(self):
        return self.__usuario

    @property
    def respuestas(self):
        return self.__respuestas