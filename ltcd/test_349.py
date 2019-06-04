# test_349.py

import unittest
from intersection_349 import intersect

class intersectTest(unittest.TestCase):
    def test_intersect_1(self):
        self.assertEqual(intersect([1,2,2,1], [2,2]), [2])
    
    # @unittest.skip("demonstrating skipping")
    def test_intersect_2(self):
        res = intersect([4,4,9,5],[9,4,9,8,4])
        res.sort()
        self.assertEqual(res, [4,9])
    
    def test_intersect_5(self):
        self.assertEqual(intersect([],[]), [])    

if __name__ == '__main__':
    unittest.main()