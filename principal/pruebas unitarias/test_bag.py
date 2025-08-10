import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import unittest
from principal.bag import Bag

class TestBag(unittest.TestCase):
    def setUp(self):
        self.bag = Bag()

    def test_add_new_item(self):
        self.bag.add('Saiyan')
        self.assertTrue(self.bag.contains('Saiyan'))
        self.assertEqual(self.bag.items['Saiyan'], 1)

    def test_add_existing_item(self):
        self.bag.add('Saiyan')
        self.bag.add('Saiyan')
        self.assertEqual(self.bag.items['Saiyan'], 2)

    def test_remove_item_decrement(self):
        self.bag.add('Saiyan')
        self.bag.add('Saiyan')
        self.bag.remove('Saiyan')
        self.assertEqual(self.bag.items['Saiyan'], 1)

    def test_remove_item_delete(self):
        self.bag.add('Saiyan')
        self.bag.remove('Saiyan')
        self.assertFalse(self.bag.contains('Saiyan'))

    def test_remove_nonexistent_item(self):
        # No error should be raised, just a print
        self.bag.remove('Namekian')
        self.assertFalse(self.bag.contains('Namekian'))

    def test_size(self):
        self.bag.add('Saiyan')
        self.bag.add('Namekian')
        self.bag.add('Saiyan')
        self.assertEqual(self.bag.size(), 3)

    def test_str(self):
        self.bag.add('Saiyan')
        self.assertEqual(str(self.bag), "{'Saiyan': 1}")

if __name__ == '__main__':
    unittest.main()
