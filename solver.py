#!/usr/bin/venv python3

from formating import print_solution, proper_formating


def first_degree(dico):
    if dico['1'] != 0:
        result = (-1 * dico['0']) / dico['1']
        print("The only solution is:")
        print_solution(result)
    else:
        print("The equation doesn't have a solution")


def get_discriminant(dico):
    a = 0
    b = 0
    c = 0

    if '0' in dico.keys():
        c = dico['0']
    if '1' in dico.keys():
        b = dico['1']
    if '2' in dico.keys():
        a = dico['2']
    return (b ** 2) - (4 * a * c), a, b, c


def positiv_discriminant(discriminant, a, b):
    print("Discriminant is strictly positive, the two solutions are:")
    print_solution((-b + discriminant ** (1 / 2)) / (2 * a))
    print_solution((-b - discriminant ** (1 / 2)) / (2 * a))


def negativ_discriminant(discriminant, a, b):
    print("Discriminant is strictly negative, the equation does not have solution in R but admits 2 solutions in C:")

    s1 = '('
    if b != 0:
        start_minus = proper_formating(b * -1) + ' - i * '
    else:
        start_minus = '- i * '
    s1 += start_minus + proper_formating(abs(discriminant) ** (1 / 2)) + ') / ' + proper_formating(2 * a) + '\nor\n'
    s1 += start_minus + proper_formating((abs(discriminant) ** (1 / 2)) / (2 * a))
    print(s1)
    print('and')
    s2 = '('
    if b != 0:
        start_plus = proper_formating(b * -1) + ' + i * '
    else:
        start_plus = 'i * '
    s2 += start_plus + proper_formating(abs(discriminant) ** (1 / 2)) + ') / ' + proper_formating(2 * a) + '\nor\n'
    s2 += start_plus + proper_formating((abs(discriminant) ** (1 / 2)) / (2 * a))
    print(s2)
    return


def null_discriminant(a, b):
    print("Discriminant is equal to zero, the only solution is:")
    print_solution(-b, ending=" / ")
    print_solution(2 * a)
    print('equal to')
    print_solution(-b / (2 * a))


def second_degree(dico):
    discriminant, a, b, c = get_discriminant(dico)
    if isinstance(discriminant, float):
        discriminant = round(discriminant, 5)
    if discriminant > 0:
        positiv_discriminant(discriminant, a, b)
    elif discriminant < 0:
        negativ_discriminant(discriminant, a, b)
    elif discriminant == 0:
        null_discriminant(a, b)


def solve(simple_form, expo):
    if expo == 2:
        second_degree(simple_form)
    if expo == 1:
        first_degree(simple_form)
    return
