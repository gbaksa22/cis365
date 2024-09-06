"""
CIS 365 - Assignment 1

Date - 8/30/2024

This program was created by Gabe Baksa

Used CIS 163 Project 2 from Winter 2023 as reference
"""
def abreviation(letter: str) -> str:
        if letter.capitalize() == "N":
            return "North"
        elif letter.capitalize() == "E":
            return "East"
        elif letter.capitalize() == "S":
            return "South"
        elif letter.capitalize() == "W":
            return "West"
        else:
            return letter

class Item:
    def __init__(self, name: str, description:str) -> None:
        self.name = name
        self.description = description

        if self.name == '':
            raise ValueError('Name variable is blank.')
        if self.description == '':
            raise ValueError('Description variable is blank.')

    def __str__(self) -> str:
        string = self.name + ' - ' + self.description
        return string

    def get_name(self) -> str:
        return self.name

    def get_description(self) -> str:
        return self.description

    def set_name(self, name) -> None:
        self.name = name

    def set_description(self, description) -> None:
        self.description = description

class Location:
    def __init__(self, name: str, description: str) -> None:
        self.name = name
        self.description = description
        self.neighbors = {}
        self.items = []
        self.visited = False

    def get_name(self) -> str:
        return self.name

    def get_neighbors(self) -> dict:
        return self.neighbors

    def add_neighbor(self, direction: str, location: 'Location') -> None:
        """
        checks to make sure that the location
        doesn't already exist and that you've
        actually typed something in.  If so,
        adds location to neighbors list

        direction - is the direction you want to add
        location - is the location you want to add
        """
        if direction == '':
            raise ValueError('No direction given.')
        if location in self.neighbors.keys():
            raise KeyError('Location already exists.')
        self.neighbors[location] = direction

    def get_items(self) -> list:
        return self.items

    def add_item(self, item) -> None:
        self.items.append(item)

    def remove_item(self, item):
        if item in self.items:
            self.items.remove(item)

    def set_visited(self) -> None:
        self.visited = True

    def get_visited(self) -> bool:
        return self.visited

