
# Importamos las herramientas necesarias para trabajar con clases abstractas.
from abc import abstractmethod

# Importamos la clase general de las entidades del sistema.
from entidades import Entidad

# Importamos la excepcion para servicios que no estan disponibles.
from excepciones import ServicioNoDisponibleError


# Clase abstracta que representa los servicios de Software FJ.
class Servicio(Entidad):

    # Inicializamos los datos generales de cada servicio.
    def __init__(self, identificador, nombre, precio_base):
        super().__init__(identificador)

        # Validamos que el nombre sea texto y no este vacio.
        if not isinstance(nombre, str) or not nombre.strip():
            raise ValueError("El nombre del servicio no es valido.")

        # Validamos que el precio sea numerico y mayor que cero.
        if (
            not isinstance(precio_base, (int, float))
            or isinstance(precio_base, bool)
            or precio_base <= 0
        ):
            raise ValueError("El precio debe ser mayor que cero.")

        # Guardamos los datos de forma encapsulada.
        self.__nombre = nombre.strip()
        self.__precio_base = float(precio_base)
        self.__disponible = True

    # Permitimos consultar el nombre del servicio.
    @property
    def nombre(self):
        return self.__nombre

    # Permitimos consultar el precio base.
    @property
    def precio_base(self):
        return self.__precio_base

    # Permitimos consultar la disponibilidad.
    @property
    def disponible(self):
        return self.__disponible

    # Cambiamos el estado de disponibilidad del servicio.
    def cambiar_disponibilidad(self, estado):
        if not isinstance(estado, bool):
            raise ValueError("La disponibilidad debe ser True o False.")

        self.__disponible = estado

    # Comprobamos que el servicio este disponible.
    def validar_disponibilidad(self):
        if not self.__disponible:
            raise ServicioNoDisponibleError(
                f"El servicio {self.__nombre} no esta disponible."
            )

    # Validamos los datos generales utilizados en los calculos.
    def validar_calculo(self, duracion, impuesto, descuento):
        self.validar_disponibilidad()

        if (
            not isinstance(duracion, (int, float))
            or isinstance(duracion, bool)
            or duracion <= 0
        ):
            raise ValueError("La duracion debe ser mayor que cero.")

        if (
            not isinstance(impuesto, (int, float))
            or isinstance(impuesto, bool)
            or impuesto < 0
        ):
            raise ValueError("El impuesto no puede ser negativo.")

        if (
            not isinstance(descuento, (int, float))
            or isinstance(descuento, bool)
            or descuento < 0
        ):
            raise ValueError("El descuento no puede ser negativo.")

        subtotal = self.precio_base * duracion

        if descuento > subtotal:
            raise ValueError("El descuento no puede superar el subtotal.")

    # Definimos los metodos que deben implementar los servicios especializados.
    @abstractmethod
    def calcular_costo(self, duracion, impuesto=0, descuento=0):
        pass

    @abstractmethod
    def describir_servicio(self):
        pass

    # Mostramos la informacion general del servicio.
    def mostrar_informacion(self):
        estado = "Disponible" if self.disponible else "No disponible"

        return (
            f"{self.nombre} | Precio base: ${self.precio_base:,.0f} "
            f"| Estado: {estado}"
        )


# Clase especializada para las reservas de salas.
class ReservaSala(Servicio):

    # Sobrescribimos la validacion para las reservas de salas.
    def validar_calculo(self, duracion, impuesto, descuento):
        super().validar_calculo(duracion, impuesto, descuento)

        if duracion > 24:
            raise ValueError("La reserva de sala no puede superar 24 horas.")

    # Calculamos el costo de reservar una sala.
    def calcular_costo(self, duracion, impuesto=0, descuento=0):
        self.validar_calculo(duracion, impuesto, descuento)

        subtotal = self.precio_base * duracion

        return subtotal + (subtotal * impuesto / 100) - descuento

    # Describimos el servicio de reserva de salas.
    def describir_servicio(self):
        return "Reserva de salas de reuniones por horas."


# Clase especializada para el alquiler de equipos.
class AlquilerEquipos(Servicio):

    # Sobrescribimos la validacion para el alquiler de equipos.
    def validar_calculo(self, duracion, impuesto, descuento):
        super().validar_calculo(duracion, impuesto, descuento)

        if duracion > 168:
            raise ValueError("El alquiler no puede superar 168 horas.")

    # Calculamos el costo incluyendo un recargo del 5 por ciento.
    def calcular_costo(self, duracion, impuesto=0, descuento=0):
        self.validar_calculo(duracion, impuesto, descuento)

        subtotal = self.precio_base * duracion
        recargo = subtotal * 0.05

        return subtotal + recargo + (subtotal * impuesto / 100) - descuento

    # Describimos el servicio de alquiler de equipos.
    def describir_servicio(self):
        return "Alquiler de computadores y equipos tecnologicos."


# Clase especializada para las asesorias.
class AsesoriaEspecializada(Servicio):

    # Sobrescribimos la validacion para las asesorias.
    def validar_calculo(self, duracion, impuesto, descuento):
        super().validar_calculo(duracion, impuesto, descuento)

        if duracion > 12:
            raise ValueError("La asesoria no puede superar 12 horas.")

    # Calculamos el costo incluyendo un recargo del 10 por ciento.
    def calcular_costo(self, duracion, impuesto=0, descuento=0):
        self.validar_calculo(duracion, impuesto, descuento)

        subtotal = self.precio_base * duracion
        recargo = subtotal * 0.10

        return subtotal + recargo + (subtotal * impuesto / 100) - descuento

    # Describimos el servicio de asesoria especializada.
    def describir_servicio(self):
        return "Asesorias especializadas en tecnologia y software."
