class Character:
    """
    Classe pour représenter un personnage non joueur (PNJ).

    Attributs :
        name (str) : Le nom du personnage.
        description (str) : La description du personnage.
        current_room (Room) : La pièce où se trouve le personnage.
        msgs (list) : Liste des messages associés au personnage.

    Méthodes :
        __str__() : Retourne une représentation textuelle du personnage.
    """

    def __init__(self, name, description, current_room, msgs):
        """
        Initialise un personnage non joueur.

        Args:
            name (str) : Le nom du personnage.
            description (str) : Une description du personnage.
            current_room (Room) : La pièce où se trouve le personnage.
            msgs (list) : Une liste de messages associés au personnage.
        """
        self.name = name
        self.description = description
        self.current_room = current_room
        self.msgs = msgs

    def __str__(self):
        """
        Retourne une représentation textuelle du personnage.

        Returns:
            str : Nom et description du personnage.
        """
        return f"{self.name} : {self.description}"