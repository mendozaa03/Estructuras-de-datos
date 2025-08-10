import logging

# Configuración del logger
logging.basicConfig(
    level=logging.DEBUG,  # Nivel de detalle (puede ser DEBUG, INFO, WARNING, ERROR, CRITICAL)
    format='%(asctime)s - %(levelname)s - %(message)s',  # Formato del mensaje
    handlers=[
        logging.FileHandler("principal/logs/torneo_poder.log"),  # Archivo de log donde se guardarán los registros
        logging.StreamHandler()  # También mostrará los logs en consola
    ]
)

# Función para obtener el logger configurado
def get_logger():
    return logging.getLogger()
