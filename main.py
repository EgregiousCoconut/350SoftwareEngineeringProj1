import time
import cv2
import pygame
import sys
from pygame.locals import *
import wx

'''
The class that will hold our data  for our graphics, including: title screen,
basketball rim, and our basketball release slider (hold down a button and release
at certain point on the slider).
'''


class graphics:
    """had to adjust because it was running an infinite loop and I needed to test the scoring"""

    def __init__(self, user1, user2):
        app = wx.App(False)
        self.width, self.height = wx.GetDisplaySize()
        pygame.init()  # initialize game
        pygame.font.init()
        self.windowSurfaceObj = pygame.display.set_mode((self.width, self.height), 1, 16)  # initialize game window
        self.whiteColor = pygame.Color(255, 255, 255)  # initialize colors
        self.greenColor = pygame.Color(0, 255, 0)
        self.blackColor = pygame.Color(0, 0, 0)
        self.a = 100  # variable for storing height of the slider
        self.b = 20  # variable for storing velocity of the slider
        self.basketballIMG = pygame.image.load('basketball.png').convert()  # initialize images
        self.backgroundIMG = pygame.image.load('background-w-rim.png').convert()
        self.backgroundIMGSmall = pygame.transform.scale(self.backgroundIMG, (self.width * .8, self.height))  # scale loaded image
        self.rimg = pygame.image.load('basketball-rim.png').convert()
        self.madeShot = cv2.VideoCapture("made.mp4")  # initialize videos
        self.missShot = cv2.VideoCapture("miss.mp4")
        self.windowSurfaceObj.blit(self.backgroundIMGSmall, (0, 0))  # set background
        self.user1 = user1  # initialize users passed into it
        self.user2 = user2
        self.current_user = self.user1  # set current user
        self.previousShot = 0

    def draw_text(self, text, position, font_size=24, color=None):
        if color is None:
            color = self.blackColor
        font = pygame.font.Font(None, font_size)  # Use the default font and specified size
        text_surface = font.render(text, True, color)  # Create a text surface
        self.windowSurfaceObj.blit(text_surface, position)  # Draw the text surface to the screen
        pygame.display.update()

    def run(self):
        running = True  # loop to run forever until conditions are met
        while running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    running = False
                elif event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False

            self.button = pygame.mouse.get_pressed()
            time.sleep(
                .01)  # slow the rate of the slider to make it uniform, otherwise speed varies on code execution speed
            self.a += self.b  # add velocity to height of slider
            if self.a < 0:  # conditions if slider is at top or bottom, reverse velocity
                self.a = 0
                self.b *= -1
            elif self.a > self.height:
                self.a = self.height
                self.b *= -1
            pygame.draw.rect(self.windowSurfaceObj, self.blackColor, Rect(self.width * .8, 0, self.width * .2, self.height))  # update slider graphics
            pygame.draw.rect(self.windowSurfaceObj, self.greenColor, Rect(self.width * .8, 50, self.width * .2, 75))
            pygame.draw.rect(self.windowSurfaceObj, self.whiteColor, Rect(self.width * .8, self.a, self.width * .2, 10))
            pygame.display.update(pygame.Rect(0, 0, self.width, self.height))
            self.draw_text(f"{player1.name} spelled: {player1.score_tracker.letters}", (35, 490),35)  # update scoring text
            self.draw_text(f"{player2.name} spelled: {player2.score_tracker.letters}", (680, 490), 35)
            if self.button[0] != 0:  # if mouse click is detected, run this
                pygame.draw.rect(self.windowSurfaceObj, self.blackColor, Rect(0, 0, self.width, self.height))  # clear background
                self.windowSurfaceObj.blit(self.backgroundIMGSmall, (0, 0))
                pygame.draw.rect(self.windowSurfaceObj, self.greenColor, Rect(self.width * .8, 50, self.width * .2, 75))
                pygame.draw.rect(self.windowSurfaceObj, self.whiteColor, Rect(self.width * .8, self.a, self.width * .2, 10))
                pygame.display.update(pygame.Rect(0, 0, self.width, self.height))
                self.b = 0  # set velocity to 0
                self.draw_text(f"{player1.name} spelled: {player1.score_tracker.letters}", (35, 490), 35)
                self.draw_text(f"{player2.name} spelled: {player2.score_tracker.letters}", (680, 490), 35)
                if 50 < self.a < 125:  # condition if slider is within scoring parameters
                    print("True")  # debug
                    pygame.display.quit()  # close pygame window
                    self.shot_animation(True)
                else:
                    print("False")
                    pygame.display.quit()
                    self.shot_animation(False)

        sys.exit()  # when loop ends, close windows associated

    def shot_animation(self, made):
        cv2.namedWindow("Video Player", cv2.WND_PROP_FULLSCREEN)  # initialize video window
        cv2.setWindowProperty("Video Player", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
        if made:  # conditional if shot was made
            # Read the entire file until it is completed
            while self.madeShot.isOpened():
                # Capture each frame
                ret, frame = self.madeShot.read()
                if ret:
                    cv2.imshow('Video Player', frame)
                    # Display the resulting frame
                    if cv2.waitKey(25) & 0xFF == ord('q'):
                        if self.current_user.add_letter():  # add letter to other user
                            if self.previousShot == 0:
                                self.previousShot = 1
                            else:
                                self.previousShot = 0
                            sys.exit()
                        break
                else:
                    if self.current_user.add_letter():  # add letter to other user
                        if self.previousShot == 0:
                            self.previousShot = 1
                        else:
                            self.previousShot = 0
                        sys.exit()
                    break
        else:
            # Read the entire file until it is completed
            while self.missShot.isOpened():  # same stuff, except with miss video
                # Capture each frame
                ret, frame = self.missShot.read()
                if ret:
                    cv2.imshow('Video Player', frame)
                    # Display the resulting frame
                    if cv2.waitKey(25) & 0xFF == ord('q'):
                        if self.previousShot == 1:
                            if self.current_user.add_letter():  # add letter to other user
                                sys.exit()
                        break
                else:
                    if self.previousShot == 1:
                        if self.current_user.add_letter():  # add letter to other user
                            sys.exit()
                    break
        self.b = 20
        if self.current_user == self.user1:
            self.current_user = self.user2
        else:
            self.current_user = self.user1
        self.madeShot.release()  # release videos, had to do this because of errors
        self.missShot.release()
        self.madeShot = cv2.VideoCapture("made.mp4")  # reinitialize videos
        self.missShot = cv2.VideoCapture("miss.mp4")
        cv2.destroyAllWindows()  # destroy video windows
        self.windowSurfaceObj = pygame.display.set_mode((self.width, self.height), 1, 16)  # reinitialize videos
        pygame.display.init()
        self.windowSurfaceObj.blit(self.backgroundIMGSmall, (0, 0))


'''
This class will hold and display the images of the basketball backgrounds when
playing the game.
'''


class scoreTrack:

    def __init__(self, name):
        self.__letters = ""  # Stores letters for horse
        self.__name = name  # used to return name of who wins

    def add_letter(self):
        self.__letters += "HORSE"[len(self.__letters)]
        if self.checkCondition():
            return True
        return False

    def checkCondition(self):
        """check if player spelled horse"""
        return self.__letters == "HORSE"

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
        self.__name = name  # name user inputs
        self.score_tracker = scoreTrack(name)  # initializes score tracker

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if len(name) > 20:
            raise UsernameMaxException(
                "Username is limited to 20 characters.")  # keeping names limited to 20 characters
        self.__name = name

    def print_info(self):
        return f"{str(self.name)} spelled: {self.score_tracker.letters}"

    def add_letter(self):
        """Add letter to players score and check if lost"""
        lost = self.score_tracker.add_letter()
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
        super().__init__(message)  # custom exception for usernames being too long


if __name__ == "__main__":
    print("Testing block is executing")  # debug

    player1 = users(str(input("Enter Player 1's name: ")))  # predetermined users for first iteration
    player2 = users(str(input("Enter Player 2's name: ")))

    shots_taken = []
    game_graphics = graphics(player1, player2)  # initialize graphics with users
    game_graphics.run()  # run main graphics

    p1_letters = len(player1.score_tracker.letters)
    p2_letters = len(player2.score_tracker.letters)

    print("\nFinal Scores:")  # print final scores
    print(player1.print_info())
    print(player2.print_info())

    winner_text = ""
    if p1_letters < p2_letters:  # conditional to print who wins
        print(f"{player1.name} wins!")
        winner_text = f"{player1.name} wins!"
    elif p2_letters < p1_letters:
        print(f"{player2.name} wins!")
        winner_text = f"{player2.name} wins!"
    else:
        print("It's a draw!")
        winner_text = "It's a Draw"

    game_graphics.draw_text(winner_text, (425, 250))  # unused, implementation for next iteration
