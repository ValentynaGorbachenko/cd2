# test_961.py

import unittest
from repeatedNTimes_961 import repeatedNTimes

class repeatedNTimesTest(unittest.TestCase):

    def test_reteated_n_times_1(self):
        self.assertEqual(repeatedNTimes([1,2,3,3]), 3)

    def test_reteated_n_times_2(self):
        self.assertEqual(repeatedNTimes([]), None)

    def test_reteated_n_times_3(self):
        self.assertEqual(repeatedNTimes([5,1,5,2,5,3,5,4]), 5)

    

if __name__ == '__main__':
    unittest.main()