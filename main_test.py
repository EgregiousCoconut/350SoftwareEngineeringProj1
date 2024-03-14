import unittest
from main import users
from main import scoreTrack


class MyTestCase(unittest.TestCase):

    # tests to see if name is returned correctly
    def test_init_name(self):
        x = users('Alice')
        self.assertIs(x.name, 'Alice')  # add assertion here

    # tests to see if string is returned correctly
    def test_print_info(self):
        x = scoreTrack("Alice")
        self.__letters = "HORSE"
        self.assertEqual(scoreTrack(self.print_info(x)), "Alice spelled HORSE")

    # tests for scoreTrack class
    def test_str_not_letters(self):
        self.__letters = None
        self.__name = "Bob"
        self.assertIs(self.__str__(), "Bob has no letters yet")

    def test_str_letters(self):
        self.__letters = "HOR"
        self.__name = ("Alice")
        self.assertEqual(self.__str__(), "Alice has the letters: HOR")

    def test_letters(self):
        x = "HORS"
        self.assertIs(scoreTrack.letters, x)

    def test_checkCondition1(self):
        letters = "HOR"
        self.assertNotEqual(scoreTrack.checkCondition(letters), "HORSE")

    def test_checkCondition2(self):
        letters = "HORSE"
        self.assertEqual(scoreTrack.checkCondition(letters), "HORSE")

    def test_add_letter1(self):
        x = "HOR"
        self.assertFalse(x, scoreTrack.add_letter)

    def test_add_letter2(self):
        x = "HORSE"
        self.assertTrue(x, scoreTrack.add_letter)
