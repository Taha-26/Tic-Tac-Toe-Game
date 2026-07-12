"""
Tic-Tac-Toe Board Module
~~~~~~~~~~~~~~~~~~~~~~~~

This module governs the internal board matrix state, terminal grid rendering,
and structural verification algorithms for checking wins and draws.
"""

from typing import List


class TicTacToe:
    """
    Manages the 3x3 Tic-Tac-Toe grid data structure and core game rules.

    :cvar WINNING_COMBINATIONS: Immutable lookup table mapping the 8 linear vectors required to win.
    :type WINNING_COMBINATIONS: list[list[int]]
    """

    WINNING_COMBINATIONS = [
        [2, 4, 6],
        [8, 4, 0],
        [0, 1, 2],  # Diagonals and first row
        [3, 4, 5],
        [6, 7, 8],  # Remaining rows
        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],  # Columns
    ]

    def __init__(self):
        """
        Initializes the game board with empty placeholder characters.
        """
        self._empty_char = " "
        self._cells = [self._empty_char] * 9

    def display_board(self, show_indices: bool = False):
        """
        Renders the current state of the grid layout inside the standard output.

        :param show_indices: If True, empty cells display their grid index number (1-9) instead of whitespaces.
        """
        print()
        for index, value in enumerate(self._cells):
            # Safe toggle check: indexes are rendered only if the cell contains the empty token
            display_value = (
                str(index + 1)
                if (show_indices and value == self._empty_char)
                else value
            )

            # Check for rightmost column positions to handle line breaks and dividers
            if index in [2, 5, 8]:
                print(display_value)
                if index != 8:
                    print("─┼─┼─")
            else:
                print(display_value, end="│")
        print()

    def get_empty_cells_index(self) -> List(int):
        """
        Computes the indices of all cells currently unoccupied.

        :return: A list containing integer indexes (0 through 8) of open positions.
        """
        return [
            index
            for index, value in enumerate(self._cells)
            if value == self._empty_char
        ]

    def set_move(self, index: int, mark: str) -> bool:
        """
        Attempts to write a player marker onto a designated board coordinate.

        Encapsulates self-state mutation security by checking availability
        prior to modification.

        :param index: Zero-indexed position on the board (0-8).
        :param mark: The token string representing the active player.

        :return: True if the modification was executed successfully, False if targeted cell was blocked.
        """
        if index in self.get_empty_cells_index():
            self._cells[index] = mark
            return True
        return False

    def is_winner(self, mark: str) -> bool:
        """
        Evaluates the matrix to see if the specified player has satisfied any winning row, column, or diagonal.

        :param mark: The token string to test against the board state.
        :return: True if a winning vector is fully occupied by the marker, False otherwise.
        """
        return any(
            all(self._cells[i] == mark for i in combo)
            for combo in self.WINNING_COMBINATIONS
        )

    def clear_board(self):
        """
        Flushes all grid nodes back to their default empty character states.
        """
        self._cells = [self._empty_char] * 9

    def is_draw(self) -> bool:
        """
        Validates if the game has ended in a deadlock where no moves remain.

        :return: True if no empty spaces exist on the board, False otherwise.
        """
        return not self.get_empty_cells_index()
