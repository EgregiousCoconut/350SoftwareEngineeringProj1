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
    pygame.draw.rect(windowSurfaceObj, greenColor, Rect(x, 5, 10, height - 10))
    pygame.display.update(pygame.Rect(0, 0, width, height))

    s = 0
    while s == 0:
        button = pygame.mouse.get_pressed()
        if button[0] != 0:
            pos = pygame.mouse.get_pos()
            x = pos[0]
            y = pos[1]
            a = x - 5
            if a < 0:
                a = 0
            pygame.draw.rect(windowSurfaceObj, blackColor, Rect(0, 0, width, height))
            pygame.draw.rect(windowSurfaceObj, greenColor, Rect(a, 5, 10, height - 10))
            pygame.display.update(pygame.Rect(0, 0, width, height))

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
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


class user(horse, scoreTrack):
    pass
