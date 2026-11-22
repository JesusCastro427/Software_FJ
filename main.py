
# Importamos la clase encargada de administrar los clientes.
from clientes import Cliente

# Importamos las clases de los diferentes servicios.
from servicios import (
    ReservaSala,
    AlquilerEquipos,
    AsesoriaEspecializada
)

# Importamos la clase que administra las reservas.
from reservas import Reserva

# Importamos las excepciones generales del sistema.
from excepciones import SoftwareFJError

# Importamos las funciones para registrar eventos y errores.
from logs import (
    registrar_evento,
    registrar_error,
    registrar_error_completo
)


# Clase principal que administra la informacion del sistema.
class SistemaGestion:

    # Inicializamos las listas donde se guardan los registros.
    def __init__(self):
        self.__clientes = []
        self.__servicios = []
        self.__reservas = []

    # Metodo para registrar clientes.
    def registrar_cliente(self, cliente):
        self.__clientes.append(cliente)
        registrar_evento(f"Cliente registrado: {cliente.nombre}")

    # Metodo para registrar servicios.
    def registrar_servicio(self, servicio):
        self.__servicios.append(servicio)
        registrar_evento(f"Servicio registrado: {servicio.nombre}")

    # Metodo para registrar reservas.
    def crear_reserva(self, reserva):
        self.__reservas.append(reserva)
        registrar_evento(f"Reserva creada: {reserva.identificador}")

    # Metodo para mostrar todos los clientes registrados.
    def mostrar_clientes(self):

        for cliente in self.__clientes:
            print(cliente.mostrar_informacion())
            print("-" * 40)

    # Metodo para mostrar los servicios registrados.
    def mostrar_servicios(self):

        for servicio in self.__servicios:
            print(servicio.mostrar_informacion())
            print(servicio.describir_servicio())
            print("-" * 40)

    # Metodo para mostrar las reservas registradas.
    def mostrar_reservas(self):

        for reserva in self.__reservas:
            print(reserva.mostrar_informacion())
            print("-" * 40)


# Funcion general para ejecutar operaciones con control de excepciones.
def ejecutar_operacion(numero, descripcion, funcion):

    print(f"\n========== OPERACION {numero} ==========")
    print(descripcion)

    try:
        # Ejecutamos la funcion correspondiente a cada operacion.
        funcion()

    except SoftwareFJError as error:

        # Mostramos los errores personalizados del sistema.
        print(f"Error controlado: {error}")

        # Registramos el error en el archivo de eventos.
        registrar_error(f"Operacion {numero}: {error}")

        # Si existe una causa original, tambien la mostramos.
        if error.__cause__ is not None:
            print(f"Causa original: {error.__cause__}")
            registrar_error(
                f"Causa original de operacion {numero}: {error.__cause__}"
            )

    except (ValueError, TypeError, AttributeError) as error:

        # Controlamos errores relacionados con los datos.
        print(f"Error de datos: {error}")
        registrar_error(f"Operacion {numero}: {error}")

    except Exception as error:

        # Capturamos cualquier otro error no previsto.
        print(f"Error inesperado: {error}")
        registrar_error_completo(
            f"Error inesperado en operacion {numero}"
        )

    else:

        # Este bloque se ejecuta cuando no ocurre ninguna excepcion.
        print("Operacion ejecutada correctamente.")
        registrar_evento(
            f"Operacion {numero} ejecutada correctamente."
        )

    finally:

        # Este bloque siempre se ejecuta al terminar la operacion.
        print("Finalizacion de la operacion.")
        registrar_evento(
            f"Finalizacion de la operacion {numero}."
        )


