
#todo : lire les arguments -> juste une string
#todo : verifier que l'equiation est bien dans une forme a*x^p
#todo : simplifier l'equation
#todo : donner le la plus haute puissance

import sys
import re
from solver import solve


def check_argv(argv):
    if '-h' in argv[1:] or '--help' in argv[1:] or len(argv) == 1:
        print("this is the help")
        exit()
    if len(argv) > 2:
        return False
    if argv[1].count('=') != 1:
        return False
    return True


def get_grouping(eq):
    eq = re.sub(r'\s+', '', eq)
    len_eq = eq.__len__()
    eq = eq.split('=')
    eq = [re.findall(r'[-+]?\d+\.?\d*\*X\^\d+', e)for e in eq]

    len = 0
    for side in eq:
        for group in side:
            len += group.__len__()

    if len != len_eq - 1:
        print("You did not format properly in the form a * X^p")
        exit()

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
        p = group.split('^')[1]
        a = float(group.split('*')[0])
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
            simple_form += '- ' + str(dico[i] * -1) + ' * X^'+i
        else:
            simple_form += '+ ' + str(dico[i]) + ' * X^' + i + ' '
    if simple_form.startswith('+'):
        simple_form = simple_form[2:]
    simple_form += ' = 0'
    print("Reduced form:",simple_form)
    return


def get_highest_expo(dico):
    rev_list_expo = sorted(dico.keys(), reverse=True)
    for i in rev_list_expo:
        if dico[i] != 0:
            return int(i)


def main(argv):
    if not check_argv(argv):
        print("The arguments given are not formated properly. See -h or --help for help")
    equation = get_grouping(argv[1])
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
    exit()
