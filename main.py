import time
import cv2
import pygame
import sys
from pygame.locals import *
import wx


class Graphics:
    """
    Handles the game graphics and user interface.
    """

    def __init__(self):
        """Initialize graphics settings and load resources."""

        # Initialize the wx application to get display size
        app = wx.App(False)
        self.width, self.height = wx.GetDisplaySize()

        # Initialize pygame
        pygame.init()
        pygame.font.init()

        # Set up game window
        self.windowSurfaceObj = pygame.display.set_mode((self.width, self.height), 1, 16)

        # Define colors
        self.whiteColor = pygame.Color(255, 255, 255)
        self.greenColor = pygame.Color(0, 255, 0)
        self.blackColor = pygame.Color(0, 0, 0)

        # Initialize slider variables
        self.a = 100
        self.b = 20

        # Load images
        self.basketballIMG = pygame.image.load('basketball.png').convert()
        self.backgroundIMG = pygame.image.load('background-w-rim.png').convert()
        self.backgroundIMGSmall = pygame.transform.scale(self.backgroundIMG, (int(self.width * .8), self.height))
        self.rimg = pygame.image.load('basketball-rim.png').convert()

        # Load videos
        self.madeShot = cv2.VideoCapture("made.mp4")
        self.missShot = cv2.VideoCapture("miss.mp4")

        # Set background
        self.windowSurfaceObj.blit(self.backgroundIMGSmall, (0, 0))

        # Create user objects
        self.player = 1
        self.user1 = User(self.create_user())
        self.player = 2
        self.user2 = User(self.create_user())

        # Set current user
        self.current_user = self.user1
        self.previousShot = 0

    def draw_text(self, text, position, font_size=24, color=None):
        """
        Draw text on the game screen.

        Args:
            text (str): Text to display.
            position (tuple): Position (x, y) to display the text.
            font_size (int, optional): Font size. Defaults to 24.
            color (tuple, optional): Text color. Defaults to None (black).
        """

        if color is None:
            color = self.blackColor
        font = pygame.font.Font(None, font_size)
        text_surface = font.render(text, True, color)
        self.windowSurfaceObj.blit(text_surface, position)
        pygame.display.update()

    def create_user(self):
        """
        Create a user by getting input for the user's name.

        Returns:
            str: User's name.
        """

        self.text = ""
        text = ""
        running = True

        while running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    running = False
                elif event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False
                    elif event.key == K_BACKSPACE:
                        self.text = self.text[:-1]
                    elif event.unicode:
                        text += event.unicode

            # Display name input prompt
            self.windowSurfaceObj.fill(self.whiteColor)
            self.draw_text("What is your name, player " + str(self.player) + "?", (600, 400), 50, self.blackColor)

            # Capture keyboard input
            if event.type == KEYDOWN:
                if event.unicode:
                    text += self.text

            # Check if Enter key is pressed to submit the name
            if event.type == KEYDOWN and event.key == K_RETURN:
                return self.text

    def run(self):
        """
        Main game loop.
        """

        app = wx.App(False)
        self.width, self.height = wx.GetDisplaySize()

        # Initialize pygame again
        pygame.init()
        pygame.font.init()

        # Set up game window again
        self.windowSurfaceObj = pygame.display.set_mode((self.width, self.height), 1, 16)

        # Set up colors
        self.whiteColor = pygame.Color(255, 255, 255)
        self.greenColor = pygame.Color(0, 255, 0)
        self.blackColor = pygame.Color(0, 0, 0)

        # Initialize slider variables
        self.a = 100
        self.b = 20

        # Load resources
        self.basketballIMG = pygame.image.load('basketball.png').convert()
        self.backgroundIMG = pygame.image.load('background-w-rim.png').convert()
        self.backgroundIMGSmall = pygame.transform.scale(self.backgroundIMG, (int(self.width * .8), self.height))
        self.rimg = pygame.image.load('basketball-rim.png').convert()
        self.madeShot = cv2.VideoCapture("made.mp4")
        self.missShot = cv2.VideoCapture("miss.mp4")

        # Set background
        self.windowSurfaceObj.blit(self.backgroundIMGSmall, (0, 0))

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    running = False
                elif event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False

            # Update slider position
            self.button = pygame.mouse.get_pressed()
            time.sleep(.01)
            self.a += self.b

            # Reverse direction if slider hits top or bottom
            if self.a < 0:
                self.a = 0
                self.b *= -1
            elif self.a > self.height:
                self.a = self.height
                self.b *= -1

            # Draw slider and update screen
            pygame.draw.rect(self.windowSurfaceObj, self.blackColor,
                             Rect(self.width * .8, 0, self.width * .2, self.height))
            pygame.draw.rect(self.windowSurfaceObj, self.greenColor, Rect(self.width * .8, 50, self.width * .2, 75))
            pygame.draw.rect(self.windowSurfaceObj, self.whiteColor, Rect(self.width * .8, self.a, self.width * .2, 10))
            pygame.display.update(pygame.Rect(0, 0, self.width, self.height))

            # Display scores
            self.draw_text(f"{player1.name} spelled: {player1.score_tracker.letters}", (35, 490), 35)
            self.draw_text(f"{player2.name} spelled: {player2.score_tracker.letters}", (1000, 490), 35)

            # Check for mouse click
            if self.button[0] != 0:
                pygame.draw.rect(self.windowSurfaceObj, self.blackColor, Rect(0, 0, self.width, self.height))
                self.windowSurfaceObj.blit(self.backgroundIMGSmall, (0, 0))
                pygame.draw.rect(self.windowSurfaceObj, self.greenColor, Rect(self.width * .8, 50, self.width * .2, 75))
                pygame.draw.rect(self.windowSurfaceObj, self.whiteColor,
                                 Rect(self.width * .8, self.a, self.width * .2, 10))
                pygame.display.update(pygame.Rect(0, 0, self.width, self.height))
                self.b = 0
                self.draw_text(f"{player1.name} spelled: {player1.score_tracker.letters}", (35, 490), 35)
                self.draw_text(f"{player2.name} spelled: {player2.score_tracker.letters}", (1000, 490), 35)

                # Check if shot is within scoring parameters
                if 50 < self.a < 125:
                    pygame.display.quit()
                    self.shot_animation(True)
                else:
                    pygame.display.quit()
                    self.shot_animation(False)

        sys.exit()

    def shot_animation(self, made):
        """
        Play shot animation based on the shot result.

        Args:
            made (bool): True if shot was made, False if missed.
        """

        cv2.namedWindow("Video Player", cv2.WND_PROP_FULLSCREEN)
        cv2.setWindowProperty("Video Player", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

        if made:
            while self.madeShot.isOpened():
                ret, frame = self.madeShot.read()
                if ret:
                    cv2.imshow('Video Player', frame)
                    if cv2.waitKey(25) & 0xFF == ord('q'):
                        if self.current_user.add_letter():
                            if self.previousShot == 0:
                                self.previousShot = 1
                            else:
                                self.previousShot = 0
                            sys.exit()
                        break
                else:
                    if self.current_user.add_letter():
                        if self.previousShot == 0:
                            self.previousShot = 1
                        else:
                            self.previousShot = 0
                        sys.exit()
                    break
        else:
            while self.missShot.isOpened():
                ret, frame = self.missShot.read()
                if ret:
                    cv2.imshow('Video Player', frame)
                    if cv2.waitKey(25) & 0xFF == ord('q'):
                        if self.previousShot == 1:
                            if self.current_user.add_letter():
                                sys.exit()
                        break
                else:
                    if self.previousShot == 1:
                        if self.current_user.add_letter():
                            sys.exit()
                    break

        # Reset slider velocity
        self.b = 20

        # Switch current user
        if self.current_user == self.user1:
            self.current_user = self.user2
        else:
            self.current_user = self.user1

        # Release videos and reset
        self.madeShot.release()
        self.missShot.release()
        self.madeShot = cv2.VideoCapture("made.mp4")
        self.missShot = cv2.VideoCapture("miss.mp4")
        cv2.destroyAllWindows()
        self.windowSurfaceObj = pygame.display.set_mode((self.width, self.height), 1, 16)
        pygame.display.init()
        self.windowSurfaceObj.blit(self.backgroundIMGSmall, (0, 0))


class ScoreTrack:
    """
    Track the score of a player.
    """

    def __init__(self, name):
        """
        Initialize the score tracker.

        Args:
            name (str): Player's name.
        """

        self.__letters = ""
        self.__name = name

    def add_letter(self):
        """
        Add a letter to the player's score.

        Returns:
            bool: True if player loses, False otherwise.
        """

        self.__letters += "HORSE"[len(self.__letters)]
        if self.checkCondition():
            return True
        return False

    def checkCondition(self):
        """
        Check if the player has spelled 'HORSE'.

        Returns:
            bool: True if player spelled 'HORSE', False otherwise.
        """

        return self.__letters == "HORSE"

    @property
    def letters(self):
        """Return the current letters."""
        return self.__letters

    @property
    def name(self):
        """Return the player's name."""
        return self.__name

    def __str__(self):
        """Return the score as a string."""
        if not self.__letters:
            return f"{self.__name} has no letters yet"
        return f"{self.__name} has the letters: {self.__letters}"


class User:
    """
    Represent a user in the game.
    """

    def __init__(self, name):
        """
        Initialize the user.

        Args:
            name (str): User's name.
        """

        self.__name = name
        self.score_tracker = ScoreTrack(name)

    @property
    def name(self):
        """Return the user's name."""
        return self.__name

    @name.setter
    def name(self, name):
        """
        Set the user's name.

        Args:
            name (str): New name for the user.
        """

        if len(name) > 20:
            raise UsernameMaxException("Username is limited to 20 characters.")
        self.__name = name

    def print_info(self):
        """Return user's name and score."""
        return f"{str(self.name)} spelled: {self.score_tracker.letters}"

    def add_letter(self):
        """
        Add a letter to the user's score and check if the user lost.

        Returns:
            bool: True if user loses, False otherwise.
        """

        lost = self.score_tracker.add_letter()
        if lost:
            print(f"{self.__name} has spelled HORSE and won the game!")
            return True
        return False


class UsernameMaxException(Exception):
    """Exception raised for usernames that are too long."""

    def __init__(self, message):
        """
        Initialize the exception.

        Args:
            message (str): Error message.
        """

        super().__init__(message)


if __name__ == "__main__":
    print("Testing block is executing")

    # Create user objects
    player1 = User("Player 1")
    player2 = User("Player 2")

    shots_taken = []
    game_graphics = Graphics()
    game_graphics.run()

    # Get final scores
    p1_letters = len(player1.score_tracker.letters)
    p2_letters = len(player2.score_tracker.letters)

    print("\nFinal Scores:")
    print(player1.print_info())
    print(player2.print_info())

    # Determine winner
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

    # Display winner text (unused in this version)
    game_graphics.draw_text(winner_text, (425, 250))
