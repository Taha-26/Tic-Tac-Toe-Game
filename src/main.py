"""
Author: https://github.com/Taha-26/

~~~~~~~~~~~~~~~~~~~~~
Main Execution Engine
~~~~~~~~~~~~~~~~~~~~~

The central control system managing initialization, runtime sequencing,
IO sanitization routines, and post-game loop processing.
"""

from random import shuffle
from typing import List

from player import Player
from tic_tac_toe import TicTacToe


def get_validated_input(message: str, valid_inputs: List(str)) -> str:
    """
    Enforces a strict console loop context ensuring only predefined
    strings are processed.

    :param message: The console prompt text presented to the user.
    :param valid_inputs: A collection of expected, safe input strings.

    :return: The validated and sanitized lowercase input string.
    """
    while True:
        user_input = input(message).lower().strip()
        if user_input in valid_inputs:
            return user_input


def setup_players() -> List(Player):
    """
    Handles terminal onboarding sequences for mapping player identities.

    Ensures zero-length values are prohibited and intercepts edge-cases
    such as naming collisions.

    :return: A list containing exactly two initialized and randomly shuffled Player objects.
    """
    names = []
    for i in range(2):
        while True:
            name = input(f"\nEnter name of player {i + 1}: ").strip()
            if not name:
                print("The name cannot be empty.")
                continue
            # Handle case-insensitive equality checks to isolate exact matches
            if name.lower() in [n.lower() for n in names]:
                print("The name of both players cannot be the same.")
                continue
            names.append(name)
            break

    p1 = Player(names[0], "o")
    p2 = Player(names[1], "x")
    players = [p1, p2]

    # Establish turn order equity using random permutation shuffling
    shuffle(players)
    return players


def main():
    """
    App-loop anchor binding state engines together. Manages turn rotation and
    conditional program termination gates.
    """
    game = TicTacToe()
    players = setup_players()

    print("—————Welcome To TicTacToe Game—————\n")

    while True:
        game.clear_board()
        print("\nThe table:")
        game.display_board()
        print("The number of cells:")
        game.display_board(show_indices=True)
        print("Game Started!!!")

        game_running = True

        # Nested loop controls active in-match logic
        while game_running:
            for player in players:
                while True:
                    move_input = (
                        input(f"\nChoice of {player.name} ({player.mark}): ")
                        .strip()
                        .lower()
                    )

                    # Intercept non-destructive display switch command
                    if move_input == "n":
                        game.display_board(show_indices=True)
                        continue

                    # Construct an index registry of available tokens as strings for sanitization check
                    valid_moves = [str(i + 1) for i in game.get_empty_cells_index()]
                    if move_input in valid_moves:
                        player.choice = int(move_input) - 1
                        break
                    else:
                        print(
                            "Invalid choice. Choose an empty cell between 1 and 9 (or 'n' to see cells)."
                        )

                # Mutate board state after passing input constraints
                game.set_move(player.choice, player.mark)
                game.display_board()

                # Rule-checking phase executed after each turn mutation
                if game.is_winner(player.mark):
                    print(f"\n{player.name} Won!\n")
                    game_running = False
                    break

                if game.is_draw():
                    print("\nDraw!\n")
                    game_running = False
                    break

        # Post-match confirmation branches
        replay = get_validated_input("Do you want to play again? (y/n): ", ["y", "n"])
        if replay == "n":
            break

        change_players = get_validated_input("Change players? (y/n): ", ["y", "n"])
        if change_players == "y":
            players = setup_players()


if __name__ == "__main__":
    main()
