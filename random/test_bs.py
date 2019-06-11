# test_bs.py
import unittest
from BubbleSort import sortBS

class BubbleSortTest(unittest.TestCase):

    def test_empty_array(self):
        self.assertEqual(sortBS([]), [])

    def test_one_value_array(self):
        self.assertEqual(sortBS([2]), [2])

    def test_sort1(self):
        self.assertEqual(sortBS([2,1,3,4,0,-1]), [-1, 0, 1, 2, 3, 4])

    def test_sort2(self):
        self.assertEqual(sortBS([2,-1]), [-1, 2])

    def test_different_type_string(self):
        with self.assertRaises(TypeError):
            sortBS("string")

    def test_different_type_number(self):
        with self.assertRaises(TypeError):
            sortBS(3)

    def test_different_type_None(self):
        with self.assertRaises(TypeError):
            sortBS(None)

if __name__ == '__main__':
    unittest.main()