import logging
import os


# Crear carpeta de registros si no existe
os.makedirs("registros", exist_ok=True)


# Configurar el archivo de registro
logging.basicConfig(
    filename="registros/eventos.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    encoding="utf-8",
    force=True
)


def registrar_evento(mensaje):
    logging.info(mensaje)


def registrar_error(mensaje):
    logging.error(mensaje)


def registrar_error_completo(mensaje):
    logging.exception(mensaje)