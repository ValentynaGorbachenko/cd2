# test_771.py

import unittest
from jewels_and_stones_771 import j_and_s_3

class jewels_and_stones(unittest.TestCase):

    def test_j_and_s1(self):
        self.assertTrue(j_and_s_3("aA", "aAAbbbb") == 3)

    def test_j_and_s2(self):
        self.assertTrue(j_and_s_3("z", "ZZ") == 0)

    def test_j_and_s_emptyJ(self):
        self.assertTrue(j_and_s_3("", "ZZ") == 0)

    def test_j_and_s_emptyS(self):
        self.assertTrue(j_and_s_3("as", "") == 0)

if __name__ == '__main__':
    unittest.main()