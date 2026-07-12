"""
Player Module
~~~~~~~~~~~~~

This module defines the Player class used to model individual participants
within the Tic-Tac-Toe game environment.
"""


class Player:
    """
    Represents a game participant.

    Attributes:
        name (str): The unique identifier/name of the player.
        mark (str): The character symbol representing the player on the board (e.g., 'x' or 'o').
        choice (int or None): The cell index chosen by the player during their turn.
    """

    def __init__(self, name: str = "", mark: str = ""):
        """
        Initializes a new Player instance.

        :param name: The name of the player, defaults to an empty string.
        :param mark: The symbol assigned to the player, defaults to an empty string.
        """
        self.name = name
        self.mark = mark
        self.choice = None
