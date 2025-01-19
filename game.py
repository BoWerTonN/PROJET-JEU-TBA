"""
class game
"""

# Import modules

from room import Room
from player import Player
from command import Command
from actions import Actions
from items import Item
from character import Character
from settings import DEBUG
import tkinter as tk
class Game:

    # Constructor
    def __init__(self):
        self.finished = False
        self.rooms = []
        self.commands = {}
        self.player = None
    """
    def display_welcome_message():
    # Créer une fenêtre Tkinter
    window = tk.Tk()
    window.title("Bienvenue dans l'aventure !")
    
    # Créer un label avec le message de bienvenue
    welcome_label = tk.Label(window, text="Bienvenue dans l'aventure !\nVous êtes sur le point de commencer une aventure épique. Bonne chance !", font=("Arial", 14))
    welcome_label.pack(pady=20)
    
    # Ajouter un bouton pour fermer la fenêtre
    close_button = tk.Button(window, text="Commencer l'aventure", command=window.destroy, font=("Arial", 12))
    close_button.pack(pady=20)
    
    # Lancer la fenêtre Tkinter
    window.mainloop()
# Je n'arrive pas à afficher une fenêtre avec github
# Appeler la fonction pour afficher le message de bienvenue
display_welcome_message()
"""
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
        self.player.current_room = village

        # Création des items
        epee = Item("epee", "une épée au fil tranchant comme un rasoir", 5)
        clef = Item("clef", "une clé dorée ouvrant une porte secrète", 1)
        pain = Item("pain", "un morceau de pain rassis", 1)
        carte = Item("carte", "une carte ancienne montrant des chemins oubliés", 1)
        buche = Item("buche", "un énorme bout de bois, certainement trop lourd pour être porté seul", 20)

        # Ajout des items aux salles
        foret.inventory.add(buche)
        village.inventory.add(epee)
        donjon.inventory.add(carte)
        prison.inventory.add(clef)
        prison.inventory.add(pain)

        # Création du joueur avec une capacité de 15 kg
        player = Player("Héros", max_weight=15)
        

        # Création des PNJ
        bucheron = Character("Bûcheron", "Un robuste homme avec une hache, prêt à couper du bois dans la forêt.", foret, ["Je suis Pierre, le bûcheron. Si vous avez besoin de bois, vous savez où me trouver.",
               "Ce bois est parfait pour l'hiver, vous ne trouvez pas ?",
               "La forêt est grande, mais je connais chaque arbre ici."])
        roi = Character("Roi", "Le souverain du royaume, portant une couronne d'or et un manteau royal.", chateau, ["Salut aventurier ! Un terrible dragon menace notre royaume... Si tu es assez courageux, arme toi d'une épée et récupère la carte dans mon donjon, tu sauras où ce trouve l'antre de ce monstre ! Je te couvrirai d'or à ton retour ! Si tu reviens bien sûr..."])
        forgeron = Character("Forgeron", ".", village, ["Je peux forger une épée pour vous."])
        prisonnier = Character("Prisonnier", "Un homme enchaîné, avec une barbe longue et des yeux fatigués.", prison, ["Les murs ici semblent m'étouffer.", 
               "Si seulement quelqu'un pouvait m'aider à m'échapper..."])
        villageois = Character("Villageois","Un homme vêtu simplement, qui semble toujours occupé par les tâches du village.", village, ["Êtes-vous l'aventurier venu nous sauver ?"])

        # Associer les PNJ aux pièces
        foret.add_character(bucheron)
        village.add_character(forgeron)
        chateau.add_character(roi)
        prison.add_character(prisonnier)
        village.add_character(villageois)

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
        print("Vous devriez allez voir le roi dans le château, il a une quête pour vous !")
        #
        print(self.player.current_room.get_long_description())
    


def main():
    # Create a game object and play the game
    Game().play()
    

if __name__ == "__main__":
    main()
