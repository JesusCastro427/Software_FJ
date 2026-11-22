
# Importamos ABC y abstractmethod para crear clases abstractas.
from abc import ABC, abstractmethod


# Clase base que representa las entidades generales del sistema.
class Entidad(ABC):

    # Inicializamos las entidades con un identificador unico.
    def __init__(self, identificador):

        # Verificamos que el identificador sea un texto valido.
        if not isinstance(identificador, str) or not identificador.strip():
            raise ValueError("El identificador no puede estar vacio.")

        # Guardamos el identificador como atributo privado.
        self.__identificador = identificador.strip()

    # Propiedad que permite consultar el identificador sin modificarlo directamente.
    @property
    def identificador(self):
        return self.__identificador

    # Metodo abstracto que deben implementar las clases hijas.
    @abstractmethod
    def mostrar_informacion(self):
        pass
