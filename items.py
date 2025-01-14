class Item:
    def __init__(self, name, description, weight):
        """
        Initialise un objet de type Item.

        Attributes:

        name (str) : Le nom de l'objet.
        description (str) : La description de l'objet.
        weight (str) : Le poids de l'objet (en kg).

        Methods:

        __str__(self) : représentation textuelle de l'objet.

        """
        self.name = name
        self.description = description
        self.weight = weight

    def __str__(self):
        """
        Redéfinit la méthode __str__ pour une représentation textuelle de l'objet.

        Return : Une chaîne de caractères représentant l'objet.
        """

        return f"{self.name} : {self.description} ({self.weight} kg)"
    
class Inventory:
    """
    Classe pour gérer un inventaire d'objets.

    Attributs :
        items (set) : Un ensemble contenant les objets de l'inventaire.
    """

    def __init__(self):
        """
        Initialise un nouvel inventaire vide.
        """
        self.items = set()

    def add(self, item):
        """
        Ajoute un objet à l'inventaire.
        """
        self.items.add(item)

    def remove(self, item):
        """
        Retire un item de l'inventaire.
        """
        self.items.remove(item)

    def get_inventory_description(self, context):
        """
        Produit une description de l'inventaire.

        Args:
            context (str): Le contexte d'affichage ('player' ou 'room').

        Returns:
            str: Une chaîne décrivant les items de l'inventaire.
        """
        if not self.items:
            if context == "player":
                return "Votre inventaire est vide."
            elif context == "room":
                return "Il n'y a rien ici."
        
        prefix = "Vous disposez des items suivants :" if context == "player" else "La pièce contient :"
        return (
            f"{prefix}\n" +
            "\n".join(f"    - {item}" for item in self.items)
        )
