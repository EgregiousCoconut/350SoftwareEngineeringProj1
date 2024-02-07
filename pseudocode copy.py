'''
The class that will hold our data  for our graphics, including: title screen,
basketball rim, and our basketball release slider (hold down a button and release
at certain point on the slider).
'''
class Graphics():
    pass

'''
This class will hold and display the images of the basketball backgrounds when
playing the game.
'''
class Frames(Graphics):
    pass

'''
This class will calculate the shot probability using random class, will store the
user input and use that to determine who shot the previous shot and how many shots
have been made (total score for user so far).
'''
class Horse():
    pass

'''
This class will keep track of the user score for both users, and will have a function
that adds a letter to the HORSE scoreboard based on if a shot was made for that user.
'''
class ScoreTrack():
    pass

'''
This class will build and hold the basic information needed to make each user in 
the game.
'''
class User(Horse, ScoreTrack):
    pass
