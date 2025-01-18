from items import Inventory
from character import Character
from settings import DEBUG
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
    def __init__(self, name, max_weight=15):
        self.name = name
        self.current_room = None
        self.history = []
        self.inventory = Inventory()
        self.max_weight = max_weight  # Poids maximal que le joueur peut porter

        
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

        # Condition de victoire : si on entre dans la grotte avec la carte et l'épée
        if next_room.name == "Grotte":
            print(f"DEBUG: Inventaire actuel: {self.inventory.items}")
            if self.inventory.contains("carte") and self.inventory.contains("epee"):
                print("Vous entrez dans la grotte. Un rugissement retentit, et un dragon colossal surgit des ténèbres.  Ses yeux rouges vous fixent avec fureur. Vous brandissez votre épée et esquivez de justesse son souffle brûlant. Profitant d’une ouverture, vous frappez son flanc, mais ses écailles sont dures comme l’acier. Le dragon riposte, vous projette contre une paroi, mais vous tenez bon.Voyant son ventre exposé, vous rassemblez vos forces pour un coup décisif. Votre épée transperce son cœur. Le dragon s’effondre dans un rugissement final, et le silence retombe. Devant vous, un trésor brille. Vous sortez victorieux, héros de votre propre légende. Félicitations, vous avez terminé le jeu !")
                print("Félicitations, vous avez terminé le jeu !")
                exit()  # Arrêter le jeu
            else:
                if not self.inventory.contains("carte"):
                    print("\nVous avez besoin de la carte pour accéder à la grotte.\n")
                if not self.inventory.contains("epee"):
                    print("Vous entrez dans la grotte, mais le dragon vous fixe avec ses yeux rouges. Vous tentez de l'affronter, mais sans votre épée, vous êtes impuissant. Le dragon vous attaque sauvagement, et vous n'avez aucune chance de survie...")
                return False

        # Vérifier si l'accès à la grotte est restreint
        if next_room.name == "Grotte" and not self.inventory.contains("carte"):
            print("\nVous avez besoin de la carte pour accéder à la grotte.\n")
            return False
        

        self.history.append(self.current_room)
        # Set the current room to the next room.
        self.current_room = next_room
        print(self.current_room.get_long_description())
        print(self.get_history())

        # Déplacer les PNJ une fois que le joueur a bougé.
        self.move_pnj()  # Déplace les PNJ après chaque déplacement du joueur.

        return True

    def move_pnj(self):
        # Utiliser une liste des noms des personnages dans la pièce pour éviter l'erreur de modification du dictionnaire pendant l'itération
        for character_name in list(self.current_room.characters.keys()):  # Créer une copie des clés
            character = self.current_room.characters[character_name]
            character.move()  # Déplace chaque PNJ

    def get_history(self):
        return(
            "\nVous avez déja visité les lieux suivants:\n"+
            "\n".join(f"-{room.name}"for room in self.history)
        )

    def get_inventory(self):
        """
        Retourne la description de l'inventaire du joueur.

        Return :
            str : Une chaîne listant les objets ou indiquant que l'inventaire est vide.
        """
        return self.inventory.get_inventory_description()
        
    def get_total_weight(self):
        """
        Calcule le poids total des objets dans l'inventaire du joueur.
        
        Returns:
            int : Poids total des objets dans l'inventaire.
        """
        return sum(item.weight for item in self.inventory.items)
    