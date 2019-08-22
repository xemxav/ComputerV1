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
    print("this is the help")
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
    len = 0
    for side in eq:
        for group in side:
            len += group.__len__()

    if len != len_eq - 1:
        error(3)

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
            print(a)
        else:
            p = '0'
            a = float(group)
            print(a)
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
    for i in rev_list_expo:
        if dico[i] != 0:
            return int(i)


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
    print('Polynomial degree: ', expo)
    if expo > 2:
        print("The polynomial degree is stricly greater than 2, I can't solve.")
    else:
        solve(simple_form, expo)


if __name__ == '__main__':
    main(sys.argv)
    exit(0)
