quitquclass Item:
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

        Paramètres :
            item (Item) : L'objet à ajouter.
        """
        self.items.add(item)

    def get_inventory_description(self):
        """
        Retourne une description de l'inventaire.

        Retour :
            str : Une chaîne listant les objets ou un message si l'inventaire est vide.
        """
        if not self.items:
            return "Il n'y a rien ici."
        return (
            "La pièce contient :\n" +
            "\n".join(f"    - {item.name} : {item.description} ({item.weight} kg)" for item in self.items)
        )

