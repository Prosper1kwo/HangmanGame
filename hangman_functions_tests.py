'''
This module tests the functions defined in hangman_functions.py
'''

from hangman_functions import hangman_draw, encode, decode, guess_test, guess_store, answer_test, hint_conversion
from hangman_pics import hang_image
import unittest


class TestImageTools(unittest.TestCase):
    """
    Class for testing ImageTools.
    """
    def test_hangman_draw(self):
        self.assertEqual(hangman_draw(4), hang_image[4])
        self.assertEqual(hangman_draw(0), hang_image[0])
        self.assertEqual(hangman_draw(6), hang_image[6])
        self.assertEqual(hangman_draw(9), ValueError())
        self.assertEqual(hangman_draw(-2), ValueError())

    def test_answer_test(self):
        self.assertEqual(answer_test('p', 'prosper'), True)
        self.assertEqual(answer_test("P", "Prosper"), True)
        self.assertEqual(answer_test("TR", "trench"), True)
        self.assertEqual(answer_test("d", "Jowayne"), False)
        self.assertEqual(answer_test("t", "Joker"), False)

    def test_encode(self):
        self.assertEqual(encode("cat"), "***")
        self.assertEqual(encode("It is a dog"), "** ** * ***")
        self.assertEqual(encode("acapulco33"), "********33")
        self.assertEqual(encode("1234"), "1234")
        self.assertEqual(encode(1234), "1234")

    def test_decode(self):
        self.assertEqual(decode("SNAKE", "S", "*****"), "S****")
        self.assertEqual(decode("FOOD", "O", "F***"), "FOO*")
        self.assertEqual(decode("UPTOWN", "P", "******"), "*P****")
        self.assertEqual(decode("12315", "1", "*****"), "1**1*")
        self.assertEqual(decode("COMPUTER", "R", "CO******"), "CO*****R")

    def test_guess_store(self):
        self.assertEqual(guess_store("d", []), ["d"])
        self.assertEqual(guess_store("D", []), ["D"])
        self.assertEqual(guess_store("a", ["f", "C", "t", "a"]), ["f", "C", "t", "a"])
        self.assertEqual(guess_store("7", ["q", "c"]), ["q", "c", "7"])
        self.assertEqual(guess_store(9, [2, 3, "7", "b"]), [2, 3, "7", "b", 9])
        self.assertEqual(guess_store(9, [2, 9, "7", "b"]), [2, 9, "7", "b"])

    def test_guess_test(self):
        self.assertEqual(guess_test("d", []), False)
        self.assertEqual(guess_test("a", ["a", "C", "t", "q"]), True)
        self.assertEqual(guess_test("7", ["q", "c"]), False)
        self.assertEqual(guess_test(9, [2, 9, "7", "b"]), True)
        self.assertEqual(guess_test("Be", ["c", "B", "e"]), False)

    def test_hint_conversion(self):
        self.assertEqual(hint_conversion("a"), "an animal")
        self.assertEqual(hint_conversion("c"), "a country")
        self.assertEqual(hint_conversion("f"), "a fruit")

if __name__ == '__main__':
    unittest.main()