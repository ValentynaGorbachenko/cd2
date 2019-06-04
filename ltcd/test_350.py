# test_350.py

import unittest
from intersect_350 import intersect

class intersectTest(unittest.TestCase):
    def test_intersect_1(self):
        self.assertEqual(intersect([1,2,2,1], [2,2]), [2,2])

    def test_intersect_2(self):
        self.assertEqual(intersect([4,4,9,5],[9,4,9,8,4]), [4,4,9])
    '''
    def test_intersect_3(self):
        self.assertEqual(intersect(["","",""]), [])

    def test_intersect_4(self):
        self.assertEqual(intersect(["acabcddd","bcbdbcbd","baddbadb","cbdddcac","aacbcccd","ccccddda","cababaab","addcaccd"]), []) 
    '''

    def test_intersect_5(self):
        self.assertEqual(intersect([],[]), [])    

if __name__ == '__main__':
    unittest.main()