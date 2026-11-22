from entidades import Entidad
from excepciones import (
    ReservaInvalidaError,
    OperacionNoPermitidaError
)


class Reserva(Entidad):

    def __init__(self, identificador, cliente, servicio, duracion):
        super().__init__(identificador)

        if cliente is None:
            raise ReservaInvalidaError("Debe seleccionar un cliente.")

        if servicio is None:
            raise ReservaInvalidaError("Debe seleccionar un servicio.")

        if not isinstance(duracion, (int, float)) or isinstance(duracion, bool) or duracion <= 0:
            raise ReservaInvalidaError("La duracion debe ser mayor que cero.")

        self.__cliente = cliente
        self.__servicio = servicio
        self.__duracion = duracion
        self.__estado = "Pendiente"
        self.__costo = 0

    @property
    def cliente(self):
        return self.__cliente

    @property
    def servicio(self):
        return self.__servicio

    @property
    def duracion(self):
        return self.__duracion

    @property
    def estado(self):
        return self.__estado

    @property
    def costo(self):
        return self.__costo

    def confirmar(self):
        if self.__estado != "Pendiente":
            raise OperacionNoPermitidaError(
                "Solo se pueden confirmar reservas pendientes."
            )

        self.__servicio.validar_disponibilidad()
        self.__estado = "Confirmada"

    def cancelar(self):
        if self.__estado == "Cancelada":
            raise OperacionNoPermitidaError(
                "La reserva ya se encuentra cancelada."
            )

        if self.__estado == "Procesada":
            raise OperacionNoPermitidaError(
                "No se puede cancelar una reserva procesada."
            )

        self.__estado = "Cancelada"

    def procesar(self, impuesto=0, descuento=0):
        if self.__estado != "Confirmada":
            raise OperacionNoPermitidaError(
                "La reserva debe estar confirmada para procesarse."
            )

        try:
            self.__costo = self.__servicio.calcular_costo(
                self.__duracion,
                impuesto,
                descuento
            )

            if self.__costo < 0:
                raise ValueError("El costo calculado no puede ser negativo.")

            self.__estado = "Procesada"
            return self.__costo

        except Exception as error:
            raise ReservaInvalidaError(
                "No fue posible procesar la reserva."
            ) from error

    def mostrar_informacion(self):
        return (
            f"Reserva: {self.identificador}\n"
            f"Cliente: {self.__cliente.nombre}\n"
            f"Servicio: {self.__servicio.nombre}\n"
            f"Duracion: {self.__duracion}\n"
            f"Estado: {self.__estado}\n"
            f"Costo: ${self.__costo:,.0f}"
        )