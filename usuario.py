

# importamos ListadoRespuestas dentro del método 'contestar_encuesta' donde realmente se usa

class Usuario:
    def __init__(self, correo: str, edad: int, region: int) -> None:
        # El constructor del Usuario.
        # Recibe un correo, una edad y una región para identificar al usuario.
        self.__correo = correo
        self.__edad = edad
        self.__region = region

    @property
    def correo(self) -> str:
        # Permite leer el correo del usuario.
        return self.__correo

    @correo.setter
    def correo(self, new_correo: str) -> None:
        # Permite modificar el correo del usuario.
        self.__correo = new_correo

    @property
    def edad(self) -> int:
        # Permite leer la edad del usuario.
        return self.__edad

    @edad.setter
    def edad(self, new_edad: int) -> None:
        # Permite modificar la edad del usuario.
        self.__edad = new_edad

    @property
    def region(self) -> int:
        # Permite leer la región del usuario.
        return self.__region

    @region.setter
    def region(self, new_region: int) -> None:
        # Permite modificar la región del usuario.
        self.__region = new_region

    def contestar_encuesta(self, encuesta, respuestas):
        # Este método es la acción principal del usuario: contestar una encuesta.
        # Recibe el objeto 'encuesta' a contestar y la lista de 'respuestas' del usuario.
        from listado_respuestas import ListadoRespuestas # Importación local para evitar circularidad.
        
        # Crea un nuevo objeto ListadoRespuestas, asociándolo a este usuario y sus respuestas.
        listado_resp = ListadoRespuestas(self, respuestas)
        
        # Le dice a la encuesta que agregue este nuevo listado de respuestas.
        # La encuesta (especialmente las limitadas) validará si el usuario puede contestar.
        encuesta.agregar_listado_respuestas(listado_resp)
        
        print(f"Usuario {self.correo} ha contestado la encuesta '{encuesta.nombre}'.")
        return listado_resp