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
    
sword = Item("sword", "une épée au fil tranchant comme un rasoir", 2)
print(sword)

