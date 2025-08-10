import unittest
from collections import deque


class TestTorneoPoder(unittest.TestCase):
    def setUp(self):
        # Simula la lista de personajes
        self.lista_personajes = [
            {'name': 'Goku'},
            {'name': 'Vegeta'},
            {'name': 'Freezer'},
            {'name': 'Jiren'}
        ]

    def test_cola_se_agrega_correctamente(self):
        torneo_poder = deque()
        for personaje in self.lista_personajes:
            torneo_poder.append(personaje['name'])
        self.assertEqual(list(torneo_poder), ['Goku', 'Vegeta', 'Freezer', 'Jiren'])

    def test_division_mitades(self):
        torneo_poder = deque(['Goku', 'Vegeta', 'Freezer', 'Jiren'])
        mitad_1 = deque()
        mitad_2 = deque()
        for i in range(len(torneo_poder)//2):
            mitad_1.append(torneo_poder.popleft())
        while torneo_poder:
            mitad_2.append(torneo_poder.popleft())
        self.assertEqual(list(mitad_1), ['Goku', 'Vegeta'])
        self.assertEqual(list(mitad_2), ['Freezer', 'Jiren'])

if __name__ == '__main__':
    unittest.main()
