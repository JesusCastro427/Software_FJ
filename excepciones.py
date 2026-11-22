
# Clase general para los errores propios del sistema Software FJ.
class SoftwareFJError(Exception):
    """Excepcion general del sistema."""
    pass


# Error que se presenta cuando los datos de un cliente son incorrectos.
class ClienteInvalidoError(SoftwareFJError):
    """Error en el registro o validacion de clientes."""
    pass


# Error que se presenta cuando un servicio no se encuentra disponible.
class ServicioNoDisponibleError(SoftwareFJError):
    """Error relacionado con la disponibilidad de los servicios."""
    pass


# Error que se presenta cuando una reserva no cumple las condiciones.
class ReservaInvalidaError(SoftwareFJError):
    """Error en la creacion o procesamiento de reservas."""
    pass


# Error que se presenta cuando una operacion no esta permitida.
class OperacionNoPermitidaError(SoftwareFJError):
    """Error por intentar ejecutar una operacion no permitida."""
    pass
