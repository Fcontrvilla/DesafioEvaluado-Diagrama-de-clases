

from pregunta import Pregunta

class Encuesta:
    def __init__(self, nombre: str, preguntas_data):
        # Inicializa el nombre de la encuesta
        self.__nombre = nombre
        # Crea una lista de objetos Pregunta a partir de los datos proporcionados
        # preguntas_data se espera que sea una lista de diccionarios
        self.__preguntas = [Pregunta(p['enunciado'], p['alternativas_data'], p.get('ayuda'), p.get('requerida', False)) for p in preguntas_data]
        # Inicializa una lista vacía para los listados de respuestas
        self.__listados_respuestas = []

    @property
    def nombre(self) -> str:
        # Permite leer el nombre de la encuesta
        return self.__nombre

    @nombre.setter
    def nombre(self, new_nombre: str) -> None:
        # Permite modificar el nombre de la encuesta
        self.__nombre = new_nombre

    @property
    def preguntas(self):
        # Permite leer la lista de preguntas
        return self.__preguntas

    @property
    def listados_respuestas(self):
        # Permite leer la lista de listados de respuestas
        return self.__listados_respuestas

    def mostrar_encuesta(self) -> None:
        # Muestra el nombre de la encuesta
        print(f"\n--- Encuesta: {self.__nombre} ---")
        # Itera sobre las preguntas y llama a su método para mostrarlas
        for preg in self.__preguntas:
            preg.mostrar_pregunta()
        print("--------------------------")

    def agregar_listado_respuestas(self, listado_respuestas) -> None:
        # Agrega un listado de respuestas a la lista de la encuesta
        # Se asume que listado_respuestas es una instancia de ListadoRespuestas
        self.__listados_respuestas.append(listado_respuestas)
        print(f"Listado de respuestas agregado a la encuesta '{self.nombre}'.")


class EncuestaLimitadaEdad(Encuesta):
    def __init__(self, nombre: str, preguntas_data, edad_minima: int, edad_maxima: int) -> None:
        # Llama al constructor de la clase padre (Encuesta)
        super().__init__(nombre, preguntas_data)
        # Inicializa la edad mínima permitida
        self.__edad_minima = edad_minima
        # Inicializa la edad máxima permitida
        self.__edad_maxima = edad_maxima

    @property
    def edad_minima(self) -> int:
        # Permite leer la edad mínima
        return self.__edad_minima

    @edad_minima.setter
    def edad_minima(self, new_edad: int) -> None:
        # Permite modificar la edad mínima
        self.__edad_minima = new_edad

    @property
    def edad_maxima(self) -> int:
        # Permite leer la edad máxima
        return self.__edad_maxima

    @edad_maxima.setter
    def edad_maxima(self, new_edad: int) -> None:
        # Permite modificar la edad máxima
        self.__edad_maxima = new_edad

    def agregar_listado_respuestas(self, listado_respuestas) -> None:
        # Sobreescribe el método para agregar validación de edad
        # Se importa Usuario localmente para evitar dependencia circular si no se usa mucho
        from usuario import Usuario
        if isinstance(listado_respuestas.usuario, Usuario):
            user_edad = listado_respuestas.usuario.edad
            if self.__edad_minima <= user_edad <= self.__edad_maxima:
                # Si la edad está en el rango, se agrega el listado de respuestas
                super().agregar_listado_respuestas(listado_respuestas)
            else:
                # Si la edad no está en el rango, se imprime un error
                print(f"ERROR: El usuario {listado_respuestas.usuario.correo} tiene {user_edad} años, lo cual está fuera del rango ({self.__edad_minima}-{self.__edad_maxima}) para esta encuesta.")
        else:
            print("ERROR: El usuario asociado al listado de respuestas no es una instancia de Usuario.")


class EncuestaLimitadaRegion(Encuesta):
    def __init__(self, nombre: str, preguntas_data, regiones) -> None:
        # Llama al constructor de la clase padre (Encuesta)
        super().__init__(nombre, preguntas_data)
        # Inicializa la lista de regiones permitidas
        self.__regiones = regiones

    @property
    def regiones(self):
        # Permite leer la lista de regiones
        return self.__regiones

    @regiones.setter
    def regiones(self, new_regiones) -> None:
        # Permite modificar la lista de regiones
        self.__regiones = new_regiones

    def agregar_listado_respuestas(self, listado_respuestas) -> None:
        # Sobreescribe el método para agregar validación de región
        # Se importa Usuario localmente para evitar dependencia circular si no se usa mucho
        from usuario import Usuario
        if isinstance(listado_respuestas.usuario, Usuario):
            user_region = listado_respuestas.usuario.region
            if user_region in self.__regiones:
                # Si la región está permitida, se agrega el listado de respuestas
                super().agregar_listado_respuestas(listado_respuestas)
            else:
                # Si la región no está permitida, se imprime un error
                print(f"ERROR: La región ({user_region}) del usuario {listado_respuestas.usuario.correo} no está permitida para esta encuesta ({self.__regiones}).")
        else:
            print("ERROR: El usuario asociado al listado de respuestas no es una instancia de Usuario.")
