from alternativa import Alternativa

class Pregunta:
    def __init__(self, enunciado: str, alternativas_data, ayuda=None, requerida=False):
        self.__enunciado = enunciado
        self.__ayuda = ayuda
        self.__requerida = requerida
        # Crea una lista de objetos Alternativa a partir de los datos proporcionados.
        # 'alternativas_data' se espera que sea una lista de diccionarios, donde cada diccionario
        # contiene al menos 'contenido' y opcionalmente 'ayuda'.
        self.__alternativas = [Alternativa(a['contenido'], a.get('ayuda')) for a in alternativas_data]

    @property
    def enunciado(self):
        # Permite leer el enunciado de la pregunta.
        return self.__enunciado

    @enunciado.setter
    def enunciado(self, new_enunciado: str):
        # Permite modificar el enunciado de la pregunta.
        self.__enunciado = new_enunciado

    @property
    def ayuda(self):
        # Permite leer la ayuda de la pregunta.
        return self.__ayuda

    @ayuda.setter
    def ayuda(self, new_ayuda):
        # Permite modificar la ayuda de la pregunta.
        self.__ayuda = new_ayuda

    @property
    def requerida(self):
        # Permite leer si la pregunta es requerida.
        return self.__requerida

    @requerida.setter
    def requerida(self, new_requerida: bool):
        # Permite modificar si la pregunta es requerida.
        self.__requerida = new_requerida

    @property
    def alternativas(self):
        # Permite consultar la lista de alternativas.
        # Las alternativas solo se pueden consultar, no modificar directamente desde aquí
        # para mantener la integridad de las opciones de la pregunta.
        return self.__alternativas

    def mostrar_pregunta(self):
        # Muestra el enunciado de la pregunta.
        print(f"Pregunta: {self.__enunciado}")
        # Si hay ayuda para la pregunta, la muestra.
        if self.__ayuda:
            print(f"  Ayuda de la pregunta: {self.__ayuda}")
        print("  Alternativas:")
        # Itera sobre las alternativas asociadas a esta pregunta y llama a su
        # método 'mostrar_alternativa' para presentarlas al usuario.
        for alt in self.__alternativas:
            alt.mostrar_alternativa()
