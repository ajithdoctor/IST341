import random  # imports the library named random


def rps():
    """ this plays a game of rock-paper-scissors-lizard-spock
        (or a variant of that game)
        arguments: no arguments    (prompted text doesn't count as an argument)
        results: no results        (printing doesn't count as a result)
    """

    def print_state(comp_choice=None):
        print("Ha! I really chose :: " + comp_choice + "--I WIN!")

    def better_luck_next():
        print("Better luck next time...")

    choices = {'R': "rock", "P": 'paper', "s": 'scissors', "L": 'lizard', "S": 'spock'}
    print("List of choices :: ", [choices])

    user = input("Choose your weapon: ")
    if user == 'R' or user == 'r':
        key = 'R'
        user = choices[key]
    elif user == 'P' or user == 'p':
        key = 'P'
        user = choices[key]
    elif user == 's':
        key = 's'
        user = choices[key]
    elif user == 'L' or user == 'l':
        key = 'L'
        user = choices[key]
    elif user == 'S':
        key = 'S'
        user = choices[key]

    comp = random.choice(['rock', 'paper', 'scissors', 'lizard', 'spock'])
    print()

    print('The user (you)  chose :: ', user)
    print('The computer (I) chose :: ', comp)
    print()

    if user == 'rock' and comp == 'paper':
        print_state(comp_choice=comp)
        better_luck_next()
    elif user == 'paper' and comp == 'scissors':
        print_state(comp_choice=comp)
        better_luck_next()
    elif user == 'scissors' and comp == 'spock':
        print_state(comp_choice=comp)
        better_luck_next()
    elif user == 'spock' and comp == 'lizard':
        print_state(comp_choice=comp)
        better_luck_next()
    elif user == 'lizard' and comp == 'rock':
        print_state(comp_choice=comp)
        better_luck_next()
    else:
        print('OK! You Win! I chose', comp)
