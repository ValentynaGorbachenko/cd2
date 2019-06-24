# 937 

import unittest
from reorderLogFiles import reorderLogFiles4
class TestReorderLogFiles(unittest.TestCase):

    def test_empty_input(self):
        self.assertEqual(reorderLogFiles4([]), [])

    def test_reorder_log_fils(self):
        self.assertEqual(reorderLogFiles4(["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo"]), ["g1 act car","a8 act zoo","ab1 off key dog","a1 9 2 3 1","zo4 4 7"])


    def test_reorder_log_fils2(self):
        self.assertEqual(reorderLogFiles4(["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo","a2 act car"]), ["a2 act car","g1 act car","a8 act zoo","ab1 off key dog","a1 9 2 3 1","zo4 4 7"])



if __name__ == "__main__":
    unittest.main()