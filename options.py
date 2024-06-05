from enum import Enum
from exception import InvalidOptionError


class Option(Enum):
    """
    This is a class to represent the options in the Rock, Paper Scissors game.

    Attributes:
        value: the value of the option (1, 2 or 3).
        beats: the value of the option which gets beaten by the chosen Option AND a descriptive message
        loses: the value which makes the chosen Option lose AND a descriptive message
    """

    ROCK = (1, {3: "\nRock beats Scissors!\n"}, {2: "\nRock loses to Paper :(\n"})
    PAPER = (2, {1: "\nPaper beats Rock!\n"}, {3: "\nPaper loses to Scissors :(\n"})
    SCISSORS = (
        3,
        {2: "\nScissors beats Paper!\n"},
        {1: "\nScissors loses to Rock :(\n"},
    )

    """
    # Used this StackOverflow post and blog to help with Enums:
    # https://stackoverflow.com/questions/12680080/python-enums-with-attributes
    # https://jwodder.github.io/kbits/posts/multi-value-enum/ 
    """

    def __new__(cls, value, beats, loses):
        option = object.__new__(cls)
        option._value_ = value
        option.beats = beats
        option.loses = loses
        return option


def get_option(option_number):
    """Function to return an option based on a number"""
    match option_number:
        case 1:
            return Option.ROCK
        case 2:
            return Option.PAPER
        case 3:
            return Option.SCISSORS
        case _:
            raise InvalidOptionError.cause_error(InvalidOptionError)


def get_value(option):
    """Returns the Options value."""
    return option.value


def get_name(option):
    return option.name


def get_beats(option):
    """Returns the info on what Option beats."""
    return option.beats


def get_loses(option):
    """Returns the info on what beats the Option."""
    return option.loses


def determine_winner(player_selection, cpu_selection):
    player_value = get_value(player_selection)
    cpu_value = get_value(cpu_selection)

    if player_value == cpu_value:  # DRAW
        return 0
    elif cpu_value in get_beats(player_selection).keys():  # PLAYER WINS
        return 1
    else:  # COMPUTER WINS
        return -1
