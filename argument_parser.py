"""
Sets up an ArgumentParser object and returns command line arguments
"""

from argparse import ArgumentParser


def parser_setup():
    """
    Sets up a parser object and defines the arguments for the program

    Returns:
     args - the command line arguments
    """
    # instantiate Parser object
    parser = ArgumentParser()

    # add player name via command line args
    parser.add_argument(
        "--name",
        "-n",
        help="The name of the Player playing Rock, Paper, Scissors vs the CPU",
        type=str
    )

    # get round count via command line args
    parser.add_argument("--rounds", "-r", help="The number of rounds being played", type=int)

    args = parser.parse_args()

    return args


def get_name(args):
    """
    Gets the name of the player

    Returns:
     name - the name the player has entered (or Player 1 as default)
    """
    name = "Player 1" if not args.name else args.name
    return name


def get_rounds(args):
    """
    Gets the number of rounds to be played

    Returns:
     rounds - the number of rounds to be played (one by default)
    """
    rounds = 1 if not args.rounds else args.rounds
    return rounds
