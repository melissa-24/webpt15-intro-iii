# from room import Room
# # from player import player

# # Declare all the rooms
# room = {
#     'town-square': Room('town-square', 'Gathering for all who want to help the Gods'),
#     'ternion': Room('ternion', 'Where the big 3, Zeus, Poseidon, and Hades reside'),
#     'ancillary': Room('ancillary', 'Where the rest of the God reside'),
#     'eminence': Room('eminence', 'The residence of the Demi-Gods'),
#     'olympus': Room('olympus', 'Zeus domain'),
#     'ocean': Room('ocean','Poseidon domain'),
#     'abyss': Room('abyss','Hades domain'),
#     'camp': Room('camp', 'Training area'),
# }


# # Link rooms together

# room['olympus'].n_to = room['ternion']
# room['ternion'].s_to = room['olympus']
# room['ternion'].n_to = room['town-square']
# room['town-square'].s_to = room['ternion']
# room['ocean'].w_to = room['ternion']
# room['ternion'].e_to = room['ocean']
# room['ternion'].w_to = room['abyss']
# room['abyss'].e_to = room['ternion']
# room['ocean'].n_to = room['ancillary']
# room['ancillary'].s_to = room['ocean']
# room['ancillary'].w_to = room['town-square']
# room['town-square'].e_to = room['ancillary']
# room['town-square'].w_to = room['eminence']
# room['eminence'].e_to = room['town-square']
# room['abyss'].n_to = room['eminence']
# room['eminence'].s_to = room['abyss']
# room['eminence'].n_to = room['camp']
# room['camp'].s_to = room['eminence']



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

answer = input('Welcome to Mythical Assist Adventures.  Would you like to play? (yes/no) ')

if answer.lower().strip() == 'yes':
    name = input('What is your name kind helper of the Gods?').strip()
    print(f'\nWelcome {name}, lets get you to the camp')
    items = input('Before we tell you who needs help would you like to pick up some gear?')
    if items.lower().strip() == 'yes':
        item = input('Wonderful idea, we have swords and shields available which do you chose?')
        print(f'\nA {item} is a valiant choice {name}')


    else:
        print('Maybe you need some more time to prepare. Please come back later')


else:
    print('Maybe next time!')