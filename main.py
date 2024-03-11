import time
import cv2
import numpy as np
import pygame, sys
import os
from pygame.locals import *

'''
The class that will hold our data  for our graphics, including: title screen,
basketball rim, and our basketball release slider (hold down a button and release
at certain point on the slider).
'''


class graphics():
    """had to adjust because it was running an infinite loop and I needed to test the scoring"""
    def __init__(self):
        self.width = 1260
        self.height = 540
        pygame.init()
        pygame.font.init()
        self.windowSurfaceObj = pygame.display.set_mode((self.width, self.height), 1, 16)
        self.whiteColor = pygame.Color(255, 255, 255)
        self.greenColor = pygame.Color(0, 255, 0)
        self.blackColor = pygame.Color(0, 0, 0)
        self.a = 100
        self.b = 10
        self.baskeballIMG = pygame.image.load('basketball.png').convert()
        self.backgroundIMG = pygame.image.load('background-w-rim.png').convert()
        self.backgroundIMGSmall = pygame.transform.scale(self.backgroundIMG, (960, 540))
        self.rimg = pygame.image.load('basketball-rim.png').convert()
        self.madeShot = cv2.VideoCapture("made.mp4")
        self.missShot = cv2.VideoCapture("miss.mp4")
        self.windowSurfaceObj.blit(self.backgroundIMGSmall, (0,0))

    def draw_text(self, text, position, font_size=24, color = None):
        if color is None:
            color = self.blackColor
        font = pygame.font.Font(None, font_size)  # Use the default font and specified size
        text_surface = font.render(text, True, color)  # Create a text surface
        self.windowSurfaceObj.blit(text_surface, position)  # Draw the text surface to the screen
        pygame.display.update()

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    running = False
                elif event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False

            self.button = pygame.mouse.get_pressed()
            time.sleep(.01)
            self.a += self.b
            if self.a < 0:
                self.a = 0
                self.b *= -1
            elif self.a > self.height:
                self.a = self.height
                self.b *= -1
            pygame.draw.rect(self.windowSurfaceObj, self.blackColor, Rect(960, 0, 300, self.height))
            pygame.draw.rect(self.windowSurfaceObj, self.greenColor, Rect(960, 50, 300, 75))
            pygame.draw.rect(self.windowSurfaceObj, self.whiteColor, Rect(960, self.a, 300, 10))
            pygame.display.update(pygame.Rect(0, 0, self.width, self.height))
            self.draw_text(f"{player1.name} spelled: {player1.score_tracker.letters}", (35, 490), 35)
            self.draw_text(f"{player2.name} spelled: {player2.score_tracker.letters}", (680, 490), 35)
            if self.button[0] != 0:
                pygame.draw.rect(self.windowSurfaceObj, self.blackColor, Rect(0, 0, self.width, self.height))
                self.windowSurfaceObj.blit(self.backgroundIMGSmall, (0, 0))
                pygame.draw.rect(self.windowSurfaceObj, self.greenColor, Rect(960, 50, 300, 75))
                pygame.draw.rect(self.windowSurfaceObj, self.whiteColor, Rect(960, self.a, 300, 10))
                pygame.display.update(pygame.Rect(0, 0, self.width, self.height))
                self.b = 0
                self.draw_text(f"{player1.name} spelled: {player1.score_tracker.letters}", (35, 490), 35)
                self.draw_text(f"{player2.name} spelled: {player2.score_tracker.letters}", (680, 490), 35)
                if self.a > 50 and self.a < 250:
                    print("True")
                    pygame.display.quit()
                    self.shot_animation(True)

                else:
                    print("False")
                    pygame.display.quit()
                    self.shot_animation(False)

        sys.exit()


    def shot_animation(self, made):
        cv2.namedWindow("Video Player", cv2.WINDOW_NORMAL)
        cv2.resizeWindow("Video Player", 270, 480)
        if made:

            # Read the entire file until it is completed
            while self.madeShot.isOpened():
                # Capture each frame
                ret, frame = self.madeShot.read()
                if ret:
                    cv2.imshow('Video Player', frame)
                    # Display the resulting frame
                    if cv2.waitKey(25) & 0xFF == ord('q'):
                        break
                else:
                    break
        else:
            # Read the entire file until it is completed
            while self.missShot.isOpened():
                # Capture each frame
                ret, frame = self.missShot.read()
                if ret:
                    cv2.imshow('Video Player', frame)
                    # Display the resulting frame
                    if cv2.waitKey(25) & 0xFF == ord('q'):
                        break
                else:
                    break
        self.b = 10
        self.madeShot.release()
        self.missShot.release()
        self.madeShot = cv2.VideoCapture("made.mp4")
        self.missShot = cv2.VideoCapture("miss.mp4")
        cv2.destroyAllWindows()
        self.windowSurfaceObj = pygame.display.set_mode((self.width, self.height), 1, 16)
        pygame.display.init()
        self.windowSurfaceObj.blit(self.backgroundIMGSmall, (0, 0))


