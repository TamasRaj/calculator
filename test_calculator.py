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
        self.assertEqual(calculator.add("\n10\n20\n30\n"), 60)
        self.assertEqual(calculator.add("\n10\n20\n\n30\n"), 60)

        self.assertEqual(calculator.add("1\n2,3"), 6)
        self.assertEqual(calculator.add("5,7\n9,20"), 41)
        self.assertEqual(calculator.add("10\n20,30\n30,45"), 135)
        self.assertEqual(calculator.add("\n10\n20\n30\n30\n45\n"), 135)

        self.assertEqual(calculator.add("//;\n1"), 1)
        self.assertEqual(calculator.add("//&\n2"), 2)
        self.assertEqual(calculator.add("//%\n4"), 4)

        self.assertEqual(calculator.add("//;\n1;2"), 3)
        self.assertEqual(calculator.add("//&\n5&7"), 12)
        self.assertEqual(calculator.add("//&\n5&7\n20"), 32)

        self.assertRaises(ValueError, calculator.add, "-1")
        self.assertRaises(ValueError, calculator.add, "-1,2")
        self.assertRaises(ValueError, calculator.add, "1,-2")
        self.assertRaises(ValueError, calculator.add, "1,-2,3")

        with self.assertRaises(ValueError) as context:
            calculator.add("-1")
        self.assertEqual(str(context.exception), "negative numbers not allowed -1")

        with self.assertRaises(ValueError) as context:
            calculator.add("-1,2")
        self.assertEqual(str(context.exception), "negative numbers not allowed -1")

        with self.assertRaises(ValueError) as context:
            calculator.add("-1,3,-12")
        self.assertEqual(str(context.exception), "negative numbers not allowed -1, -12")

if __name__ == '__main__':
    unittest.main()