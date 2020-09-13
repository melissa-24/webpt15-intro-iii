from room import Room
from player import Player
import time
from item import Item
from os import system, name

room = {
    'ternion': Room('ternion', 'Where the big 3, Zeus, Poseidon, and Hades reside', []),
    'ancillary': Room('ancillary', 'Where the rest of the God reside', []),
    'eminence': Room('eminence', 'The residence of the Demi-Gods', []),
    'olympus': Room('olympus', 'Zeus domain', []),
    'ocean': Room('ocean','Poseidon domain', []),
    'abyss': Room('abyss','Hades domain', []),
    'camp': Room('camp', 'Training area as well as the main gathering area', []),
}

# Link rooms together

room['olympus'].n_to = room['camp']
room['camp'].s_to = room['olympus']
room['ocean'].w_to = room['olympus']
room['olympus'].e_to = room['ocean']
room['olympus'].w_to = room['abyss']
room['abyss'].e_to = room['olympus']
room['ocean'].n_to = room['ternion']
room['ternion'].s_to = room['ocean']
room['ternion'].w_to = room['camp']
room['camp'].e_to = room['ternion']
room['abyss'].n_to = room['ancillary']
room['ancillary'].s_to = room['abyss']
room['camp'].w_to = room['ancillary']
room['ancillary'].e_to = room['camp']
room['eminence'].s_to = room['camp']
room['camp'].n_to = room['eminence']


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


# answer = input('Welcome to Mythical Assist Adventures.  Would you like to play? (yes/no) ')

# if answer.lower().strip() == 'yes':
#     name = input('What is your name kind helper of the Gods?').strip()
#     player = name('{name}', camp, [])
#     print(f'\nWelcome {name}, lets get you to the {camp}')
#     items = input('Before we tell you who needs help would you like to pick up some gear?')
#     if items.lower().strip() == 'yes':
#         item = input('Wonderful idea, we have swords and shields available which do you chose?')
#         print(f'\nA {item} is a valiant choice {name}')


#     else:
#         print('Maybe you need some more time to prepare. Please come back later')


# else:
#     print('Maybe next time!')

def clear():
    if name =='nt':
        _ = system('cls')
    else:
        _ = system('clear')

player_name = str(input('Hello, what is your name?   '))
player = Player(player_name, room['camp'])
clear()


playing = True
print(f'\nWelcome {player.name}\n')
time.sleep(1)
clear()
while playing:   
    print(player)
    selection = input('    Please select a direction to move.  ')
    if selection == 'n': 
        if player.room.n_to != 'The way is blocked.':
            player.room = player.room.n_to
            clear()
            print(f'You move into the {player.room.name}')
            time.sleep(1)
        else:
            clear()
            print(player.room.n_to)
            time.sleep(1)
            clear()
            print('Try a different direction.')
            time.sleep(1)
    elif selection == 'e':
        if player.room.e_to != 'The way is blocked.':
            player.room = player.room.e_to
            clear()
            print(f'You move into the {player.room.name}')
            time.sleep(1)
        else:
            clear()
            print(player.room.e_to)
            time.sleep(1)
            clear()
            print('Try a different direction.')
            time.sleep(1)
    elif selection == 's':
        if player.room.s_to != 'The way is blocked.':
            player.room = player.room.s_to
            clear()
            print(f'You move into the {player.room.name}')
            time.sleep(1)
        else:
            clear()
            print(player.room.s_to)
            time.sleep(1)
            clear()
            print('Try a different direction.')
            time.sleep(1)
    elif selection == 'w':
        if player.room.w_to != 'The way is blocked.':
            player.room = player.room.w_to
            clear()
            print(f'You move into the {player.room.name}')
            time.sleep(1)
        else:
            clear()
            print(player.room.w_to)
            time.sleep(1)
            clear()
            print('Try a different direction.')
            time.sleep(1)
    elif selection == 'q':
        clear()
        print(f'\nThanks for playing, {player.name}!\n')
        playing = False
    else:
        clear()
        print(f'\n {player.name}! You must be confused, try again\n')
        time.sleep(1)
    
    time.sleep(.5)
    clear()