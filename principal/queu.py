import api 
import requests
from collections import deque
from logs import get_logger

logger = get_logger()


torneo_poder = deque()
logger.info("creando cola para el torneo de poder")

logger.info("agregando personajes a la cola del torneo de poder")
for personaje in api.lista_personajes:
    
    torneo_poder.append(personaje['name'])  

logger.info("personajes agregados a la cola con exito")


# Mostrar la cola antes de los enfrentamientos
print("Cola de personajes en el Torneo de Poder: ")
print(torneo_poder)


logger.info("creando dos colas nuevas para añadir las mitades de la cola principal y hacer los enfrentamientos")
mitad_1 = deque()
mitad_2 = deque()

logger.info("dividiendo la cola en dos mitades y almacenando el contenido en las nuevas colas")

try:
    for i in range(len(torneo_poder)//2):
        mitad_1.append(torneo_poder.popleft())

    while torneo_poder:
        mitad_2.append(torneo_poder.popleft())
except Exception as e:
    logger.error(f"Error al dividir la cola: {e}")


