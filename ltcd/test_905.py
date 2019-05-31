# test_905.py

import unittest
from sort_by_parity_905 import sortArrayByParity

class sortArrayByParityTest(unittest.TestCase):

    def test_sort_array_by_parity_1(self):
        self.assertEqual(sortArrayByParity([3,1,2,4]), [2,4,1,3])

    def test_sort_array_by_parity_2(self):
        self.assertEqual(sortArrayByParity([]), [])

    def test_sort_array_by_parity_3(self):
        self.assertEqual(sortArrayByParity([5,6,2,8,1,9]), [2, 6, 8, 1, 5, 9])

    

if __name__ == '__main__':
    unittest.main()