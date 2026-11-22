
# Importar las clases necesarias para el funcionamiento del sistema
from clientes import Cliente
from servicios import (
    ReservaSala,
    AlquilerEquipos,
    AsesoriaEspecializada
)
from reservas import Reserva

# Importar las excepciones personalizadas
from excepciones import (
    SoftwareFJError,
    ClienteInvalidoError,
    ReservaInvalidaError,
    ServicioNoDisponibleError
)

# Importar las funciones para registrar eventos y errores
from logs import (
    registrar_evento,
    registrar_error,
    registrar_error_completo
)


# Clase principal para administrar clientes, servicios y reservas
class SistemaGestion:

    def __init__(self):
        # Crear listas privadas para almacenar la informacion
        self.__clientes = []
        self.__servicios = []
        self.__reservas = []

    # Registrar un nuevo cliente
    def registrar_cliente(self, cliente):
        self.__clientes.append(cliente)
        registrar_evento(f"Cliente registrado: {cliente.nombre}")

    # Registrar un nuevo servicio
    def registrar_servicio(self, servicio):
        self.__servicios.append(servicio)
        registrar_evento(f"Servicio registrado: {servicio.nombre}")

    # Registrar una nueva reserva
    def crear_reserva(self, reserva):
        self.__reservas.append(reserva)
        registrar_evento(f"Reserva creada: {reserva.identificador}")

    # Mostrar todos los clientes registrados
    def mostrar_clientes(self):
        for cliente in self.__clientes:
            print(cliente.mostrar_informacion())
            print("-" * 40)

    # Mostrar todos los servicios disponibles
    def mostrar_servicios(self):
        for servicio in self.__servicios:
            print(servicio.mostrar_informacion())
            print(servicio.describir_servicio())
            print("-" * 40)

    # Mostrar todas las reservas registradas
    def mostrar_reservas(self):
        for reserva in self.__reservas:
            print(reserva.mostrar_informacion())
            print("-" * 40)


# Funcion para ejecutar operaciones y controlar posibles errores
def ejecutar_operacion(numero, descripcion, funcion):

    print(f"\n========== OPERACION {numero} ==========")
    print(descripcion)

    try:
        # Ejecutar la operacion correspondiente
        funcion()

    # Capturar las excepciones personalizadas del sistema
    except SoftwareFJError as error:
        print(f"Error controlado: {error}")

        # Comprobar si existe una excepcion original encadenada
        if error.__cause__ is not None:
            print(f"Causa original: {error.__cause__}")

            registrar_error_completo(
                f"Operacion {numero}: Error encadenado"
            )
        else:
            registrar_error(f"Operacion {numero}: {error}")

    # Capturar errores relacionados con datos y atributos
    except (ValueError, TypeError, AttributeError) as error:
        print(f"Error de datos: {error}")
        registrar_error(f"Operacion {numero}: {error}")

    # Capturar cualquier otro error inesperado
    except Exception as error:
        print(f"Error inesperado: {error}")
        registrar_error_completo(
            f"Error inesperado en operacion {numero}"
        )

    # Ejecutar cuando no se presentan errores
    else:
        print("Operacion ejecutada correctamente.")
        registrar_evento(
            f"Operacion {numero} ejecutada correctamente."
        )

    # Ejecutar siempre, ocurra o no un error
    finally:
        print("Finalizacion de la operacion.")
        registrar_evento(
            f"Finalizacion de la operacion {numero}."
        )


# Funcion principal del programa
def main():

    # Crear el sistema de gestion
    sistema = SistemaGestion()

    print("=" * 55)
    print(" SISTEMA INTEGRAL DE GESTION - SOFTWARE FJ")
    print("=" * 55)

    # OPERACION 1: Registrar cliente valido
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

    # OPERACION 2: Intentar registrar cliente invalido
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

    # OPERACION 3: Registrar segundo cliente valido
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

    # OPERACION 4: Crear servicio de reserva de sala
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

    # OPERACION 5: Crear servicio de alquiler de equipos
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

    # OPERACION 6: Crear servicio de asesoria especializada
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

    # OPERACION 7: Intentar crear servicio con precio invalido
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

    # OPERACION 8: Crear y confirmar una reserva
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

    # OPERACION 9: Procesar reserva con impuesto y descuento
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

    # OPERACION 10: Intentar reservar un servicio no disponible
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

    # OPERACION 11: Intentar crear reserva con duracion invalida
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

    # OPERACION 12: Crear y cancelar una reserva
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

    # OPERACION 13: Mostrar clientes registrados
    ejecutar_operacion(
        13,
        "Consulta de clientes registrados",
        sistema.mostrar_clientes
    )

    # OPERACION 14: Mostrar servicios registrados
    ejecutar_operacion(
        14,
        "Consulta de servicios registrados",
        sistema.mostrar_servicios
    )

    # OPERACION 15: Mostrar reservas registradas
    ejecutar_operacion(
        15,
        "Consulta de reservas registradas",
        sistema.mostrar_reservas
    )

    # OPERACION 16: Demostrar encadenamiento de excepciones
    def operacion16():

        reserva4 = Reserva(
            "R005",
            cliente1,
            sala,
            2
        )

        # Confirmar la reserva cuando el servicio esta disponible
        reserva4.confirmar()

        # Cambiar la disponibilidad para provocar el error
        sala.cambiar_disponibilidad(False)

        # Procesar la reserva y generar la excepcion encadenada
        reserva4.procesar()

    ejecutar_operacion(
        16,
        "Prueba de encadenamiento de excepciones",
        operacion16
    )

    # Mostrar mensaje de finalizacion del programa
    print("\n" + "=" * 55)
    print("PROCESO FINALIZADO")
    print("El sistema continuo funcionando ante los errores.")
    print("Los eventos y errores fueron registrados en eventos.log.")
    print("=" * 55)

    # Registrar la finalizacion general del sistema
    registrar_evento("Ejecucion general del sistema finalizada.")


# Iniciar el programa
if __name__ == "__main__":
    main()
