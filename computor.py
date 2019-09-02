#!/usr/bin/venv python3

import sys
import re
from solver import solve
from formating import proper_formating

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


def equation_reduction(groups):
    dico = dict()
    for group in groups:
        a = 0
        p = ''
        if re.match(r'[-+]?\d+\.?\d*\*X\^[-+]?\d+\.?\d*', group) is not None:
            p = proper_formating(float(group.split('^')[1]))
            a = float(group.split('*')[0])
        elif re.match(r'[-+]?\d+\.?\d*', group) is not None:
            p = '0'
            a = float(group)
        else:
            error(2)
        if a.is_integer():
            a = int(a)
        if p in dico.keys():
            dico[p] += a
        else:
            dico[p] = a

    to_remove = list()
    for p in dico:
        if dico[p] == 0:
            to_remove.append(p)
    for p in to_remove:
        dico.pop(p)
    return dico


def print_simple_form(dico):
    list_expo = sorted(dico.keys())
    simple_form = str()
    for expo in list_expo:
        if dico[expo] < 0:
            simple_form += '- ' + str(dico[expo] * -1) + ' * X^' + expo + ' '
        else:
            simple_form += '+ ' + str(dico[expo]) + ' * X^' + expo + ' '
    if simple_form.startswith('+'):
        simple_form = simple_form[2:]
    if simple_form == '':
        simple_form += '0 '
    simple_form += '= 0'
    print("Reduced form:", simple_form)
    return


def check_expo(dico):
    error = False
    expo = 0
    if len(dico) == 0 or (len(dico) == 1 and '0' in dico.keys() and dico['0'] == 0):
        err_message = 'All the real number are solution to the equation because the sides are equal.'
        error = True
    if len(dico) == 1 and '0' in dico.keys() and dico['0'] != 0:
        err_message = "The sides are not equal."
        error = True
    if error:
        print('Polynomial degree: 0')
        print(err_message)
        exit(0)
    rev_list_expo = sorted(dico.keys(), reverse=True)
    for i in rev_list_expo:
        if dico[i] != 0:
            expo = float(i)
            expo_str = i
            break
    print('Polynomial degree:', expo_str)
    for i in rev_list_expo:
        if '.' in i:
            print("Computor doesn't accept decimal coefficient.")
            exit(0)
        if '-' in i:
            print("Computor doesn't accept negativ coefficient.")
            exit(0)
    return expo


def main(argv):
    if len(argv) > 2:
        error(1)
    if len(argv) == 1:
        argument = input("Enter your equation or -h/--help for help: ")
    else:
        argument = argv[1]
    check_argument(argument)
    equation = get_grouping(argument)
    simple_form = equation_reduction(equation)
    print_simple_form(simple_form)
    expo = check_expo(simple_form)
    if expo == 0:
        error(4)
    if expo > 2:
        print("The polynomial degree is stricly greater than 2, I can't solve.")
    else:
        solve(simple_form, expo)


if __name__ == '__main__':
    main(sys.argv)
    exit(0)
