

# importamos ListadoRespuestas dentro del método 'contestar_encuesta' donde realmente se usa

class Usuario:
    def __init__(self, correo: str, edad: int, region: int):
        self.__correo = correo
        self.__edad = edad
        self.__region = region

    @property
    def correo(self):
        return self.__correo

    @correo.setter
    def correo(self, new_correo: str):
        self.__correo = new_correo

    @property
    def edad(self):
        return self.__edad

    @edad.setter
    def edad(self, new_edad: int):
        self.__edad = new_edad

    @property
    def region(self):
        return self.__region

    @region.setter
    def region(self, new_region: int):
        self.__region = new_region

    def contestar_encuesta(self, encuesta, respuestas):
        from listado_respuestas import ListadoRespuestas # Importación local para evitar circularidad.
        
        # Crea un nuevo objeto ListadoRespuestas, asociándolo a este usuario y sus respuestas.
        listado_resp = ListadoRespuestas(self, respuestas)
        
        
        encuesta.agregar_listado_respuestas(listado_resp)
        
        print(f"Usuario {self.correo} ha contestado la encuesta '{encuesta.nombre}'.")
        return listado_resp