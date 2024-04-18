import unittest

import pygame

from main import User, Graphics
from main import ScoreTrack


class MyTestCase(unittest.TestCase):

    def test_name(self):
        x = ScoreTrack('Alice')
        self.assertIs(x.name, 'Alice')  # add assertion here

    def test_str_letters(self):
        x = ScoreTrack("Bob")
        self.assertEqual(x.__str__(), "Bob has no letters yet")

    def test_letters(self):
        x = ScoreTrack("Alice")
        self.assertEqual(x.letters, "")

    def test_checkCondition(self):
        x = ScoreTrack("Bob")
        self.assertNotEqual(x.checkCondition(), "HORSE")

    def test_add_letter(self):
        x = ScoreTrack("HOR")
        self.assertTrue(x.add_letter, "HORS")

    def test_print_info(self):
        user = User("Player1")
        self.assertEqual(user.print_info(), "Player1 spelled: ") # verify inital print info

        user.add_letter()
        self.assertEqual(user.print_info(), "Player1 spelled: H") # verify the print info

    def test_graphics_init(self):
        graphics = Graphics() # create Graphics instance

        # verify Pygame has been initialized
        self.assertTrue(pygame.get_init())

        # verify the game window has been created
        self.assertIsNotNone(graphics.windowSurfaceObj)

        # verify that the other attributes (colors, images) have been initialized
        self.assertIsNotNone(graphics.whiteColor)
        self.assertIsNotNone(graphics.greenColor)
        self.assertIsNotNone(graphics.blackColor)

        # verify the correct state is set initially
        self.assertEqual(graphics.state, 'entering_player1')
