# Description: Game class

# Import modules

from room import Room
from player import Player
from command import Command
from actions import Actions
from items import Item
from character import Character
from settings import DEBUG
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
        back = Command("back", " <direction> : se déplacer dans une direction (N, E, S, O, U, D )", Actions.back, 0)
        self.commands["back"]= back
        check = Command("check", " : vérifier les items dans votre inventaire", Actions.check, 0)
        self.commands["check"] = check
        look = Command("look", " : voir les items présents dans la pièce actuelle", Actions.look, 0)
        self.commands["look"] = look
        take = Command("take", " : prendre un item dans la pièce où vous vous trouvez", Actions.take, 1)
        self.commands["take"] = take
        drop = Command("drop", " : reposer un item dans la pièce où vous vous trouvez", Actions.drop, 1)
        self.commands["drop"] = drop
        talk = Command("talk", " <pnj> : parler à un personnage non joueur", Actions.talk, 1)
        self.commands["talk"] = talk
        
        # Setup rooms

        foret = Room("Foret", "Une forêt dense et sombre, où la lumière peine à pénétrer. Des racines tordues émergent du sol, comme des griffes cherchant à attraper les imprudents.")
        self.rooms.append(foret)
        rempart = Room("Rempart", "Les murs imposants du rempart témoignent de la grandeur passée de la capitale. Des morceaux de pierre brisée gisent au sol. ")
        self.rooms.append(rempart)
        grotte = Room("Grotte", "Une cavité naturelle creusée dans la roche, humide et oppressante. On dit qu’elle mène à des passages oubliés.")
        self.rooms.append(grotte)
        cascade = Room("Cascade", "Une chute d’eau majestueuse masquant une entrée secrète. Le son apaisant dissimule une tension sous-jacente.")
        self.rooms.append(cascade)
        village = Room("Village", "Le village est calme, presque trop calme, comme s'il attendait quelque chose. Les rues sont désertes, et la plupart des portes sont fermées à double tour.")
        self.rooms.append(village)
        champ = Room("Champ", "Les champs de blé se balancent doucement dans le vent, comme des vagues dorées. Des oiseaux chantent doucement, mais leurs chants semblent moins joyeux qu'autrefois.")
        self.rooms.append(champ)
        chateau = Room("Chateau", "Le château se dresse fièrement, mais sa grandeur passée est maintenant ternie par les signes de l'abandon." )
        self.rooms.append(chateau)
        donjon = Room("Donjon","Le donjon est un lieu froid et humide, où chaque bruit semble amplifié par les murs épais. Le sol est jonché de débris, témoins des années de négligence et d’abandon.")
        self.rooms.append(donjon)
        prison = Room("Prison","Les cellules de la prison sont sombres et exiguës, offrant peu d’espoir à ceux qui y sont enfermés.")
        self.rooms.append(prison)


        # Create exits for rooms

        foret.exits = {"N" : cascade, "E" : None, "S" : village, "O" : None, "U": None, "D": None}
        rempart.exits = {"N" : None, "E" : None, "S" : None, "O" : None, "U": None, "D": chateau}
        grotte.exits = {"N" : None, "E" : None, "S" : cascade, "O" : None, "U": None, "D": None}
        cascade.exits = {"N" : grotte, "E" : None, "S" : foret, "O" : None, "U": None, "D": None}
        village.exits = {"N" : foret, "E" : chateau, "S" : champ, "O" : None, "U": None, "D": None}
        champ.exits = {"N" : village, "E" : None, "S" : None, "O" : None, "U": None, "D": None}
        chateau.exits = {"N" : None, "E" : donjon, "S" : None, "O" : village, "U": rempart, "D": None}
        donjon.exits = {"N" : None, "E" : None, "S" : None, "O" : chateau, "U": None, "D": prison}
        prison.exits = {"N" : None, "E" : None, "S" : None, "O" : None, "U": donjon, "D": None}

        self.rooms = [foret, rempart, grotte, cascade, village, champ, chateau, donjon, prison]


        # Setup player and starting room

        self.player = Player(input("\nEntrez votre nom: "))
        self.player.current_room = chateau

        # Création des items
        sword = Item("sword", "une épée au fil tranchant comme un rasoir", 2)
        shield = Item("shield", "un bouclier léger et résistant", 1)
        helmet = Item("helmet", "un casque en métal", 1)

        herbs = Item("herbs", "des herbes médicinales aux propriétés curatives", 1)
        amulet = Item("amulet", "une amulette mystérieuse gravée de symboles anciens", 1)
        torch = Item("torch", "une torche qui éclaire les endroits sombres", 1)
        golden_key = Item("golden_key", "une clé dorée ouvrant une porte secrète", 1)
        stone = Item("stone", "une pierre étrange et lisse, peut-être magique", 1)
        bread = Item("bread", "un morceau de pain, simple mais nourrissant", 1)
        map = Item("map", "une carte ancienne montrant des chemins oubliés", 1)
        crystal = Item("crystal", "un cristal brillant émettant une douce lumière", 1)

        # Ajout des items aux salles
        foret.inventory.add(sword)
        village.inventory.add(shield)
        chateau.inventory.add(helmet)
        
        grotte.inventory.add(torch)
        cascade.inventory.add(crystal)
        rempart.inventory.add(map)
        prison.inventory.add(golden_key)
        champ.inventory.add(bread)
        foret.inventory.add(herbs)
        village.inventory.add(amulet)
        chateau.inventory.add(stone)

         # Création des PNJ
        gandalf = Character("gandalf", "un magicien blanc", foret, ["Je suis Gandalf", "Abracadabra !"])
        blacksmith = Character("forgeron", "un artisan musclé", village, ["Je peux forger une épée pour vous."])

        # Associer les PNJ aux pièces
        foret.add_character(gandalf)
        village.add_character(blacksmith)


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

        # Si le joueur se déplace (commande 'go' ou 'back'), déplacer les PNJ
        if command_word in ["go", "back"]:
            self.move_pnj()  # Déplacer les PNJ après que le joueur se soit déplacé

    # Méthode pour déplacer les PNJ dans leurs pièces respectives
    def move_pnj(self):
        for room in self.rooms:
            for character in room.characters:
                character.move()


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
