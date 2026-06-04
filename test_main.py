import unittest
# Import the functions from your calc.py file
from main import add, subtract, multiply, divide

class TestCalculator(unittest.TestCase):

    # Test 1: Does addition work?
    def test_addition(self):
        self.assertEqual(add(10, 5), 15)
        self.assertEqual(add(-1, 1), 0)

    # Test 2: Does subtraction work?
    def test_subtraction(self):
        self.assertEqual(subtract(10, 5), 5)

    # Test 3: Does multiplication work?
    def test_multiplication(self):
        self.assertEqual(multiply(10, 5), 50)

    # Test 4: Does division work normally?
    def test_division(self):
        self.assertEqual(divide(10, 2), 5)

    # Test 5: Does it handle dividing by zero safely?
    def test_divide_by_zero(self):
        self.assertEqual(divide(10, 0), "Cannot divide by zero")

if __name__ == '__main__':
    unittest.main()