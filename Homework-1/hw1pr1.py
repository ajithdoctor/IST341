from math import *


def get_data():
    answers = [("zero is", (4 - 4 + 4 - 4)),
               ("One is", (4 / 4 * 4 / 4)),
               ("Two is", (4 / 4 + 4 / 4)),
               ("three is", (4 - (4 / 4 / 4))),
               ("four is", ((4 - 4) / 4) + 4),
               ("five is", (((4 / 4) ** 4) + 4)),
               ("six is", (((4 + 4) / 4) + 4)),
               ("seven is", int(4 - (4 / 4) + 4)),
               ("eight is", int(4 - 4 + 4 + 4)),
               ("nine is", int((4 + 4) + (4 / 4))),
               ("ten is", int((44 - 4) / 4)),
               ("eleven is", int(44 / (sqrt(4) * (sqrt(4))))),
               ("twelve is", int((4 - (4 / 4)) * 4)),
               ("thirteen is", int((44 / 4) + (sqrt(4)))),
               ("fourteen is", int(4 + 4 + 4 + sqrt(4))),
               ("fifteen is", int((4 * 4) - (4 / 4))),
               ("sixteen is", int(4 * 4 - 4 + 4)),
               ("seventeen is", int(4 * 4) + (4 / 4)),
               ("eighteen is", int(((4 * 4) + (sqrt(4) + .4)))),
               ("nineteen is", int(factorial(4) - ((4 / 4) + 4))),
               ("twenty is", int(44 - 4) / sqrt(4))]
    return answers


def print_num():
    answers = get_data()
    for answer in answers:
        print(answer[0] + " " + str(int(answer[1])))


if __name__ == "__main__":
    print_num()
