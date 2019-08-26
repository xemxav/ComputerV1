# todo : lire les arguments -> juste une string
# todo : verifier que l'equiation est bien dans une forme a*x^p
# todo : simplifier l'equation
# todo : donner le la plus haute puissance

import sys
import re
from solver import solve


def error(err_code):
    if err_code == 1:
        print("The arguments given are not formated properly. See -h or --help for help")
    elif err_code == 2:
        print("The arguments given are not formated properly. See -h or --help for help")
        print("You did not format properly in the form a * X^p")
    exit(err_code)


def help_computor():
    print("Computor is a tool to solve polynomial equation up to degree 2")
    print("Usage : Python computor.py [-h] [--help] [equation]", end="\n\n")
    print("Please enter your equation as a string as computor's first parameter.")
    print("Or you can launch computer withour any parameter and it will let you enter your equation.")
    print("Please enter your equation as follow :")
    print("A * X^P + ... A_n * X^P_n =  A_n+1 + X^P_n+1")
    print("Each member of the equation must have at least one number (decimal or not)", end="\n\n")
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
    eq = [re.findall(r'[-+]?X\^\d+|[-+]?\d+\.?\d*\*X\^\d+|[-+]?\d+\.?\d*', e) for e in eq]
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
        if re.match(r'[-+]?\d+\.?\d*\*X\^\d+', group) is not None:
            p = group.split('^')[1]
            a = float(group.split('*')[0])
        elif re.match(r'[-+]?X\^\d+', group) is not None:
            p = group.split('^')[1]
            if group.startswith('+'):
                a = 1
            else:
                a = -1
        elif re.match(r'[-+]?\d+\.?\d*', group) is not None:
            p = '0'
            a = float(group)
        else:
            error(2)
        if p in dico.keys():
            dico[p] += a
        else:
            dico[p] = a
    return dico


def print_simple_form(dico):
    list_expo = sorted(dico.keys())
    simple_form = str()
    for i in list_expo:
        if dico[i] < 0:
            simple_form += '- ' + str(dico[i] * -1) + ' * X^' + i
        else:
            simple_form += '+ ' + str(dico[i]) + ' * X^' + i + ' '
    if simple_form.startswith('+'):
        simple_form = simple_form[2:]
    simple_form += ' = 0'
    print("Reduced form:", simple_form)
    return


def get_highest_expo(dico):

    rev_list_expo = sorted(dico.keys(), reverse=True)
    if dico.__len__() == 1 and '0' in dico.keys():
        return 0
    for i in rev_list_expo:
        if dico[i] != 0:
            return int(i)
    return 0

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
    expo = get_highest_expo(simple_form)
    if expo > 0:
        print('Polynomial degree: ', expo)
    if expo > 2:
        print("The polynomial degree is strictly greater than 2, I can't solve.")
    elif expo == 0 and simple_form['0'] == 0:
        print('All the real number are solution to the equation because the sides are equal')
    elif expo == 0 and simple_form['0'] != 0:
        print("The sides are not equal.")
    else:
        solve(simple_form, expo)


if __name__ == '__main__':
    main(sys.argv)
    exit(0)
