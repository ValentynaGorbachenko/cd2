# test_1002.py

import unittest
from commonChars_1002 import commonChars

class commonCharsTest(unittest.TestCase):
    def test_common_chars_1(self):
        self.assertEqual(commonChars(["bella","label","roller"]), ["e", "l", "l"])

    def test_common_chars_2(self):
        self.assertEqual(commonChars(["cool","lock","cook"]), ["c", "o"])

    def test_common_chars_3(self):
        self.assertEqual(commonChars(["","",""]), [])

    def test_common_chars_4(self):
        self.assertEqual(commonChars(["acabcddd","bcbdbcbd","baddbadb","cbdddcac","aacbcccd","ccccddda","cababaab","addcaccd"]), []) 

    def test_common_chars_5(self):
        self.assertEqual(commonChars([]), [])    

if __name__ == '__main__':
    unittest.main()