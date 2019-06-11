# test_804.py

import unittest
from uniqueMorseRepresentations_804 import uniqueMorseRepresentationsClass 
# print (uniqueMorseRepresentationsClass)

class uniqueMorseRepresentationsTest(unittest.TestCase):
    def setUp(self):
        self.func = uniqueMorseRepresentationsClass().uniqueMorseRepresentations
        # print (self.func)
        
    def test_intersect_1(self):
        self.assertEqual(self.func(["Gin", "zen", "gig", "msg"]), 2)
     

if __name__ == '__main__':
    unittest.main()