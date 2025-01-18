
# Description: The actions module.

# The actions module contains the functions that are called when a command is executed.
# Each function takes 3 parameters:
# - game: the game object
# - list_of_words: the list of words in the command
# - number_of_parameters: the number of parameters expected by the command
# The functions return True if the command was executed successfully, False otherwise.
# The functions print an error message if the number of parameters is incorrect.
# The error message is different depending on the number of parameters expected by the command.


# The error message is stored in the MSG0 and MSG1 variables and formatted with the command_word variable, the first word in the command.
# The MSG0 variable is used when the command does not take any parameter.
MSG0 = "\nLa commande '{command_word}' ne prend pas de paramètre.\n"
# The MSG1 variable is used when the command takes 1 parameter.
MSG1 = "\nLa commande '{command_word}' prend 1 seul paramètre.\n"

class Actions:

    def go(game, list_of_words, number_of_parameters):
        """
        Move the player in the direction specified by the parameter.
        The parameter must be a cardinal direction (N, E, S, O).

        Args:
            game (Game): The game object.
            list_of_words (list): The list of words in the command.
            number_of_parameters (int): The number of parameters expected by the command.

        Returns:
            bool: True if the command was executed successfully, False otherwise.

        Examples:
        
        >>> from game import Game
        >>> game = Game()
        >>> game.setup()
        >>> go(game, ["go", "N"], 1)
        True
        >>> go(game, ["go", "N", "E"], 1)
        False
        >>> go(game, ["go"], 1)
        False

        """
        
        player = game.player
        l = len(list_of_words)

        # Listes des appellations possibles pour chaque direction
        nord = ["N", "n", "nord", "NORD", "Nord"]
        sud = ["S", "s", "sud", "SUD", "Sud"]
        est = ["E", "e", "est", "EST", "Est"]
        ouest = ["O", "o", "ouest", "OUEST", "Ouest"]
        up = ["U","u","up","UP","Up"]
        down = ["D","d","down",'DOWN',"Down"]

        # If the number of parameters is incorrect, print an error message and return False.
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG1.format(command_word=command_word))
            return False
        
        # Get the direction from the list of words.
        direction = list_of_words[1]

         # Move the player in the direction specified by the parameter.
        if direction in nord:
            player.move("N")
        elif direction in sud:
            player.move("S")
        elif direction in est:
            player.move("E")
        elif direction in ouest:
            player.move("O")
        elif direction in up:
            player.move("U")
        elif direction in down:
            player.move("D")

        else:
            print("\nDirection inconnue. Veuillez entrer une direction valide : N, S, E, O, U, D")
            return False
            
        return True

    def quit(game, list_of_words, number_of_parameters):
        """
        Quit the game.

        Args:
            game (Game): The game object.
            list_of_words (list): The list of words in the command.
            number_of_parameters (int): The number of parameters expected by the command.

        Returns:
            bool: True if the command was executed successfully, False otherwise.

        Examples:

        >>> from game import Game
        >>> game = Game()
        >>> game.setup()
        >>> quit(game, ["quit"], 0)
        True
        >>> quit(game, ["quit", "N"], 0)
        False
        >>> quit(game, ["quit", "N", "E"], 0)
        False

        """
        l = len(list_of_words)
        # If the number of parameters is incorrect, print an error message and return False.
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG0.format(command_word=command_word))
            return False
        
        # Set the finished attribute of the game object to True.
        player = game.player
        msg = f"\nMerci {player.name} d'avoir joué. Au revoir.\n"
        print(msg)
        game.finished = True
        return True

    def help(game, list_of_words, number_of_parameters):
        """
        Print the list of available commands.
        
        Args:
            game (Game): The game object.
            list_of_words (list): The list of words in the command.
            number_of_parameters (int): The number of parameters expected by the command.

        Returns:
            bool: True if the command was executed successfully, False otherwise.

        Examples:

        >>> from game import Game
        >>> game = Game()
        >>> game.setup()
        >>> help(game, ["help"], 0)
        True
        >>> help(game, ["help", "N"], 0)
        False
        >>> help(game, ["help", "N", "E"], 0)
        False

        """

        # If the number of parameters is incorrect, print an error message and return False.
        l = len(list_of_words)
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG0.format(command_word=command_word))
            return False
        
        # Print the list of available commands.
        print("\nVoici les commandes disponibles:")
        for command in game.commands.values():
            print("\t- " + str(command))
        print()
        return True

    def back(game, list_of_words, number_of_parameters):
        """
    Permet au joueur de revenir à la salle précédente.
    
    Args:
        game (Game): L'objet du jeu.
        list_of_words (list): Liste des mots dans la commande.
        number_of_parameters (int): Le nombre de paramètres attendus par la commande.

    Returns:
        bool: True si la commande est exécutée avec succès, False sinon.
    """
    # Vérifier si l'historique des salles est vide ou contient qu'une seule salle
        if len(game.player.history) <= 1:  # Si l'historique contient 1 ou moins de salles, le joueur est déjà à son point de départ
            print("Le joueur est à son point d'apparition")
            return False
    
    # Récupérer la salle précédente à partir de l'historique
        previous_room = game.player.history[-1]  # La deuxième dernière salle dans l'historique
        print(f"Vous êtes revenu dans : {previous_room.name}.")
    
        game.player.current_room = previous_room
        print(game.player.current_room.get_long_description())

        game.player.history.pop()  # La salle actuelle est en dernière position, donc on la retire
        print(game.player.get_history())

        return True
        


    def check(game, list_of_words, number_of_parameters):
        """
        Affiche la liste des items dans l'inventaire du joueur.

        Args:
            game (Game): L'objet du jeu.
            list_of_words (list): Les mots de la commande saisie.
            number_of_parameters (int): Le nombre de paramètres attendu pour cette commande.
        """
        # Afficher les items présents dans l'inventaire du joueur
        print(game.player.inventory.get_inventory_description(context="player"))    
   


    def look(game, list_of_words, number_of_parameters):
        """
        Affiche la description de la pièce actuelle et la liste des items présents.

        Paramètres :
            game (Game) : L'objet principal du jeu.
            list_of_words (list) : Les mots de la commande entrée.
            number_of_parameters (int) : Le nombre de paramètres attendus pour la commande.
        """

        # Afficher les items présents dans la pièce
        current_room = game.player.current_room
        print(current_room.get_inventory())


    def take(game, list_of_words, number_of_parameters):
        """
        Permet au joueur de prendre un item dans la pièce où il se trouve.

        Args:
            game: Instance du jeu.
            list_of_words (list): Liste des mots de la commande.
            number_of_parameters (int): Nombre attendu de paramètres.

        Returns:
            None
        """
        player = game.player

        if len(list_of_words) < 2:
            print("Vous devez spécifier l'item à prendre. Exemple : 'take sword'")
            return

        item_name = " ".join(list_of_words[1:])
        current_room = game.player.current_room
        room_inventory = current_room.inventory
        player_inventory = game.player.inventory

        # Chercher l'item dans l'inventaire de la pièce
        item_to_take = None
        for item in room_inventory.items:
            if item.name.lower() == item_name.lower():
                item_to_take = item
                break

        if not item_to_take:
            print(f"L'item '{item_name}' n'est pas présent dans cette pièce.")
            return

        # Vérifier si le joueur peut prendre l'objet (en fonction du poids)
        total_weight = player.get_total_weight() + item.weight
        if total_weight > player.max_weight:
            print(f"Vous ne pouvez pas prendre {item_name}. L'objet est trop lourd pour votre inventaire ({total_weight}/{player.max_weight} kg).")
            return False

        # Chercher l'item dans l'inventaire de la pièce
        for item in room_inventory.items:
            if item.name.lower() == item_name.lower():
                # Ajouter l'item à l'inventaire du joueur
                player_inventory.add(item)
                # Retirer l'item de l'inventaire de la pièce
                room_inventory.remove(item)
                print(f"Vous avez pris l'item : {item}.")
                return


    def drop(game, list_of_words, number_of_parameters):
        """
        Permet au joueur de reposer un item dans la pièce où il se trouve.

        Args:
            game: Instance du jeu.
            list_of_words (list): Liste des mots de la commande.
            number_of_parameters (int): Nombre attendu de paramètres.

        Returns:
            None
        """
        if len(list_of_words) < 2:
            print("Vous devez spécifier l'item à reposer. Exemple : 'drop sword'")
            return

        item_name = " ".join(list_of_words[1:])
        player_inventory = game.player.inventory
        current_room_inventory = game.player.current_room.inventory

        # Chercher l'item dans l'inventaire du joueur
        for item in player_inventory.items:
            if item.name.lower() == item_name.lower():
                # Retirer l'item de l'inventaire du joueur
                player_inventory.remove(item)
                # Ajouter l'item à l'inventaire de la pièce
                current_room_inventory.add(item)
                print(f"Vous avez reposé l'item : {item}.")
                return

        print(f"L'item '{item_name}' n'est pas présent dans votre inventaire.")

    def talk(game, list_of_words, number_of_parameters):
        """
        Permet au joueur de parler à un PNJ dans la pièce actuelle.

        Args:
            game (Game): Instance du jeu.
            list_of_words (list[str]): Les mots de la commande utilisateur.
            number_of_parameters (int): Le nombre de paramètres attendus.
        """
        if len(list_of_words) < 2:
            print("À qui voulez-vous parler ?")
            return

        pnj_name = list_of_words[1].lower()
        current_room = game.player.current_room

        # Vérifie si le PNJ est présent dans la salle
        for key, pnj in current_room.characters.items():
            if key.lower() == pnj_name:  
                print(pnj.get_msg())  # Affiche le message du PNJ
                return
                print(f"Aucun personnage nommé '{pnj_name}' ici.")