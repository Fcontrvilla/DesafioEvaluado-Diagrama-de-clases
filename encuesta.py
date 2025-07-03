

from pregunta import Pregunta


class Encuesta:
    def __init__(self, nombre: str, preguntas_data):
        self.__nombre = nombre
        # Crea una lista de objetos Pregunta a partir de los datos proporcionados
        self.__preguntas = [Pregunta(p['enunciado'], p['alternativas_data'], p.get('ayuda'), p.get('requerida', False)) for p in preguntas_data]
        self.__listados_respuestas = []

    @property
    def nombre(self):   # lee la encuesta
        return self.__nombre

    @nombre.setter
    def nombre(self, new_nombre: str): #  modifica nombre de la encuesta
        self.__nombre = new_nombre

    @property
    def preguntas(self):
        return self.__preguntas

    @property
    def listados_respuestas(self):
        return self.__listados_respuestas

    def mostrar_encuesta(self):
        print(f"\n--- Encuesta: {self.__nombre} ---")
        
        for preg in self.__preguntas:   # Itera sobre las preguntas y llama a su método para mostrarlas
            preg.mostrar_pregunta()
        print("--------------------------")


    def agregar_listado_respuestas(self, listado_respuestas):
        
        self.__listados_respuestas.append(listado_respuestas)
        print(f"Listado de respuestas agregado a la encuesta '{self.nombre}'.")





class EncuestaLimitadaEdad(Encuesta):
    def __init__(self, nombre: str, preguntas_data, edad_minima: int, edad_maxima: int):
        
        super().__init__(nombre, preguntas_data)
        
        self.__edad_minima = edad_minima
        self.__edad_maxima = edad_maxima

    @property
    def edad_minima(self):
        return self.__edad_minima

    @edad_minima.setter
    def edad_minima(self, new_edad: int) :
        self.__edad_minima = new_edad

    @property
    def edad_maxima(self):
        return self.__edad_maxima

    @edad_maxima.setter
    def edad_maxima(self, new_edad):
        self.__edad_maxima = new_edad

    def agregar_listado_respuestas(self, listado_respuestas):
        
        from usuario import Usuario  # Se importa usuario localmente para evitar dependencia circular si no se usa mucho

        if isinstance(listado_respuestas.usuario, Usuario):
            user_edad = listado_respuestas.usuario.edad
            if self.__edad_minima <= user_edad <= self.__edad_maxima:
                super().agregar_listado_respuestas(listado_respuestas)
            else:
                print(f"ERROR: El usuario {listado_respuestas.usuario.correo} tiene {user_edad} años, lo cual está fuera del rango ({self.__edad_minima}-{self.__edad_maxima}) para esta encuesta.")
        else:
            print("ERROR: El usuario asociado al listado de respuestas no es una instancia de usuario!")


class EncuestaLimitadaRegion(Encuesta):
    def __init__(self, nombre, preguntas_data, regiones):
        
        super().__init__(nombre, preguntas_data)  # Llama al constructor de la clase padre (Encuesta)
        self.__regiones = regiones

    @property
    def regiones(self):
        return self.__regiones

    @regiones.setter
    def regiones(self, new_regiones):
        self.__regiones = new_regiones

    def agregar_listado_respuestas(self, listado_respuestas):
        
        from usuario import Usuario   # Se importa Usuario localmente para evitar dependencia circular si no se usa mucho
        if isinstance(listado_respuestas.usuario, Usuario):
            user_region = listado_respuestas.usuario.region
            if user_region in self.__regiones:
                super().agregar_listado_respuestas(listado_respuestas)
            else:
                print(f"ERROR: La región ({user_region}) del usuario {listado_respuestas.usuario.correo} no está permitida para esta encuesta ({self.__regiones}).")
        else:
            print("ERROR: El usuario asociado al listado de respuestas no es una instancia de usuario.")
