# Description: Game class

# Import modules

from room import Room
from player import Player
from command import Command
from actions import Actions

class Game:

    # Constructor
    def __init__(self):
        self.finished = False
        self.rooms = []
        self.commands = {}
        self.player = None
    
    # Setup the game
    def setup(self):

        # Setup commands

        help = Command("help", " : afficher cette aide", Actions.help, 0)
        self.commands["help"] = help
        quit = Command("quit", " : quitter le jeu", Actions.quit, 0)
        self.commands["quit"] = quit
        go = Command("go", " <direction> : se déplacer dans une direction (N, E, S, O, U, D )", Actions.go, 1)
        self.commands["go"] = go
        
        # Setup rooms

        foret = Room("Foret", "foret")
        self.rooms.append(foret)
        rempart = Room("Rempart", "rempart")
        self.rooms.append(rempart)
        grotte = Room("Grotte", "grotte")
        self.rooms.append(grotte)
        cascade = Room("Cascade", "cascade")
        self.rooms.append(cascade)
        village = Room("Village", "village")
        self.rooms.append(village)
        champ = Room("Champ", "champ")
        self.rooms.append(champ)
        chateau = Room("Chateau", "chateau" )
        self.rooms.append(chateau)
        donjon = Room("Donjon","donjon")
        self.rooms.append(donjon)
        prison = Room("Prison","prison")

        # Create exits for rooms

        foret.exits = {"N" : cascade, "E" : None, "S" : village, "O" : None, "U": None, "D": None}
        rempart.exits = {"N" : None, "E" : None, "S" : None, "O" : None, "U": None, "D": chateau}
        grotte.exits = {"N" : None, "E" : None, "S" : cascade, "O" : None, "U": None, "D": None}
        cascade.exits = {"N" : grotte, "E" : None, "S" : foret, "O" : None, "U": None, "D": None}
        village.exits = {"N" : foret, "E" : chateau, "S" : champ, "O" : None, "U": None, "D": None}
        champ.exits = {"N" : village, "E" : None, "S" : None, "O" : None, "U": None, "D": None}
        chateau.exits = {"N" : None, "E" : village, "S" : None, "O" :donjon, "U": rempart, "D": None}
        donjon.exits = {"N" : None, "E" : None, "S" : None, "O" : chateau, "U": None, "D": prison}
        prison.exits = {"N" : None, "E" : None, "S" : None, "O" : None, "U": donjon, "D": None}

        # Setup player and starting room

        self.player = Player(input("\nEntrez votre nom: "))
        self.player.current_room = chateau

    # Play the game
    def play(self):
        self.setup()
        self.print_welcome()
        # Loop until the game is finished
        while not self.finished:
            # Get the command from the player
            self.process_command(input("> "))
        return None

    # Process the command entered by the player
    def process_command(self, command_string) -> None:

        # Split the command string into a list of words
        list_of_words = command_string.split(" ")

        command_word = list_of_words[0]

        # If the command is not recognized, print an error message
        if command_word not in self.commands.keys():
            print(" ")
        # If the command is recognized, execute it
        else:
            command = self.commands[command_word]
            command.action(self, list_of_words, command.number_of_parameters)

    # Print the welcome message
    def print_welcome(self):
        print(f"\nBienvenue {self.player.name} dans ce jeu d'aventure !")
        print("Entrez 'help' si vous avez besoin d'aide.")
        #
        print(self.player.current_room.get_long_description())
    

def main():
    # Create a game object and play the game
    Game().play()
    

if __name__ == "__main__":
    main()
