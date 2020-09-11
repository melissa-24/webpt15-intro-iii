# from room import Room
# from player import player

# Declare all the rooms




# Link rooms together



#
# Main
#

# Make a new player object that is currently in the 'outside' room.

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

def show_welcome_message():
    welcome_message = "Welcome one and all to a game of Blackout Uno!"
    print(welcome_message)

def quit_game():
    quit_message = "Thank you for not setting things on fire, please play again!"
    if cmd == "q":
        print(quit_message)

welcome_message = "Welcome one and all to a game of Blackout Uno!"
quit_message = "Thank you for not setting things on fire, please play again!"
win_message = "You Won!"
loss_message = "Sorry, but you lost this time."

show_welcome_message()