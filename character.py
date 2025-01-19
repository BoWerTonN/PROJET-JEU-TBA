"""
class character
"""

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
        Fait se déplacer le personnage non joueur, sauf si le personnage est immobile.

        Returns:
            bool: True si le PNJ s'est déplacé, False sinon.
        """
        immobile_characters = ['roi', 'forgeron', 'prisonnier']  # Liste des personnages immobiles
    
        # Si le personnage est immobile, on ne le déplace pas
        if self.name.lower() in immobile_characters:
            print(f"{self.name} reste sur place.")
            return False

        # Si le personnage n'est pas immobile, on procède au déplacement
        if random.choice([True, False]):
            # Récupérer les salles voisines (qui ne sont pas None)
            adjacent_rooms = [room for room in self.current_room.exits.values() if room]
        
            # Vérifier s'il y a des salles voisines
            if adjacent_rooms:
                # Choisir une salle voisine aléatoire
                new_room = random.choice(adjacent_rooms)

                # Afficher un message lorsque le personnage se déplace
                print(f"{self.name} se déplace de {self.current_room.name} vers {new_room.name}.")
            
                # Retirer le personnage de la salle actuelle
                if self.name in self.current_room.characters:
                    del self.current_room.characters[self.name]  # Utilisation de 'del' pour supprimer un dictionnaire

                # Mettre à jour la salle actuelle
                self.current_room = new_room

                # Ajouter le personnage à la nouvelle salle
                self.current_room.characters[self.name] = self
            
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