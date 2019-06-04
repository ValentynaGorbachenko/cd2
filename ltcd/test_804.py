# test_804.py

import unittest
from uniqueMorseRepresentations_804 import uniqueMorseRepresentations

class uniqueMorseRepresentationsTest(unittest.TestCase):
    def test_intersect_1(self):
        self.assertEqual(uniqueMorseRepresentations(["gin", "zen", "gig", "msg"]), 2)
     

if __name__ == '__main__':
    unittest.main()