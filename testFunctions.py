# Fernando González Colín  #
# Ciudad de México, México #
# gc.fernando.96@gmail.com #
# April, 2019              #
# Simple sample functions  #

import unittest
import numpy as np
from functions import *

class TestFunctions(unittest.TestCase):
    def test_factorial(self):
        self.assertEqual(factorial(0),1)
        self.assertEqual(factorial(1),1)
        self.assertEqual(factorial(2),2)
        self.assertEqual(factorial(3),6)
        self.assertEqual(factorial(4),24)
        self.assertEqual(factorial(5),120)
        self.assertEqual(factorial(7),5040)
        
    def test_isPowerOf(self):
        self.assertEqual(isPowerOf(4,2),True)
        self.assertEqual(isPowerOf(5,2),False)
        self.assertEqual(isPowerOf(9,3),True)
        self.assertEqual(isPowerOf(8,2),True)
        self.assertEqual(isPowerOf(16,4),True)
        self.assertEqual(isPowerOf(4,4),True)
        self.assertEqual(isPowerOf(3,4),False)

    def test_addDigitsUntilOne(self):
        self.assertEqual(addDigitsUntilOne(42),6)
        self.assertEqual(addDigitsUntilOne(57),3)
        self.assertEqual(addDigitsUntilOne(93),3)
        self.assertEqual(addDigitsUntilOne(82),1)
        self.assertEqual(addDigitsUntilOne(164),2)
        self.assertEqual(addDigitsUntilOne(44),8)
        self.assertEqual(addDigitsUntilOne(34),7)
        
    def test_isASimpleProgression(self):
        self.assertEqual(isASimpleProgression([2,4,6,8,10]),True)
        self.assertEqual(isASimpleProgression([2,3,5,6,8,9]),False)
        self.assertEqual(isASimpleProgression([90,82,74,66,58]),True)
        self.assertEqual(isASimpleProgression([11,23,35,47,59]),True)
        self.assertEqual(isASimpleProgression([1,1,1,1,1]),True)
        self.assertEqual(isASimpleProgression([1.25,1.5,1.75,2.0,1.8]),False)
        self.assertEqual(isASimpleProgression([0,0,0,-1,-1]),False)
    
    def test_traveledDistance(self):
        self.assertEqual(traveledDistance(['UP 5','DOWN 3','LEFT 3', 'RIGHT 2']),2.236)
        self.assertEqual(traveledDistance(['DOWN 5','LEFT 5', 'UP 5', 'RIGHT 5']),0.0)
        self.assertEqual(traveledDistance(['RIGHT 2', 'UP 5', 'RIGHT 3', 'DOWN 8', 'LEFT 1']),5.0)
        self.assertEqual(traveledDistance(['LEFT 7', 'DOWN 2', 'DOWN 4', 'LEFT 2', 'DOWN 3']),12.728)
        self.assertEqual(traveledDistance(['UP 4', 'LEFT 5', 'UP 7', 'RIGHT 2', 'UP 3']),14.318)
        self.assertEqual(traveledDistance(['UP 1','UP 2','RIGHT 3','DOWN 2']),3.162)
        self.assertEqual(traveledDistance(['LEFT 5', 'RIGHT 10','UP 2','LEFT 2']),3.606)
    
if __name__ == '__main__':
    unittest.main()