# Funcion principal que ejecuta el sistema integral de gestion.
def main():

    # Creamos el objeto encargado de administrar el sistema.
    sistema = SistemaGestion()

    # Mostramos el encabezado principal del programa.
    print("=" * 55)
    print(" SISTEMA INTEGRAL DE GESTION - SOFTWARE FJ")
    print("=" * 55)

    # OPERACION 1: Registrar un cliente valido.

    cliente1 = None

    def operacion1():
        nonlocal cliente1

        cliente1 = Cliente(
            "C001",
            "Jesus Castro",
            "jesus@gmail.com",
            "3001234567"
        )

        sistema.registrar_cliente(cliente1)
        print(cliente1.mostrar_informacion())

    ejecutar_operacion(
        1,
        "Registro de cliente valido",
        operacion1
    )

    # OPERACION 2: Intentar registrar un cliente con datos incorrectos.

    def operacion2():

        cliente_invalido = Cliente(
            "C002",
            "",
            "correo_incorrecto",
            "123"
        )

        sistema.registrar_cliente(cliente_invalido)

    ejecutar_operacion(
        2,
        "Registro de cliente con datos incorrectos",
        operacion2
    )

    # OPERACION 3: Registrar un segundo cliente valido.

    cliente2 = None

    def operacion3():
        nonlocal cliente2

        cliente2 = Cliente(
            "C003",
            "Maria Rodriguez",
            "maria@gmail.com",
            "3109876543"
        )

        sistema.registrar_cliente(cliente2)
        print(cliente2.mostrar_informacion())

    ejecutar_operacion(
        3,
        "Registro de segundo cliente",
        operacion3
    )

    # OPERACION 4: Crear el servicio de reserva de salas.

    sala = None

    def operacion4():
        nonlocal sala

        sala = ReservaSala(
            "S001",
            "Sala de reuniones",
            50000
        )

        sistema.registrar_servicio(sala)
        print(sala.describir_servicio())

    ejecutar_operacion(
        4,
        "Creacion de servicio de reserva de sala",
        operacion4
    )

    # OPERACION 5: Crear el servicio de alquiler de equipos.

    equipo = None

    def operacion5():
        nonlocal equipo

        equipo = AlquilerEquipos(
            "S002",
            "Computador portatil",
            20000
        )

        sistema.registrar_servicio(equipo)
        print(equipo.describir_servicio())

    ejecutar_operacion(
        5,
        "Creacion de servicio de alquiler de equipos",
        operacion5
    )

    # OPERACION 6: Crear el servicio de asesoria especializada.

    asesoria = None

    def operacion6():
        nonlocal asesoria

        asesoria = AsesoriaEspecializada(
            "S003",
            "Asesoria de software",
            80000
        )

        sistema.registrar_servicio(asesoria)
        print(asesoria.describir_servicio())

    ejecutar_operacion(
        6,
        "Creacion de servicio de asesoria especializada",
        operacion6
    )

    # OPERACION 7: Intentar crear un servicio con precio negativo.

    def operacion7():

        servicio_invalido = ReservaSala(
            "S004",
            "Sala invalida",
            -5000
        )

        sistema.registrar_servicio(servicio_invalido)

    ejecutar_operacion(
        7,
        "Creacion de servicio con precio incorrecto",
        operacion7
    )

    # OPERACION 8: Crear y confirmar una reserva.

    reserva1 = None

    def operacion8():
        nonlocal reserva1

        reserva1 = Reserva(
            "R001",
            cliente1,
            sala,
            2
        )

        sistema.crear_reserva(reserva1)
        reserva1.confirmar()

        print(reserva1.mostrar_informacion())

    ejecutar_operacion(
        8,
        "Creacion y confirmacion de reserva",
        operacion8
    )

    # OPERACION 9: Procesar la reserva aplicando impuesto y descuento.

    def operacion9():

        costo = reserva1.procesar(
            impuesto=19,
            descuento=5000
        )

        print(f"Costo final de la reserva: ${costo:,.0f}")

    ejecutar_operacion(
        9,
        "Procesamiento de reserva con impuesto y descuento",
        operacion9
    )

    # OPERACION 10: Intentar reservar un servicio no disponible.

    def operacion10():

        equipo.cambiar_disponibilidad(False)

        reserva2 = Reserva(
            "R002",
            cliente2,
            equipo,
            3
        )

        sistema.crear_reserva(reserva2)
        reserva2.confirmar()

    ejecutar_operacion(
        10,
        "Intento de reserva de servicio no disponible",
        operacion10
    )

    # OPERACION 11: Intentar crear una reserva con duracion negativa.

    def operacion11():

        reserva_invalida = Reserva(
            "R003",
            cliente1,
            asesoria,
            -2
        )

        sistema.crear_reserva(reserva_invalida)

    ejecutar_operacion(
        11,
        "Intento de crear reserva con duracion negativa",
        operacion11
    )

    # OPERACION 12: Crear y cancelar una reserva.

    def operacion12():

        reserva3 = Reserva(
            "R004",
            cliente2,
            asesoria,
            2
        )

        sistema.crear_reserva(reserva3)
        reserva3.cancelar()

        print(reserva3.mostrar_informacion())

    ejecutar_operacion(
        12,
        "Cancelacion de reserva",
        operacion12
    )

    # OPERACION 13: Consultar los clientes registrados.

    ejecutar_operacion(
        13,
        "Consulta de clientes registrados",
        sistema.mostrar_clientes
    )

    # OPERACION 14: Consultar los servicios registrados.

    ejecutar_operacion(
        14,
        "Consulta de servicios registrados",
        sistema.mostrar_servicios
    )

    # OPERACION 15: Consultar las reservas registradas.

    ejecutar_operacion(
        15,
        "Consulta de reservas registradas",
        sistema.mostrar_reservas
    )

    # OPERACION 16: Demostrar el encadenamiento de excepciones.

    def operacion16():

        # Creamos una nueva reserva para realizar la prueba.
        reserva4 = Reserva(
            "R005",
            cliente1,
            sala,
            2
        )

        # Confirmamos la reserva cuando el servicio esta disponible.
        reserva4.confirmar()

        # Cambiamos la disponibilidad despues de confirmar.
        sala.cambiar_disponibilidad(False)

        # Intentamos procesar la reserva y provocamos el error.
        # La excepcion original se encadena con ReservaInvalidaError.
        reserva4.procesar()

    ejecutar_operacion(
        16,
        "Prueba de encadenamiento de excepciones",
        operacion16
    )

    # Mostramos el mensaje de finalizacion del programa.
    print("\n" + "=" * 55)
    print("PROCESO FINALIZADO")
    print("El sistema continuo funcionando ante los errores.")
    print("Los eventos y errores fueron registrados en eventos.log.")
    print("=" * 55)

    # Registramos la finalizacion general del sistema.
    registrar_evento("Ejecucion general del sistema finalizada.")


# Ejecutamos el programa solamente cuando se abre este archivo directamente.
if __name__ == "__main__":
    main()
