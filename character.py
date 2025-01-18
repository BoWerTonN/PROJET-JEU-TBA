import random
from settings import DEBUG

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
        self._msg_index = 0  # Index pour garder la trace du message à afficher

    def __str__(self):
        """
        Retourne une représentation textuelle du personnage.

        Returns:
            str : Nom et description du personnage.
        """
        return f"{self.name} : {self.description}"

    def move(self):
        """
        Fait se déplacer le personnage non joueur.

        Returns:
            bool: True si le PNJ s'est déplacé, False sinon.
        """
        import random
        if random.choice([True, False]):
            # Récupérer les salles voisines (qui ne sont pas None)
            adjacent_rooms = [room for room in self.current_room.exits.values() if room]
        
            # Vérifier s'il y a des salles voisines
            if adjacent_rooms:
                # Choisir une salle voisine aléatoire
                new_room = random.choice(adjacent_rooms)
            
                if DEBUG:
                    print(f"DEBUG: {self.name} se déplace de {self.current_room.name} vers {new_room.name}.")
            
                # Retirer le PNJ de la salle actuelle
                self.current_room.characters.remove(self)
            
                # Mettre à jour la salle actuelle du PNJ
                self.current_room = new_room
            
                # Ajouter le PNJ à la nouvelle salle
                self.current_room.characters.append(self)
            
                return True
        
        if DEBUG:
            print(f"DEBUG: {self.name} reste dans {self.current_room.name}.")
    
        return False


    def get_msg(self):
        """
        Retourne un message cyclique associé au personnage.

        Returns:
            str: Le message du PNJ.
        """
        if not self.msgs:
            return f"{self.name} n'a rien à dire."
        msg = self.msgs[self._msg_index]
        self._msg_index = (self._msg_index + 1) % len(self.msgs)
        return msg