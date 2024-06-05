"""
Module which holds the high-level Rock, Paper, Scissors game logic
"""

from argument_parser import parser_setup, get_name, get_rounds
from interface import start_game, end_game, play_round

def main():
    """
    Main method which holds the high-level Rock, Paper, Scissors game logic
    """
    scores = {"player": 0, "cpu": 0}
    # Setup and retrieve command line arguments
    cli_args = parser_setup()
    player_name = get_name(cli_args)
    rounds = get_rounds(cli_args)

    start_game(player_name, rounds)

    # while count is not round count
    for round in range(1, rounds + 1):
        print(f"\t-----THIS IS ROUND {round}-----")
        play_round(scores)

    # end game
    end_game(scores)


if __name__ == "__main__":
    main()
