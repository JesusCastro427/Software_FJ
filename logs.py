
# Importamos las librerias necesarias para administrar los registros.
import logging
import os


# Obtenemos la ruta de la carpeta donde se encuentra este archivo.
CARPETA_PROYECTO = os.path.dirname(os.path.abspath(__file__))

# Definimos la carpeta donde se almacenaran los registros.
CARPETA_REGISTROS = os.path.join(CARPETA_PROYECTO, "registros")

# Creamos la carpeta automaticamente si todavia no existe.
os.makedirs(CARPETA_REGISTROS, exist_ok=True)

# Definimos la ruta completa del archivo de eventos.
ARCHIVO_LOG = os.path.join(CARPETA_REGISTROS, "eventos.log")

# Configuramos el sistema de registro de eventos y errores.
logging.basicConfig(
    filename=ARCHIVO_LOG,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    encoding="utf-8",
    force=True
)


# Funcion para registrar eventos y operaciones exitosas.
def registrar_evento(mensaje):
    logging.info(mensaje)


# Funcion para registrar errores controlados.
def registrar_error(mensaje):
    logging.error(mensaje)


# Funcion para registrar errores con informacion detallada.
def registrar_error_completo(mensaje):
    logging.exception(mensaje)
