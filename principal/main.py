import queu  
from logs import get_logger
import stack 
import bag
import api
import json


logger = get_logger()

logger.info("creando emparejamiento de personajes para el torneo de poder")
print("Enfrentamientos del Torneo de Poder:")

enfrentamientos = []
try:
    while queu.mitad_1 and queu.mitad_2:
        personaje1 = queu.mitad_1.popleft()  # El primer personaje de la primera mitad
        personaje2 = queu.mitad_2.popleft()  # El primer personaje de la segunda mitad
        # Mostrar el enfrentamiento entre los personajes
        logger.info(f"Enfrentamiento: {personaje1} vs {personaje2}")
        enfrentamientos.append((personaje1, personaje2))

        with open('principal/archivos json/torneoDragonball.json', 'w') as file:  
            json.dump(enfrentamientos,file,indent=4)  
except Exception as e:
    logger.error(f"Error al procesar los enfrentamientos: {e}")



poderObjetivo = int(1000000)
nombreKiPersonajes = []


for poder in api.lista_personajes:
    try:
        ki_value = poder['ki'].replace('.', '')  # Reemplazar  los puntos
        if int(ki_value) > poderObjetivo:  # Convertir a entero después de eliminar los puntos
            stack.rastreadorPoder.push(ki_value)
            logger.info(f" {poder['name']} añadido a la pila con poder {ki_value}" + "y sobre escrito en archivo json") 
            nombreKiPersonajes.append({'name': poder['name'], 'ki': ki_value})
        with open('principal/archivos json/rastreoPoder.json', 'w') as file:  # escribir en json
            json.dump(nombreKiPersonajes,file,indent=4)  
    except ValueError:
        logger.error(f"Valor no válido para 'ki' en el personaje: {poder['name']}") 

logger.info("poderes de los personajes rastreados y guardados en rastreoPoder.json")
print("Poder de los personajes en el Torneo de Poder: ")
print(stack.rastreadorPoder.stack)





razalist = []
for raza in api.lista_personajes:
    try:
        # Solo agregar el nombre del personaje a la cola
        bag.razas.add(raza['race']) 
        logger.info(f" {raza['race']} añadido a la bolsa")
        razalist.append(raza['race'])
        with open('principal/archivos json/razas.json', 'w') as file:  
                json.dump(razalist,file,indent=4)
    except Exception as e:
        logger.error(f"Error al procesar la raza): {e}")

listaCantidadRazas = []
listaCantidadRazas.append("cantidad de razas en la bolsa " + str(bag.razas.size()))

try:
    with open('principal/archivos json/razas.json',"a") as file:  
     json.dump(listaCantidadRazas,file,indent=4)    
except Exception as e:
    logger.error(f"Error al escribir en razas.json: {e}")      

print(bag.razas.size())
print(bag.razas)
