import time

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
        self.width = 960
        self.height = 540
        pygame.init()
        pygame.font.init()
        self.windowSurfaceObj = pygame.display.set_mode((self.width, self.height), 1, 16)
        self.whiteColor = pygame.Color(255, 255, 255)
        self.greenColor = pygame.Color(0, 255, 0)
        self.blackColor = pygame.Color(0, 0, 0)
        pygame.draw.rect(self.windowSurfaceObj, self.whiteColor, Rect(self.width / 4, self.a, self.width / 2, 10))
        self.whiteColor = pygame.Color(255, 255, 255)
        self.a = 100
        self.b = 10
        pygame.draw.rect(self.windowSurfaceObj, self.greenColor, Rect(self.width / 4, self.a, self.width / 2, 10))
        pygame.display.update(pygame.Rect(0, 0, self.width, self.height))

    def draw_text(self, text, position, font_size=24, color = None):
        if color is None:
            color = self.whiteColor
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
            time.sleep(.03)
            self.a += self.b
            if self.a < 0:
                self.a = 0
                self.b *= -1
            elif self.a > self.height:
                self.a = self.height
                self.b *= -1
            pygame.draw.rect(self.windowSurfaceObj, self.blackColor, Rect(0, 0, self.width, self.height))
            pygame.draw.rect(self.windowSurfaceObj, self.greenColor, Rect(5, 50, self.width / 2, 200))
            pygame.draw.rect(self.windowSurfaceObj, self.whiteColor, Rect(5, self.a, self.width / 2, 10))
            pygame.display.update(pygame.Rect(0, 0, self.width, self.height))
            if self.button[0] != 0:
                pygame.draw.rect(self.windowSurfaceObj, self.blackColor, Rect(0, 0, self.width, self.height))
                pygame.draw.rect(self.windowSurfaceObj, self.greenColor, Rect(5, 50, self.width / 2, 200))
                pygame.draw.rect(self.windowSurfaceObj, self.whiteColor, Rect(5, self.a, self.width / 2, 10))
                pygame.display.update(pygame.Rect(0, 0, self.width, self.height))
                self.b = 0
                self.draw_text(f"{player1.name} spelled: {player1.score_tracker.letters}", (35, 490), 35)
                self.draw_text(f"{player2.name} spelled: {player2.score_tracker.letters}", (680, 490), 35)
                self.draw_text(winner_text, (425, 250), 35)
                if self.a > 50 and self.a < 250:
                    print("True")
                    return True
                else:
                    print("False")
                    return False

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



if __name__ == "__main__":
    print("Testing block is executing")

    player1 = users("Alice")
    player2 = users("Bob")

    shots_taken = [("Alice", True), ("Bob", False), ("Alice", False), ("Bob", True), ("Alice", False), ("Bob", False), ("Alice", False), ("Bob", False), ("Alice", False), ("Bob", False), ("Alice", True), ("Bob", False)]

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

    game_graphics.draw_text(f"{player1.name} spelled: {player1.score_tracker.letters}", (35, 490))
    game_graphics.draw_text(f"{player2.name} spelled: {player2.score_tracker.letters}", (680, 490))
    game_graphics.draw_text(winner_text, (425, 250))

    game_graphics = graphics()
    game_graphics.run()
