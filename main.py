import pygame, sys
import os
from pygame.locals import *

'''
The class that will hold our data  for our graphics, including: title screen,
basketball rim, and our basketball release slider (hold down a button and release
at certain point on the slider).
'''


class graphics():

    width = 960
    height = 540

    pygame.init()
    windowSurfaceObj = pygame.display.set_mode((width, height), 1, 16)
    greenColor = pygame.Color(0, 255, 0)
    blackColor = pygame.Color(0, 0, 0)

    x = 100
    y = 100
    pygame.draw.rect(windowSurfaceObj, greenColor, Rect(width / 3, 10, width / 2, 10))
    pygame.display.update(pygame.Rect(0, 0, width, height))

    s = 0
    a = y - 5
    b = 2
    while s == 0:
        button = pygame.mouse.get_pressed()
        a -= b
        if a <= 0:
            a = 5
            b *= -1
        elif a > height - 5:
            a = height - 5
            b *= -1
        pygame.draw.rect(windowSurfaceObj, blackColor, Rect(0, 0, width, height))
        pygame.draw.rect(windowSurfaceObj, greenColor, Rect(width / 3, a, width / 2, 10))
        pygame.display.update(pygame.Rect(0, 0, width, height))
        if button[0] != 0:
            pygame.draw.rect(windowSurfaceObj, blackColor, Rect(0, 0, width, height))
            pygame.draw.rect(windowSurfaceObj, greenColor, Rect(width / 3, a, width / 2, 10))
            pygame.display.update(pygame.Rect(0, 0, width, height))
            b = 0

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()


'''
This class will hold and display the images of the basketball backgrounds when
playing the game.
'''


class frames(graphics):
    pass


'''
This class will calculate the shot probability using random class, will store the
user input and use that to determine who shot the previous shot and how many shots
have been made (total score for user so far).
'''


class horse():
    pass



'''
This class will keep track of the user score for both users, and will have a function
that adds a letter to the HORSE scoreboard based on if a shot was made for that user.
'''


class scoreTrack():

    def __init__(self, name):
        self.__score = 0  # score per player
        self.__name = name  # used to return name of who wins

    @property
    def score(self):
        return self.__score

    @score.setter
    def score(self, madeCondition):
        if madeCondition:
            self.__score += 1  # checks if condition passed is true, if so, increment by one
            if self.checkCondition() != False:
                pass  # call game condition to let it know someone has passed the point threshold and has won, along with the name

    def checkCondition(self):
        if self.__score > 4:
            return self.__name  # return name instead of True, so we can know who won
        else:
            return False

    @property
    def name(self):
        return self.__name


'''
This class will build and hold the basic information needed to make each user in 
the game.
'''


class UsernameMaxException(Exception):
    def __init__(self, message):
        super().__init__(message)

class user(horse, scoreTrack):
    def __init__(self, name):
        self.__name = name  # name user inputs

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if len(name) > 20:
            raise UsernameMaxException("Username is limited to 20 characters.")
        self.__name = name

    def print_info(self):
        return "User: " + str(self.name)
