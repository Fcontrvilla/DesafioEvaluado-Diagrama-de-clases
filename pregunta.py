from alternativa import Alternativa

class Pregunta:
    def __init__(self, enunciado: str, alternativas_data, ayuda=None, requerida=False):  # 'alternativas_data' debe ser una lista de diccionarios, donde cada diccionario crea una lista de objetos Alternativa a partir de los datos proporcionados
        self.__enunciado = enunciado
        self.__ayuda = ayuda
        self.__requerida = requerida
        self.__alternativas = [Alternativa(a['contenido'], a.get('ayuda')) for a in alternativas_data]   # contiene al menos contenido y opcionalmente ayuda

    @property
    def enunciado(self):    #  leer  enunciado de la pregunta
        return self.__enunciado

    @enunciado.setter
    def enunciado(self, new_enunciado: str):     # modifica el enunciado de la pregunta
        self.__enunciado = new_enunciado

    @property
    def ayuda(self):   # leer la ayuda de la pregunta
        return self.__ayuda

    @ayuda.setter
    def ayuda(self, new_ayuda):     #modifica la ayuda de la pregunta
        self.__ayuda = new_ayuda

    @property
    def requerida(self):  #  leer si la pregunta es requerida
        return self.__requerida

    @requerida.setter
    def requerida(self, new_requerida: bool):  # modifica si la pregunta es requerida
        self.__requerida = new_requerida

    @property
    def alternativas(self):
        return self.__alternativas

    def mostrar_pregunta(self):
        print(f"Pregunta: {self.__enunciado}")   #enunciado
        
        if self.__ayuda:  # Si hay ayuda la muestra
            print(f"  Ayuda de la pregunta: {self.__ayuda}")
        
        print("  Alternativas:")
        for alt in self.__alternativas:
            alt.mostrar_alternativa()  #from clase importada 