import unittest
import calculations

class Test_Calculations(unittest.TestCase):

    def test_add(self):
        self.assertEqual(calculatios.add(10, 5), 15)
        self.assertEqual(calculations.add(100, 1), 101)
        self.assertEqual(calculations.add(-88, 88), 0)
        self.assertEqual(calculations.add(2, 2), 4)

    def test_subtract(self):
        self.assertEqual(calculations.subtract(10, 5), 5)
        self.assertEqual(calculations.subtract(100, 1), 99)
        self.assertEqual(calculations.subtract(-88, 88), -176)
        self.assertEqual(calculations.subtract(2, 2), 0)

    def test_divide(self):
        self.assertEqual(calculations.divide(10, 5), 2)
        self.assertEqual(calculations.divide(100, 1), 100)
        self.assertEqual(calculations.divide(-88, 88), -1)
        self.assertEqual(calculations.divide(2, 2), 1)

        # self.assertRaises(ValueError, calculations.divide, 10, 0)

        with self.assertRaises(ValueError):
            n = 10
            l = 0
            calculations.divide(n, l)

        with self.assertRaises(ValueError):
            calculations.divide(99999, 0)

    def test_multiply(self):
        self.assertEqual(calculations.multiply(10, 5), 50)
        self.assertEqual(calculations.multiply(100, 1), 100)
        self.assertEqual(calculations.multiply(-88, 88), -7744)
        self.assertEqual(calculations.multiply(2, 2), 4)
    

if __name__ == '__main__':
    unittest.main()
