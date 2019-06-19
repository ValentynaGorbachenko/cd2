import unittest
from heightChecker import heightChecker

class TestHeightChecker(unittest.TestCase):
    def test_zero_elements_in_array(self):
        self.assertEqual(heightChecker([]), 0)

    def test_one_element_array(self):
        self.assertEqual(heightChecker([1]), 0)

    def test_correct_order_of_elements(self):
        self.assertEqual(heightChecker([1,2,3,4,5]), 0)

    def test_wrong_order_of_elements(self):
        self.assertEqual(heightChecker([1,1,4,2,1,3]), 3)


if __name__ == "__main__":
    unittest.main()
        