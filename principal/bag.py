import api
import logs 

logger = logs.get_logger()

class Bag:
    def __init__(self):
        self.items = {}

    def add(self, item):
        if item in self.items:
            self.items[item] += 1  # Aumenta la cantidad si ya existe
        else:
            self.items[item] = 1  # Si no existe, lo agrega con cantidad 1

    def remove(self, item):
        if item in self.items:
            if self.items[item] > 1:
                self.items[item] -= 1  # Disminuye la cantidad
            else:
                del self.items[item]  # Elimina el item si la cantidad es 1
        else:
            print(f"Item {item} no encontrado.")

    def contains(self, item):
        return item in self.items

    def size(self):
        return sum(self.items.values())  # Devuelve el total de elementos

    def __str__(self):
        return str(self.items)

razas = Bag()
for raza in api.lista_personajes:
    razas.add(raza['race']) 
    logger.info(raza["race"] + " añadido a la bolsa")