'''
This class will hold and display the images of the basketball backgrounds when
playing the game.
'''

class scoreTrack():

    def __init__(self, name):
        self.__letters = ""  # Stores letters for horse
        self.__name = name  # used to return name of who wins

    def add_letter(self, letter):
        self.__letters += letter
        if self.checkCondition():
            return True
        return False

    def checkCondition(self):
        """check if player spelled horse"""
        return self.__letters.startswith("HORSE")

    @property
    def letters(self):
        return self.__letters

    @property
    def name(self):
        return self.__name

    def __str__(self):
        """returns current status of players HORSE letters"""
        if not self.__letters:
            return f"{self.__name} has no letters yet"
        return f"{self.__name} has the letters: {self.__letters}"

class users:
    def __init__(self, name):
        self.__name = name # name user inputs
        self.score_tracker = scoreTrack(name) # initializes score tracker

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if len(name) > 20:
            raise UsernameMaxException("Username is limited to 20 characters.")
        self.__name = name

    def print_info(self):
        return f"{str(self.name)} spelled: {self.score_tracker.letters}"

    def add_letter(self, letter):
        """Add letter to players score and check if lost"""
        lost = self.score_tracker.add_letter(letter)
        if lost:
            print(f"{self.__name} has spelled HORSE and lost the game!")
            return True
        return False


'''
This class will build and hold the basic information needed to make each user in 
the game.
'''


class UsernameMaxException(Exception):
    def __init__(self, message):
        super().__init__(message)


if __name__ == "__main__":
    print("Testing block is executing")

    player1 = users("Alice")
    player2 = users("Bob")

    shots_taken = []

    for player_name, shot_made in shots_taken:
        if player_name == player1.name:
            if not shot_made:
                letter = "HORSE"[len(player1.score_tracker.letters)]
                lost = player1.add_letter(letter)
                print(player1.print_info())
                if lost:
                    print(f"{player1.name} has lost the game.")
                    break

        elif player_name == player2.name:
            if not shot_made:
                letter = "HORSE"[len(player2.score_tracker.letters)]
                lost = player2.add_letter(letter)
                print(player2.print_info())
                if lost:
                    print(f"{player2.name} has lost the game.")
                    break

    game_graphics = graphics()
    game_graphics.run()

    p1_letters = len(player1.score_tracker.letters)
    p2_letters = len(player2.score_tracker.letters)

    print("\nFinal Scores:")
    print(player1.print_info())
    print(player2.print_info())

    winner_text = ""
    if p1_letters < p2_letters:
        print(f"{player1.name} wins!")
        winner_text = f"{player1.name} wins!"
    elif p2_letters < p1_letters:
        print(f"{player2.name} wins!")
        winner_text = f"{player2.name} wins!"
    else:
        print("It's a draw!")
        winner_text = "It's a Draw"

    game_graphics.draw_text(winner_text, (425, 250))
