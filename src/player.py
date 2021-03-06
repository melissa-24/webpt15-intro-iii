default = 'The way is blocked.'
class Player:
    def __init__(self, name, room, inventory=[]):
        self.name = name
        self.room = room
        self.inventory = inventory

    def add_item(self, new_item):
        self.inventory.append(new_item)

    def remove_item(self, old_item):
        self.inventory.remove(old_item)

    def __str__(self):
        ret = f"You are currently in {self.room.name}"
        ret += '\n-------------'
        ret += f'\n{self.room.description}'
        ret += '\n-------------'
        if len(self.room.inventory) != 0:
            ret += f'\nYou find the following in the room:'
            for i, p in enumerate(self.room.inventory):
                ret += f'\n    {i + 1}: {p.name} - {p.description}'
        else:
            ret += '\nYou don\'t see anything of value in the room.'
        ret += '\n-------------'
        ret += f'\nActions'
        if self.room.n_to != default:
            ret += f'\n    n: {self.room.n_to.name}'
        if self.room.e_to != default:    
            ret += f'\n    e: {self.room.e_to.name}'
        if self.room.s_to != default:
            ret += f'\n    s: {self.room.s_to.name}'
        if self.room.w_to != default:
            ret += f'\n    w: {self.room.w_to.name}'
        ret += '\n    i: inventory'
        ret += '\n    q: Quit'
        ret += '\n'
    
        return ret