import time


def adventure():
    """ this function runs one session of interactive fiction
        Well, it's "fiction," depending on the pill color chosen...
        arguments: no arguments (prompted text doesn't count as an argument)
        results: no results     (printing doesn't count as a result)
    """
    delay = 0.0  # change to 0.0 for testing or speed runs,
    # ..larger for dramatic effect!

    username = input("What do they call you, worthy adventurer? ")

    print()
    print("Welcome,", username, " to the Maze")
    print("of survival and adventure")
    print()

    print("You are in the middle of the maze, do you wish to get out?")
    print()
    print("Choose from one of these weapons: hatchet, blaster, axe")
    weapon = input("What weapon do you want? ")
    if weapon == "hatchet":
        print("Wise! You will like this weapon.")
    elif weapon == "blaster":
        print("Best Choice!", username)
    elif weapon == "axe":
        print(weapon, "is a good choice!")
    else:
        print("Each to their own, then.")
    print()

    print("Now chose from the two paths: right or left")
    path = input("your path of choice?")
    if choice1 == "right":
        print("As you approach to the right, the lights are stonger, until...")
        time.sleep(delay)
        print("...they resolve into unending stacks of poptarts, foil shimmering.")
        print("You succeed, sumptuously, in sating the challenge--and your hunger.")
        print("Go well,", username, "!")

    else:
        print("You push the door into a gathering of sagefowl, athenas, and stags alike,")
        print("all relishing their tasks. Teamwork and merriment abound here, except...")
        time.sleep(delay)
        print("...they have consumed ALL of the poptarts! Drifts of wrappers coat the floor.")
        print("Dizzy, you grasp for a pastry. None is at hand. You exhale and slip")
        print("under the teeming tide of foil as it finishes winding around you.")
        print("Farewell,", username, ".")
