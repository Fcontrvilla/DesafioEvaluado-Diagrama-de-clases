class Alternativa:
    def __init__(self, contenido: str, ayuda: str = None) -> None:
        self.__contenido = contenido
        self.__ayuda = ayuda

    @property
    def contenido(self) -> str:
        return self.__contenido

    @contenido.setter
    def contenido(self, new_contenido: str) -> None:
        self.__contenido = new_contenido

    @property
    def ayuda(self) -> str:
        return self.__ayuda

    @ayuda.setter
    def ayuda(self, new_ayuda: str) -> None:
        self.__ayuda = new_ayuda

    def mostrar_alternativa(self) -> None:
        if self.__ayuda:
            print(f"  - Contenido: {self.__contenido} (Ayuda: {self.__ayuda})")
        else:
            print(f"  - Contenido: {self.__contenido}")