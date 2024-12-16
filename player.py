# Define the Player class.
class Player():
    """
    This class represents a command. A command is composed of a command word, a help string, an action and a number of parameters.

    Attributes:
        current_room (str): Salle dans laquelle le joueur se trouve actuellement 
        name (str): nom du joueur
        

    Methods:
        __init__(self, name) : Le constructeur
        move(self,direction) : Change le joueur de carte

    """

    # Define the constructor.
    def __init__(self, name):
        self.name = name
        self.current_room = None
        self.history = [] 
        
    def set_starting_room(self, starting_room):
        
        # Set the starting room for the player and initialize the history with it.
        
        self.current_room = starting_room
        self.history.append(starting_room) 
    
    # Define the move method.
    def move(self, direction):
        # Get the next room from the exits dictionary of the current room.
        next_room = self.current_room.exits[direction]

        # If the next room is None, print an error message and return False.
        if next_room is None:
            print("\nAucuns lieux dans cette direction !\n")
            return False
        self.history.append(self.current_room)
        # Set the current room to the next room.
        self.current_room = next_room
        print(self.current_room.get_long_description())
        print(self.get_history())
        return True

    def get_history(self):
        return(
            "\nVous avez déja visité les lieux suivants:\n"+
            "\n".join(f"-{room.name}"for room in self.history)
        )

    