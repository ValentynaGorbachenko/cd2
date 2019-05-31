# is_test.py
import unittest
from InsertionSort import sortIS

class InsertionSortTest(unittest.TestCase):
	
	def test_empty_array(self):
		self.assertEqual(sortIS([]), [])
	
	def test_one_value_array(self):
		self.assertEqual(sortIS([2]), [2])

	def test_sort1(self):
		self.assertEqual(sortIS([4,0,3,1,-1,2]), [-1,0,1,2,3,4])
	
	def test_sort2(self):
		self.assertEqual(sortIS([2,-1]), [-1, 2])
	
	def test_different_type_string(self):
		with self.assertRaises(TypeError):
			sortIS("string")
	
	def test_different_type_number(self):
		with self.assertRaises(TypeError):
			sortIS(3)
	
	def test_different_type_None(self):
		with self.assertRaises(TypeError):
			sortIS(None)

if __name__ == '__main__':
	unittest.main()