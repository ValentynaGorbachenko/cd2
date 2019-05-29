# bs.py
import unittest
from BubbleSort import sortBS

# print(sortBS([2, 1,-3,0]))
# print(sortBS([2, 1,0]))
# print(sortBS([]))
# print(sortBS([2]))
# print(sortBS([2, 1]))

class BubbleSortTest(unittest.TestCase):

	def test_empty_array(self):
		self.assertEqual(sortBS([]), [])

	def test_one_value_array(self):
		self.assertEqual(sortBS([2]), [2])

	def test_sort1(self):
		self.assertEqual(sortBS([2,1,3,4,0,-1]), [-1, 0, 1, 2, 3, 4])

	def test_sort2(self):
		self.assertEqual(sortBS([2,-1]), [-1, 2])

	def test_different_type(self):
		with self.assertRaises(TypeError):
			sortBS("string")

if __name__ == '__main__':
	unittest.main()