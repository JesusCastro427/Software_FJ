
# Importamos la clase base de las entidades.
from entidades import Entidad

# Importamos las excepciones utilizadas en las reservas.
from excepciones import (
    ReservaInvalidaError,
    OperacionNoPermitidaError
)


# Clase que administra las reservas realizadas por los clientes.
class Reserva(Entidad):

    # Recibimos el identificador, cliente, servicio y duracion.
    def __init__(self, identificador, cliente, servicio, duracion):

        # Inicializamos el identificador mediante la clase padre.
        super().__init__(identificador)

        # Validamos que se haya seleccionado un cliente.
        if cliente is None:
            raise ReservaInvalidaError("Debe seleccionar un cliente.")

        # Validamos que se haya seleccionado un servicio.
        if servicio is None:
            raise ReservaInvalidaError("Debe seleccionar un servicio.")

        # Comprobamos que la duracion sea numerica y positiva.
        if (
            not isinstance(duracion, (int, float))
            or isinstance(duracion, bool)
            or duracion <= 0
        ):
            raise ReservaInvalidaError(
                "La duracion debe ser mayor que cero."
            )

        # Guardamos los datos de la reserva como atributos privados.
        self.__cliente = cliente
        self.__servicio = servicio
        self.__duracion = duracion

        # Inicializamos la reserva con estado pendiente y costo cero.
        self.__estado = "Pendiente"
        self.__costo = 0

    # Propiedad para consultar el cliente asociado a la reserva.
    @property
    def cliente(self):
        return self.__cliente

    # Propiedad para consultar el servicio reservado.
    @property
    def servicio(self):
        return self.__servicio

    # Propiedad para consultar la duracion.
    @property
    def duracion(self):
        return self.__duracion

    # Propiedad para consultar el estado de la reserva.
    @property
    def estado(self):
        return self.__estado

    # Propiedad para consultar el costo calculado.
    @property
    def costo(self):
        return self.__costo

    # Metodo que permite confirmar una reserva pendiente.
    def confirmar(self):

        # Solo se pueden confirmar reservas pendientes.
        if self.__estado != "Pendiente":
            raise OperacionNoPermitidaError(
                "Solo se pueden confirmar reservas pendientes."
            )

        # Verificamos que el servicio se encuentre disponible.
        self.__servicio.validar_disponibilidad()

        # Cambiamos el estado de la reserva.
        self.__estado = "Confirmada"

    # Metodo que permite cancelar una reserva.
    def cancelar(self):

        # Evitamos cancelar una reserva que ya fue cancelada.
        if self.__estado == "Cancelada":
            raise OperacionNoPermitidaError(
                "La reserva ya se encuentra cancelada."
            )

        # No permitimos cancelar una reserva procesada.
        if self.__estado == "Procesada":
            raise OperacionNoPermitidaError(
                "No se puede cancelar una reserva procesada."
            )

        # Actualizamos el estado de la reserva.
        self.__estado = "Cancelada"

    # Procesamos la reserva y calculamos su costo final.
    # Los parametros opcionales permiten aplicar impuesto y descuento.
    def procesar(self, impuesto=0, descuento=0):

        # Verificamos que la reserva este confirmada.
        if self.__estado != "Confirmada":
            raise OperacionNoPermitidaError(
                "La reserva debe estar confirmada para procesarse."
            )

        try:
            # Utilizamos el metodo sobrescrito del servicio correspondiente.
            self.__costo = self.__servicio.calcular_costo(
                self.__duracion,
                impuesto,
                descuento
            )

            # Verificamos que el costo final no sea negativo.
            if self.__costo < 0:
                raise ValueError(
                    "El costo calculado no puede ser negativo."
                )

            # Cambiamos el estado cuando el proceso termina correctamente.
            self.__estado = "Procesada"

            # Retornamos el costo calculado.
            return self.__costo

        except Exception as error:

            # Encadenamos la excepcion original con una excepcion personalizada.
            raise ReservaInvalidaError(
                "No fue posible procesar la reserva."
            ) from error

    # Sobrescribimos el metodo de informacion de la clase Entidad.
    def mostrar_informacion(self):

        # Retornamos los datos completos de la reserva.
        return (
            f"Reserva: {self.identificador}\n"
            f"Cliente: {self.__cliente.nombre}\n"
            f"Servicio: {self.__servicio.nombre}\n"
            f"Duracion: {self.__duracion}\n"
            f"Estado: {self.__estado}\n"
            f"Costo: ${self.__costo:,.0f}"
        )