class Game:
    def __init__(self) -> None:
        self.game = True
        self.commands = self.setup_commands()
        self.create_world()
        self.current_location = self.locations[0]
        self.inventory = []

    def get_commands(self) -> str:
        return self.commands

    def create_world(self) -> None:

        # creates location instances
        #descriptions were generated by ChatGPT
        start = Location("START", "This is the start location.")
        one = Location("ONE", "A cold, dim room with flickering torchlight and stone walls.")
        two = Location("TWO", "A narrow corridor with old tapestries and creaking floorboards.")
        three = Location("THREE", "An open chamber with glowing runes and a cracked altar.")
        four = Location("FOUR", "An overgrown garden, dense with vines and rustling leaves.")
        five = Location("FIVE", "A dusty library with cobwebs and a key on an old table.")
        six = Location("SIX", "A circular room of black marble, echoing with dripping water.")
        seven = Location("SEVEN", "A spiraling staircase, dimly lit by a single lantern.")
        end = Location("END", "This is the end location.")

        #adds neighbors to locations
        start.add_neighbor("East", one)
    
        one.add_neighbor("East", two)

        two.add_neighbor("East", three)
        two.add_neighbor("West", one)
        two.add_neighbor("South", four)

        three.add_neighbor("West", two)
    
        four.add_neighbor("North", two)
        four.add_neighbor("South", six)

        five.add_neighbor("East", six)

        six.add_neighbor("North", four)
        six.add_neighbor("East", seven)
        six.add_neighbor("West", five)

        seven.add_neighbor("East", end)
        seven.add_neighbor("West", six)

        self.locations = [start, one, two, three, four, five, six, seven, end]

        #creates items
        key = Item("Key", "needed to win the game")

        self.items = [key]

        five.add_item(key)

    def setup_commands(self) -> dict:
        """
        Setup commands creates all the commands that the
        user is allowed to enter while playing.

        Each command calls a function that has a
        purpose of its own
        """
        commands = {
            "look": self.look,
            "take": self.take,
            "items": self.show_items,
            "go": self.go,
            "?": self.show_help,
            "help": self.show_help,
            "quit": self.quit,
        }
        return commands

    def play(self) -> None:
        """
        This is the heart of the game.  Runs a while loop that has the user
        enter commands until the game is over.  Commands are split to check if it's valid

        Invalid user input will prompt a print statement

        """
        print("Welcome to the game!  Find the key then travel to the final room to beat the game")
        self.setup_commands()

        while self.game == True:
            user_response = str(input("Enter a command: "))
            tokens = user_response.split()
            command = tokens[0].lower()
            del (tokens[0])
            target: str = str(' '.join(tokens))
            if command in self.get_commands().keys():
                self.get_commands()[command](target)
            else:
                print(f"Unknown command: {command}")

    def show_help(self, args: str = None) -> None:
        """
        Help function.  Activated by typing in "help" or "?".
        This will display all valid commands that can be entered

        
        """
        print("Valid commands are:")
        c = self.setup_commands()
        for key in c:
            print("- " + key)

    def has_key(self, args: str = None) -> bool:
        """
        Checks if user has the key in their inventory.
        """
        for item in self.inventory:
            if item.get_name() == "Key":
                return True
        return False

    def look(self, args: str = None) -> None:
        '''
        The look function prints the current location, items at the location, if any,
        and directions on how to get to the neighbor locations.
        :param args: is so the look function can be called with the same syntax as other commands
        :return: None
        '''

        print('Current Location: ' + self.current_location.name + ' - ' + self.current_location.description)
        print('Items:')
        # If there are items at the location, this will print them
        if len(self.current_location.get_items()) > 0:
            for item in self.current_location.get_items():
                print("- " + item.name)
        else:
            print('None')
        # prints the directions of where the user can move
        # if the player has already visited a neighbor location, this will give them the location name too
        print('Directions:')
        for location, direction in self.current_location.get_neighbors().items():
            if location.get_visited() == True:
                print(direction + ' - ' + location.get_name())
            else:
                print(direction)

    def take(self, target: str) -> None:
        """
        Take takes a target and if the target is in the room,
        it adds the target to users inventory.
        Also adds the weight of the item to your total weight carried
        target - the Item you wish to pick up

        prints "there is no item {target}" if user enters invalid target
        """
        item = None
        for i in self.current_location.get_items():
            if i.get_name().lower() == target.lower():
                item = i
                break
        if item:
            self.current_location.items.remove(item)
            self.inventory.append(item)
            print(f"You have picked up {item.get_name()}")
        else:
            print(f"There is no item named '{target}' in the room.")

    def go(self, target: str) -> None:
        """
        Go takes a target (east/west/north/south) and transports the user there.
        User can only travel to locations directly adjacent to them.

        prints an invalid statement id invalid target

        target - the desired direction user wants to go
        """
        target = abreviation(target)
        if target.capitalize() in self.current_location.get_neighbors().values():
            self.current_location.visited = True
            for location, direction in self.current_location.get_neighbors().items():
                if target.capitalize() == direction:
                    if location.get_name() == "END":
                        if self.has_key():
                            print("YOU UNLOCKED THE FINAL ROOM AND BEAT THE GAME")
                            self.quit()
                        else:
                            print("You must have the key in your inventory to unlock the final room.")
                    else:
                        self.current_location = location
                        print('You have now entered room ' + self.current_location.name + '. ' + self.current_location.description)
            return self.current_location
        else:
            print(f"You can't go {target} from here.")

    def show_items(self, args: str = None) -> None:
        """
        Show items is a command that allows the user to see what
        is in their inventory

        loops over the items in your inventory and prints their
        name, and it's description

        args: is so the look function can be called with the same syntax as other commands
        """
        for item in self.inventory:
            print("- " + Item.__str__(item))

    def quit(self, args: str = None) -> None:
        """
        Is called either when you enter the command 'quit'
        or when you feed Mermaid Man and Barnacle Boy their
        500 calories worth of food

        sets self.game to false, effectively ending the game.

        args: is so the look function can be called with the same syntax as other commands
        """
        self.game = False
        # Code to shut off game

game = Game()
game.play()
