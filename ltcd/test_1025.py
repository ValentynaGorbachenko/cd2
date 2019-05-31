# test_1025.py

import unittest
from divisorGame_1025 import divisorGame

class repeatedNTimesTest(unittest.TestCase):

    def test_divisor_game_1(self):
        self.assertFalse(divisorGame(15))

    def test_divisor_game_2(self):
        self.assertFalse(divisorGame(3))

    def test_divisor_game_3(self):
        self.assertFalse(divisorGame(1))

    def test_divisor_game_4(self):
        self.assertTrue(divisorGame(2))

    def test_divisor_game_5(self):
        self.assertTrue(divisorGame(8))


    

if __name__ == '__main__':
    unittest.main()