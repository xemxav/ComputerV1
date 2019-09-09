#!/Users/xmoreau/.brew/opt/python/bin/python3.7

from formating import print_solution, proper_formating
from my_math import my_abs, my_sqrt


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
    return (b * b) - (4 * a * c), a, b, c


def positiv_discriminant(discriminant, a, b):
    print("Discriminant is strictly positive, the two solutions are:")
    sqrt_discri = my_sqrt(discriminant)
    print_solution((-b + sqrt_discri) / (2 * a))
    print_solution((-b - sqrt_discri) / (2 * a))


def negativ_discriminant(discriminant, a, b):
    print("Discriminant is strictly negative, the equation does not have solution in R but admits 2 solutions in C:")

    sqrt_discri = my_sqrt(my_abs(discriminant))
    s1 = '('
    top = proper_formating(sqrt_discri) + ') / ' + proper_formating(2 * a) + '\nor\n'
    bottom_1 = proper_formating(sqrt_discri / (2 * a))

    if b != 0:
        start_minus = proper_formating(b * -1) + ' - i * '
        start_minus_red = proper_formating((b * -1) / (2 * a)) + ' - i * '
    else:
        start_minus = '- i * '
        start_minus_red = '- i * '
    s1 += start_minus + proper_formating(sqrt_discri) + ') / ' + proper_formating(2 * a) + '\nor\n'
    s1 += start_minus_red + proper_formating(sqrt_discri / (2 * a))
    print(s1)
    print('and')
    s2 = '('
    if b != 0:
        start_plus = proper_formating(b * -1) + ' + i * '
        start_plus_red = proper_formating((b * -1) / (2 * a)) + ' + i * '
    else:
        start_plus = 'i * '
        start_plus_red = 'i * '
    s2 += start_plus + proper_formating(sqrt_discri) + ') / ' + proper_formating(2 * a) + '\nor\n'
    s2 += start_plus_red + proper_formating(sqrt_discri / (2 * a))
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
