import unittest
import calculator

class TestCalculator(unittest.TestCase):

    def test_nothing(self):
        pass

    def test_add(self):
        self.assertEqual(calculator.add(""), 0)
        self.assertEqual(calculator.add("1"), 1)
        self.assertEqual(calculator.add("2"), 2)

if __name__ == '__main__':
    unittest.main()