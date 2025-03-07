import unittest
import calculator

class TestCalculator(unittest.TestCase):

    def test_nothing(self):
        pass

    def test_add(self):
        self.assertEqual(calculator.add(""), 0)
        self.assertEqual(calculator.add("1"), 1)
        self.assertEqual(calculator.add("2"), 2)
        self.assertEqual(calculator.add("10"), 10)
        self.assertEqual(calculator.add("100"), 100)

        self.assertEqual(calculator.add("1,2"), 3)
        self.assertEqual(calculator.add("5,7"), 12)
        self.assertEqual(calculator.add("10,20"), 30)

        self.assertEqual(calculator.add("1,2,3"), 6)
        self.assertEqual(calculator.add("5,7,9,20"), 41)
        self.assertEqual(calculator.add("10,20,30,30,45"), 135)

        self.assertEqual(calculator.add("1,2,3,4,"), 10)
        self.assertEqual(calculator.add("5,7,9,,20"), 41)
        self.assertEqual(calculator.add(",10,,20,30,30,45,"), 135)

        self.assertEqual(calculator.add("1\n2"), 3)
        self.assertEqual(calculator.add("5\n7"), 12)
        self.assertEqual(calculator.add("10\n20\n30"), 60)

if __name__ == '__main__':
    unittest.main()