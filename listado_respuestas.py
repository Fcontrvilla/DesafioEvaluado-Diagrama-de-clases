# listado_respuestas.py
# No necesita importar nada de 'typing' para su funcionalidad.
# Las clases 'Usuario' y 'Encuesta' se manejarán en otros archivos
# donde se necesiten para evitar dependencias circulares complejas.

class ListadoRespuestas:
    def __init__(self, usuario, respuestas) -> None:
        # El constructor de un Listado de Respuestas.
        # Recibe el objeto 'usuario' que contestó la encuesta,
        # y una lista con las 'respuestas' (por ejemplo, los índices de las alternativas elegidas).
        # Estos se guardan como atributos privados.
        self.__usuario = usuario
        self.__respuestas = respuestas

    @property
    def usuario(self):
        # Este "getter" permite leer el objeto 'usuario' asociado a este listado.
        # No hay "setter" porque, una vez creado, este listado está ligado a ese usuario.
        return self.__usuario

    @property
    def respuestas(self):
        # Este "getter" permite leer la lista de respuestas.
        # Similar al usuario, no hay "setter" para mantener la inmutabilidad del registro de respuestas.
        return self.__respuestas