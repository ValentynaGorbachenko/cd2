# test_441.py

import unittest
from arrangeCoins_441 import arrangeCoins

class arrangeCoinsTest(unittest.TestCase):
    def test_intersect_1(self):
        self.assertEqual(arrangeCoins(5), 2)
    
    # @unittest.skip("demonstrating skipping")
    def test_intersect_2(self):
        self.assertEqual(arrangeCoins(8), 3)
    
    def test_intersect_5(self):
        self.assertEqual(arrangeCoins(0), 0) 

    def test_intersect_3(self):
        self.assertEqual(arrangeCoins(1), 1)   

if __name__ == '__main__':
    unittest.main()