import unittest
import math
import main

class TestCalculator(unittest.TestCase):

    def test_add(self):
        self.assertEqual(main.add(2, 3), 5) 
        self.assertEqual(main.add(-1, 1), 0)
        self.assertEqual(main.add(0, 0), 0)

    def test_sub(self):
        self.assertEqual(main.sub(10, 5), 5)
        self.assertEqual(main.sub(0, 5), -5)
        self.assertEqual(main.sub(-3, -3), 0)

    def test_mul(self):
        self.assertEqual(main.mul(3, 4), 12)
        self.assertEqual(main.mul(-2, 3), -6)
        self.assertEqual(main.mul(0, 100), 0)

    def test_div(self):
        self.assertEqual(main.div(10, 2), 5)
        self.assertAlmostEqual(main.div(1, 3), 0.333333, places=5)
        with self.assertRaises(ZeroDivisionError):
            main.div(10, 0)

    def test_mod(self):
        self.assertEqual(main.mod(10, 3), 1)
        self.assertEqual(main.mod(10, 5), 0)
        self.assertEqual(main.mod(7, 2), 1)

    def test_power(self):
        self.assertEqual(main.power(2, 3), 8)
        self.assertEqual(main.power(5, 0), 1)
        self.assertEqual(main.power(2, -1), 0.5)

    def test_sqrt(self):
        self.assertEqual(main.my_sqrt(9), 3)
        self.assertEqual(main.my_sqrt(0), 0)
        self.assertAlmostEqual(main.my_sqrt(2), 1.414213, places=5)
        with self.assertRaises(ValueError):
            main.my_sqrt(-1)

    def test_floor(self):
        self.assertEqual(main.my_floor(3.7), 3)
        self.assertEqual(main.my_floor(-3.1), -4)
        self.assertEqual(main.my_floor(5.0), 5)

    def test_ceil(self):
        self.assertEqual(main.my_ceil(3.1), 4)
        self.assertEqual(main.my_ceil(-3.7), -3)
        self.assertEqual(main.my_ceil(5.0), 5)

    def test_sin(self):
        self.assertAlmostEqual(main.my_sin(0), 0, places=5)
        self.assertAlmostEqual(main.my_sin(math.pi / 2), 1, places=5)
        self.assertAlmostEqual(main.my_sin(math.pi), 0, places=5)

    def test_cos(self):
        self.assertAlmostEqual(main.my_cos(0), 1, places=5)
        self.assertAlmostEqual(main.my_cos(math.pi), -1, places=5)
        self.assertAlmostEqual(main.my_cos(math.pi / 2), 0, places=5)

    def test_memory(self):
        main.m_clear()
        self.assertEqual(main.memory, 0)
        main.m_plus(5)
        self.assertEqual(main.memory, 5)
        main.m_plus(3)
        self.assertEqual(main.memory, 8)
        main.m_minus(2)
        self.assertEqual(main.memory, 6)
        main.m_clear()
        self.assertEqual(main.memory, 0)


if __name__ == '__main__':
    unittest.main()