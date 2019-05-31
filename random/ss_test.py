# bs_test.py
import unittest
from SelectionSort import sortSS

class SelectionSortTest(unittest.TestCase):

	def test_empty_array(self):
		self.assertEqual(sortSS([]), [])

	def test_one_value_array(self):
		self.assertEqual(sortSS([2]), [2])

	def test_sort1(self):
		self.assertEqual(sortSS([4,0,3,1,-1,2]), [-1,0,1,2,3,4])

	def test_sort2(self):
		self.assertEqual(sortSS([2,-1]), [-1, 2])

	def test_different_type_string(self):
		with self.assertRaises(TypeError):
			sortSS("string")

	def test_different_type_number(self):
		with self.assertRaises(TypeError):
			sortSS(3)

	def test_different_type_None(self):
		with self.assertRaises(TypeError):
			sortSS(None)

if __name__ == '__main__':
	unittest.main()