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


def clear():
    if name =='nt':
        _ = system('cls')
    else:
        _ = system('clear')

player_name = str(input('Hello, what is your name?   '))
player = Player(player_name, room['camp'])
clear()

sword = Item('sword','A small, slim, barbed blade made of folded steel is held by a grip wrapped in uncommon, maroon bear leather.')
watch = Item('watch', 'A watch is a portable timepiece intended to be carried or worn by a person.')
coin = Item('coin', 'A small, flat, round piece of metal or plastic used primarily as a medium of exchange or legal tender.')
torch = Item('torch', 'A burning stick of resinous wood or twist of tow used to give light and usually carried in the hand.')
bottle = Item('bottle', 'Container that is used to hold water, liquids or other beverages for consumption.')

room['ternion'].inventory.append(sword)
room['camp'].inventory.append(watch)
room['eminence'].inventory.append(coin)
room['abyss'].inventory.append(torch)
room['ocean'].inventory.append(bottle)



playing = True
print(f'\nWelcome {player.name}\n')
time.sleep(1)
clear()
while playing:   
    print(player)
    selection = input(f'    What would you like to do {player.name}?  ')
    selection = selection.split()
    if len(selection) == 1:
        if selection[0] == 'n': 
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
        elif selection[0] == 'e':
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
        elif selection[0] == 's':
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
        elif selection[0] == 'w':
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
        elif selection[0] == 'i' or selection[0] == 'inventory':
            clear()
            if len(player.inventory) != 0:
                print(f'\n You are now holding:')
                for i, p in enumerate(player.inventory):
                    print(f'    {i + 1}: {p.name} - {p.description}\n')
                inpurt('Press enter to continue,')
        elif selection[0] == 'q':
            clear()
            print(f'\nThank you for playing, {player.name}!\n')
            playing = False
        else:
            clear()
            print(f'\n {player.name}! You must be confused, try again\n')
            time.sleep(1)
    else:
        if selection[0] == 'get' or selection[0] == 'take':
            if len(player.room.inventory) == 0:
                clear()
                print('Nothing here')
                time.sleep(1)
            else:
                for each in player.room.inventory:
                    if each.name == selection[1]:
                        player.add_item(each)
                        player.room.remove_item(each)
                        clear()
                        each.on_take()
                    else:
                        clear()
                        print(f'Unable to find {selection[1]}')
                        time.sleep(1)
        elif selection[0] == 'drop':
            if len(player.inventory) == 0:
                clear()
                print('You aren\'t holding anything.')
                time.sleep(1)
            else:
                for each in player.inventory:
                    if each.name == selection[1]:
                        player.remove_item(each)
                        player.room.add_item(each)
                        clear()
                        each.on_drop()
                    else:
                        clear()
                        print(f'You don\'t have {selection[1]}')
                        time.sleep(1)
        else:
            clear()
            print(f'\n {player.name}! Please enter a valid action.\n')
            time.sleep(1)
    
    time.sleep(.5)
    clear()