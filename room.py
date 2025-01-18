from items import Inventory
from settings import DEBUG

# Define the Room class.

class Room:
    """
    This class represents a command. A command is composed of a command word, a help string, an action and a number of parameters.

    Attributes:
        description (str): Description de la pièce
        name (str): Nom du joueur
        exits (dict): Dictionnaire comprenant les points cardinaux
       

    Methods:
        __init__(self, name, description) : The constructor.
        get_exit(self, direction): Vérifie quelles sorties existent.
        get_exit_string(self): Renvoie au joueur la liste des sorties possibles.
        get_long_description(self): Renvoie la description de la salle ainsi que ses sorties
    """
    # Define the constructor. 
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.exits = {}
        self.inventory = Inventory()
        self.characters = {}
    
    # Define the get_exit method.
    def get_exit(self, direction):
    
        # Return the room in the given direction if it exists.
        if direction in self.exits.keys():
            return self.exits[direction]
        else:
            return None
    
    # Return a string describing the room's exits.
    def get_exit_string(self):
        exit_string = "Sorties: " 
        for exit in self.exits.keys():
            if self.exits.get(exit) is not None:
                exit_string += exit + ", "
        exit_string = exit_string.strip(", ")
        return exit_string

    # Return a long description of this room including exits.
    def get_long_description(self):
        return f"\n{self.description}\n\n{self.get_exit_string()}\n"

   
    def get_inventory(self):
        """
        Produit une description des items et des personnages non joueurs présents dans la pièce.

        Returns:
        str : Une description des items et des PNJ dans la pièce.
        """
        descriptions = []

        # Ajouter les descriptions des items avec le contexte "room"
        items_description = self.inventory.get_inventory_description("room")
        if items_description != "Il n'y a rien ici.":
            descriptions.append(items_description)

        # Ajouter les descriptions des PNJ
        characters_description = ""  # Initialisation par défaut
        if self.characters:
            characters_description = (
                "Les personnages suivants sont ici :\n" +
                "\n".join(f"- {name} : {char.description}" for name, char in self.characters.items())
            )
            descriptions.append(characters_description)

        # Débogage conditionnel
        if DEBUG:
            print(f"DEBUG: Inventaire de la salle {self.name}:")
            print(f"DEBUG: Items -> {items_description}")
            print(f"DEBUG: Personnages -> {characters_description if self.characters else 'Aucun'}")

        # Retourner l'ensemble des descriptions
        if descriptions:
            return "\n".join(descriptions)
        else:
            return "Il n'y a rien ici."

            # Retourner l'ensemble des descriptions
            if descriptions:
                return "\n".join(descriptions)
            else:
                return "Il n'y a rien ici."

    def add_character(self, character):
        """
        Ajoute un personnage non joueur à la pièce.

        Args:
            character (Character) : Le personnage à ajouter.
        """
        self.characters[character.name] = character

    def remove_character(self, character_name):
        """
        Retire un personnage non joueur de la pièce.

        Args:
            character_name (str) : Le nom du personnage à retirer.
        """
        if character_name in self.characters:
            del self.characters[character_name]
