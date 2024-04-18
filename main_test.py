import unittest
from unittest.mock import MagicMock

import pygame

from main import User, Graphics
from main import ScoreTrack

class MyTestCase(unittest.TestCase):
    # Testing for the ScoreTrack class

    def test_name(self):
        x = ScoreTrack('Alice')
        self.assertIs(x.name, 'Alice')  # tests to see if name is returned correctly

    def test_checkCondition(self):
        score_track = ScoreTrack("Player1") # create instance
        self.assertFalse(score_track.checkCondition()) # verify returns false intially

        for _ in range(5):
            score_track.add_letter() # add letters until HORSE is spelled

        self.assertTrue(score_track.checkCondition()) # verify returns True after spelling HORSE

    def test_str_letters(self):
        x = ScoreTrack("Bob")
        self.assertEqual(x.__str__(), "Bob has no letters yet")

    def test_letters(self):
        x = ScoreTrack("Alice")
        self.assertEqual(x.letters, "")

    # testing for the User class

    def test_user_init(self):
        # Initialize a User instance with a name
        user_name = "TestUser"
        user = User(user_name)
        self.assertEqual(user.name, user_name)

        # Verify that the user's score tracker is initialized correctly
        # Check if score tracker is an instance of ScoreTrack
        self.assertIsInstance(user.score_tracker, ScoreTrack)

        # Verify that the score tracker's name is the same as the user's name
        self.assertEqual(user.score_tracker.name, user_name)

        # Verify that the user's score tracker starts with no letters
        self.assertEqual(user.score_tracker.letters, "")

    def test_add_letter(self):
        x = ScoreTrack("HOR")
        self.assertTrue(x.add_letter, "HORS")

    def test_print_info(self):
        user = User("Player1")
        self.assertEqual(user.print_info(), "Player1 spelled: ") # verify inital print info

        user.add_letter()
        self.assertEqual(user.print_info(), "Player1 spelled: H") # verify the print info

    # testing for the graphics class
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
