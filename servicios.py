
# Importamos las herramientas para trabajar con clases abstractas.
from abc import abstractmethod

# Importamos la clase base y la excepcion de disponibilidad.
from entidades import Entidad
from excepciones import ServicioNoDisponibleError


# Clase abstracta que representa los servicios ofrecidos por la empresa.
class Servicio(Entidad):

    # Inicializamos los datos generales de cada servicio.
    def __init__(self, identificador, nombre, precio_base):
        super().__init__(identificador)

        # Validamos el nombre del servicio.
        if not isinstance(nombre, str) or not nombre.strip():
            raise ValueError("El nombre del servicio no es valido.")

        # Validamos que el precio sea numerico y mayor que cero.
        if (
            not isinstance(precio_base, (int, float))
            or isinstance(precio_base, bool)
            or precio_base <= 0
        ):
            raise ValueError("El precio debe ser mayor que cero.")

        # Guardamos los datos privados del servicio.
        self.__nombre = nombre.strip()
        self.__precio_base = float(precio_base)
        self.__disponible = True

    # Propiedad para consultar el nombre del servicio.
    @property
    def nombre(self):
        return self.__nombre

    # Propiedad para consultar el precio base.
    @property
    def precio_base(self):
        return self.__precio_base

    # Propiedad para consultar la disponibilidad.
    @property
    def disponible(self):
        return self.__disponible

    # Metodo para cambiar la disponibilidad del servicio.
    def cambiar_disponibilidad(self, estado):

        if not isinstance(estado, bool):
            raise ValueError("La disponibilidad debe ser True o False.")

        self.__disponible = estado

    # Verificamos que el servicio pueda utilizarse.
    def validar_disponibilidad(self):

        if not self.__disponible:
            raise ServicioNoDisponibleError(
                f"El servicio {self.__nombre} no esta disponible."
            )

    # Validacion general de los parametros de calculo.
    def validar_parametros(self, duracion, impuesto, descuento):

        # Comprobamos que la duracion sea numerica y positiva.
        if (
            not isinstance(duracion, (int, float))
            or isinstance(duracion, bool)
            or duracion <= 0
        ):
            raise ValueError("La duracion debe ser mayor que cero.")

        # Verificamos que el impuesto sea un porcentaje valido.
        if (
            not isinstance(impuesto, (int, float))
            or isinstance(impuesto, bool)
            or not 0 <= impuesto <= 100
        ):
            raise ValueError("El impuesto debe estar entre 0 y 100.")

        # Verificamos que el descuento sea un valor numerico no negativo.
        if (
            not isinstance(descuento, (int, float))
            or isinstance(descuento, bool)
            or descuento < 0
        ):
            raise ValueError("El descuento no puede ser negativo.")

        # Calculamos el subtotal para comprobar el descuento.
        subtotal = self.precio_base * duracion

        if descuento > subtotal:
            raise ValueError("El descuento no puede superar el subtotal.")

    # Validamos la disponibilidad y los parametros del calculo.
    def validar_calculo(self, duracion, impuesto, descuento):
        self.validar_disponibilidad()
        self.validar_parametros(duracion, impuesto, descuento)

    # Metodo abstracto que calcula el costo de cada servicio.
    @abstractmethod
    def calcular_costo(self, duracion, impuesto=0, descuento=0):
        pass

    # Metodo abstracto para describir cada tipo de servicio.
    @abstractmethod
    def describir_servicio(self):
        pass

    # Metodo que muestra los datos generales del servicio.
    def mostrar_informacion(self):

        estado = "Disponible" if self.disponible else "No disponible"

        return (
            f"{self.nombre} | Precio base: ${self.precio_base:,.0f} "
            f"| Estado: {estado}"
        )


# Clase derivada que representa la reserva de salas.
class ReservaSala(Servicio):

    # Sobrescribimos la validacion de parametros para este servicio.
    def validar_parametros(self, duracion, impuesto, descuento):
        super().validar_parametros(duracion, impuesto, descuento)

        if duracion > 24:
            raise ValueError("La reserva de sala no puede superar 24 horas.")

    # Calculamos el costo aplicando el impuesto y el descuento.
    def calcular_costo(self, duracion, impuesto=0, descuento=0):

        self.validar_calculo(duracion, impuesto, descuento)

        subtotal = self.precio_base * duracion
        total = subtotal + (subtotal * impuesto / 100) - descuento

        return total

    # Describimos el servicio de reserva de salas.
    def describir_servicio(self):
        return "Reserva de salas de reuniones por horas."


# Clase derivada que representa el alquiler de equipos.
class AlquilerEquipos(Servicio):

    # Sobrescribimos la validacion de parametros del alquiler.
    def validar_parametros(self, duracion, impuesto, descuento):
        super().validar_parametros(duracion, impuesto, descuento)

        if duracion > 720:
            raise ValueError("El alquiler no puede superar 720 horas.")

    # Calculamos el costo incluyendo un recargo del 5 por ciento.
    def calcular_costo(self, duracion, impuesto=0, descuento=0):

        self.validar_calculo(duracion, impuesto, descuento)

        subtotal = self.precio_base * duracion
        recargo = subtotal * 0.05
        total = subtotal + recargo + (subtotal * impuesto / 100) - descuento

        return total

    # Describimos el servicio de alquiler de equipos.
    def describir_servicio(self):
        return "Alquiler de computadores y equipos tecnologicos."


# Clase derivada que representa las asesorias especializadas.
class AsesoriaEspecializada(Servicio):

    # Sobrescribimos la validacion de parametros de la asesoria.
    def validar_parametros(self, duracion, impuesto, descuento):
        super().validar_parametros(duracion, impuesto, descuento)

        if duracion > 12:
            raise ValueError("La asesoria no puede superar 12 horas.")

    # Calculamos el costo incluyendo un recargo del 10 por ciento.
    def calcular_costo(self, duracion, impuesto=0, descuento=0):

        self.validar_calculo(duracion, impuesto, descuento)

        subtotal = self.precio_base * duracion
        recargo = subtotal * 0.10
        total = subtotal + recargo + (subtotal * impuesto / 100) - descuento

        return total

    # Describimos el servicio de asesoria especializada.
    def describir_servicio(self):
        return "Asesorias especializadas en tecnologia y software."
