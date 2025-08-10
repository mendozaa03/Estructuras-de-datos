import requests
from collections import deque
from logs import get_logger

logger = get_logger()

url = "https://dragonball-api.com/api/characters"
logger.info(f"haciendo request de datos a la api {url}")
response = requests.get(url)
logger.info("Data obetenida de la API, se procede a almacenar en un json")
data = response.json()
logger.info("data guardada en archivo json con exito")

lista_personajes = data['items']
logger.info("guardando intems de la api en una lista")


