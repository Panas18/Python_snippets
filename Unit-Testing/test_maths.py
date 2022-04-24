import unittest
import maths

class TestMaths(unittest.TestCase):

    def test_area(self):
        self.assertEqual(maths.area(10), 314.16)
        self.assertEqual(maths.area(0), 0)
        with self.assertRaises(ValueError):
            maths.area(-10)

    def test_circumference(self):
        self.assertEqual(maths.cicumference(10), 62.83)
        self.assertEqual(maths.area(0), 0)
        with self.assertRaises(ValueError):
            maths.area(-10)


if __name__ == "__main__":
    unittest.main()
