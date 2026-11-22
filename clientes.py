
# Importamos la clase base y la excepcion para clientes.
from entidades import Entidad
from excepciones import ClienteInvalidoError


# Clase que representa a los clientes del sistema.
class Cliente(Entidad):

    # Recibimos los datos necesarios para registrar un cliente.
    def __init__(self, identificador, nombre, correo, telefono):

        # Inicializamos el identificador mediante la clase padre.
        super().__init__(identificador)

        # Guardamos los datos del cliente como atributos privados.
        self.__nombre = nombre
        self.__correo = correo
        self.__telefono = telefono

        # Validamos los datos antes de completar el registro.
        self.validar_datos()

    # Metodo encargado de verificar que los datos del cliente sean correctos.
    def validar_datos(self):

        # Comprobamos que el nombre sea un texto y no este vacio.
        if not isinstance(self.__nombre, str) or not self.__nombre.strip():
            raise ClienteInvalidoError("El nombre no es valido.")

        # Comprobamos que el correo sea un texto.
        if not isinstance(self.__correo, str):
            raise ClienteInvalidoError("El correo debe ser texto.")

        # Verificamos que el correo tenga una estructura basica valida.
        if (
            "@" not in self.__correo
            or "." not in self.__correo.split("@")[-1]
        ):
            raise ClienteInvalidoError("El correo electronico no es valido.")

        # Comprobamos que el telefono sea un texto.
        if not isinstance(self.__telefono, str):
            raise ClienteInvalidoError("El telefono debe ser texto.")

        # Verificamos que el telefono tenga exactamente diez digitos.
        if not self.__telefono.isdigit() or len(self.__telefono) != 10:
            raise ClienteInvalidoError(
                "El telefono debe contener exactamente 10 digitos."
            )

    # Propiedad para consultar el nombre del cliente.
    @property
    def nombre(self):
        return self.__nombre

    # Propiedad para consultar el correo del cliente.
    @property
    def correo(self):
        return self.__correo

    # Propiedad para consultar el telefono del cliente.
    @property
    def telefono(self):
        return self.__telefono

    # Sobrescribimos el metodo abstracto de la clase Entidad.
    def mostrar_informacion(self):

        # Retornamos todos los datos del cliente en formato de texto.
        return (
            f"Identificador: {self.identificador}\n"
            f"Nombre: {self.__nombre}\n"
            f"Correo: {self.__correo}\n"
            f"Telefono: {self.__telefono}"
        )
