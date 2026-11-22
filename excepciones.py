class SoftwareFJError(Exception):
    """Excepcion general del sistema Software FJ."""
    pass


class ClienteInvalidoError(SoftwareFJError):
    """Error cuando los datos de un cliente son incorrectos."""
    pass


class ServicioNoDisponibleError(SoftwareFJError):
    """Error cuando un servicio no esta disponible."""
    pass


class ReservaInvalidaError(SoftwareFJError):
    """Error cuando una reserva no cumple las condiciones."""
    pass


class OperacionNoPermitidaError(SoftwareFJError):
    """Error cuando se intenta realizar una operacion no permitida."""
    pass