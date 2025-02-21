import unittest
from math_utils import MathUtils

class TestMathUtils(unittest.TestCase):
    """
    Class to control functionality of class MathUtils
    """
    def test_add(self):
        """
        Check for addition, incorporated negative numbers and decimals.
        """
        self.assertEqual(MathUtils.add(1,2),3)
        self.assertEqual(MathUtils.add(1.5, 2.5), 4)
        self.assertEqual(MathUtils.add(-1, 1), 0)
        self.assertEqual(MathUtils.add(-1.5, 1.5), 0)

    def test_subtract(self):
        """
        Check for subtraction, incorporated negative numbers and decimals.
        """
        self.assertEqual(MathUtils.subtract(1, 2),-1)
        self.assertEqual(MathUtils.subtract(1.5, 2.5), -1)
        self.assertEqual(MathUtils.subtract(-1, 1), -2)
        self.assertEqual(MathUtils.subtract(-1.5, -1.5), 0)

    def test_divide(self):
        """
        Check for division, incorporated negative numbers and decimals.
        """
        self.assertEqual(MathUtils.divide(4, 2), 2)
        self.assertEqual(MathUtils.divide(2, 4), 0.5)
        self.assertEqual(MathUtils.divide(3, -2), -1.5)
        self.assertEqual(MathUtils.divide(-8, -4), 2)

    def test_multiply(self):
        """
        Check for multiplication, incorporated negative numbers and decimals.
        """
        self.assertEqual(MathUtils.multiply(4, 2), 8)
        self.assertEqual(MathUtils.multiply(2, 2.5), 5)
        self.assertEqual(MathUtils.multiply(2, -1), -2)
        self.assertEqual(MathUtils.multiply(-2, -1.5), 3)



