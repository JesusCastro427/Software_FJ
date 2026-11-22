from entidades import Entidad
from excepciones import ClienteInvalidoError


class Cliente(Entidad):

    def __init__(self, identificador, nombre, correo, telefono):
        super().__init__(identificador)

        self.__nombre = nombre
        self.__correo = correo
        self.__telefono = telefono

        self.validar_datos()

    def validar_datos(self):

        if not isinstance(self.__nombre, str) or not self.__nombre.strip():
            raise ClienteInvalidoError("El nombre no es valido.")

        if not isinstance(self.__correo, str):
            raise ClienteInvalidoError("El correo debe ser texto.")

        if "@" not in self.__correo or "." not in self.__correo:
            raise ClienteInvalidoError("El correo electronico no es valido.")

        if not isinstance(self.__telefono, str):
            raise ClienteInvalidoError("El telefono debe ser texto.")

        if not self.__telefono.isdigit() or len(self.__telefono) != 10:
            raise ClienteInvalidoError(
                "El telefono debe contener exactamente 10 digitos."
            )

    @property
    def nombre(self):
        return self.__nombre

    @property
    def correo(self):
        return self.__correo

    @property
    def telefono(self):
        return self.__telefono

    def mostrar_informacion(self):
        return (
            f"Identificador: {self.identificador}\n"
            f"Nombre: {self.__nombre}\n"
            f"Correo: {self.__correo}\n"
            f"Telefono: {self.__telefono}"
        )