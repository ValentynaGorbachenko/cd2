# test_561.py

import unittest
from arrayPairSum_561 import arrayPairSum

class sortArrayByParityTest(unittest.TestCase):

    def test_sort_array_by_parity_1(self):
        self.assertEqual(arrayPairSum([1,4,3,2]), 4)

    def test_sort_array_by_parity_2(self):
        self.assertEqual(arrayPairSum([]), 0)
    

if __name__ == '__main__':
    unittest.main()