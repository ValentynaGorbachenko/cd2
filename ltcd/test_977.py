# test_977.py

import unittest
from sortedSquares_977 import sortedSquares#, sortedSquares2
from sortedSquares_977 import sortedSquares2
class sortArrayByParityTest(unittest.TestCase):

    def test_sort_array_by_parity_1(self):
        self.assertEqual(sortedSquares([-4,-1,0,3,10]), [0,1,9,16,100])

    def test_sort_array_by_parity_2(self):
        self.assertEqual(sortedSquares([-7,-3,2,3,11]), [4,9,9,49,121])

    def test_sort_array_by_parity_3(self):
        self.assertEqual(sortedSquares([]), [])

    def test_sort_array_by_parity_11(self):
        self.assertEqual(sortedSquares2([-4,-1,0,3,10]), [0,1,9,16,100])

    def test_sort_array_by_parity_22(self):
        self.assertEqual(sortedSquares2([-7,-3,2,3,11]), [4,9,9,49,121])

    def test_sort_array_by_parity_33(self):
        self.assertEqual(sortedSquares2([]), [])
    

if __name__ == '__main__':
    unittest.main()