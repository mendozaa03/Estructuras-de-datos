import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import unittest
from principal.stack import Stack

class TestStack(unittest.TestCase):
    def setUp(self):
        self.stack = Stack()

    def test_push_and_size(self):
        self.stack.push('A')
        self.stack.push('B')
        self.assertEqual(self.stack.size(), 2)

    def test_pop(self):
        self.stack.push('A')
        self.stack.push('B')
        item = self.stack.pop()
        self.assertEqual(item, 'B')
        self.assertEqual(self.stack.size(), 1)

    def test_pop_empty(self):
        result = self.stack.pop()
        self.assertEqual(result, "La pila está vacía")

    def test_peek(self):
        self.stack.push('A')
        self.assertEqual(self.stack.peek(), 'A')
        self.stack.push('B')
        self.assertEqual(self.stack.peek(), 'B')

    def test_peek_empty(self):
        self.assertEqual(self.stack.peek(), "La pila está vacía")

    def test_is_empty(self):
        self.assertTrue(self.stack.is_empty())
        self.stack.push('A')
        self.assertFalse(self.stack.is_empty())

if __name__ == '__main__':
    unittest.main()
