#!/Users/xmoreau/.brew/opt/python/bin/python3.7

import re


def error(err_code):
    if err_code == 1:
        print("The arguments given are not formatted properly. See -h or --help for help")
    elif err_code == 2:
        print("The arguments given are not formatted properly. See -h or --help for help")
        print("You did not format properly in the form a * X^p")
    elif err_code == 4:
        print("An error has occurred.")
    exit(err_code)


def help_computor():
    print("Computor is a tool to solve polynomial equation up to degree 2")
    print("Usage : Python computor.py [-h] [--help] [equation]", end="\n\n")
    print("Please enter your equation as a string as computor's first parameter.")
    print("Or you can launch computer without any parameter and it will let you enter your equation.")
    print("Please enter your equation as follow :")
    print("A * X^P + ... A_n * X^P_n =  A_n+1 + X^P_n+1")
    print("Each member of the equation must be formatted this way", end="\n\n")
    print("Type -h or --h to see the help again")
    exit(0)


def check_argument(arg):
    if '-h' in arg or '--help' in arg:
        help_computor()
    if arg.count('=') != 1:
        error(2)
    return


def get_grouping(eq):
    eq = re.sub(r'\s+', '', eq)
    len_eq = eq.__len__()
    eq = eq.split('=')
    if eq[1] == '':
        error(1)
    eq = [re.findall(r'[-+]?\d+\.?\d*\*X\^[-+]?\d+\.?\d*|[-+]?\d+\.?\d*', e) for e in eq]
    lenght = 0
    for side in eq:
        for group in side:
            lenght += group.__len__()

    if lenght != len_eq - 1:
        error(2)

    for group in eq[1]:
        if group.startswith('-'):
            eq[0].append(group[1:])
        elif group.startswith('+'):
            eq[0].append('-' + group[1:])
        elif '+' not in group:
            eq[0].append('-' + group)
    return eq[0]
