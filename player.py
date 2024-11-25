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
    
    # Define the move method.
    def move(self, direction):
        # Get the next room from the exits dictionary of the current room.
        next_room = self.current_room.exits[direction]

        # If the next room is None, print an error message and return False.
        if next_room is None:
            print("\nAucune porte dans cette direction !\n")
            return False
        
        # Set the current room to the next room.
        self.current_room = next_room
        print(self.current_room.get_long_description())
        return True

    