import unittest
from main import users
from main import scoreTrack


class MyTestCase(unittest.TestCase):

    # tests to see if string is returned correctly
    def test_print_info(self):
        x = users("Alice")
        self.assertEqual(x.print_info(), "Alice spelled: ")

    # tests for scoreTrack class
    # tests to see if name is returned correctly
    def test_name(self):
        x = scoreTrack('Alice')
        self.assertIs(x.name, 'Alice')  # add assertion here

    def test_str_letters(self):
        x = scoreTrack("Bob")
        self.assertEqual(x.__str__(), "Bob has no letters yet")

    def test_letters(self):
        x = scoreTrack("Alice")
        self.assertEqual(x.letters, "")

    def test_checkCondition(self):
        x = scoreTrack("Bob")
        self.assertNotEqual(x.checkCondition(), "HORSE")

    def test_add_letter(self):
        x = scoreTrack("HOR")
        self.assertTrue(x.add_letter, "HORS")
