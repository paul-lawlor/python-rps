from random import randint
from options import get_option, get_name, get_beats, get_loses, determine_winner
from exception import InvalidOptionError
from time import sleep


def start_game(player_name, rounds):
    # display start game
    print(
        f"Hello {player_name}, welcome to Rock, Paper, Scissors in Python! My name is CPU :)\n"
    )
    print(f"We are going to play {rounds} rounds of Rock, Paper, Scissors!\n")


def play_round(scores):
    errored = False
    # Print options to select
    selection = input(
        """Please select either:
            1. Rock
            2. Paper
            3. Scissors\n"""
    )

    # Get a selection
    try:
        player_selection = get_option(int(selection))
    except InvalidOptionError:
        errored = True
        print("Try again...")
        while errored:
            play_round(scores)
            errored = False

    # Get random selection from CPU
    cpu_selection = get_option(randint(1, 3))

    # Determine the winner
    winner_int = determine_winner(player_selection, cpu_selection)

    # Display result
    get_result(winner_int, player_selection, cpu_selection, scores)


def get_result(winner_int, player_selection, cpu_selection, scores):
    print("\nThe CPU chose...", sep=None)
    sleep(0.5)
    print(f"{cpu_selection.name}\n")
    sleep(1)

    match winner_int:
        case 0:
            print("It's a draw!")
            print(
                f"{get_name(player_selection)} is the same as {get_name(cpu_selection)}\n"
            )
        case 1:
            print("You win!")
            print(f"{list(get_beats(player_selection).values())[0]}\n")
            scores["player"] += 1
        case -1:
            print("You lose!")
            print(f"{list(get_loses(player_selection).values())[0]}\n")
            scores["cpu"] += 1


def end_game(scores):
    player_final = scores["player"]
    cpu_final = scores["cpu"]
    print("---- SCORES ----")
    print(f"You won {player_final} rounds...\n")
    print(f"The CPU won {cpu_final} rounds...\n")

    if player_final > cpu_final:
        print("CONGRATS! YOU WIN!!!")
    elif player_final < cpu_final:
        print("You lose! Better luck next time ;)")
    else:
        print("It's a draw!!!")
