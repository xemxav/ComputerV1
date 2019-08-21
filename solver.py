
#todo : supprimer import interdit
from math import sqrt

from my_math import my_sqrt


def first_degree(dico):
    if dico['1'] != 0:
        result = dico['0'] / dico['1']
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
    print(a,b,c)
    return (b * b) - (4 * a * c), a, b, c

def positiv_discriminant(discriminant, a, b):
    print("Discriminant is strictly positive, the two solutions are:")
    print("%.6f" % ((-b + my_sqrt(discriminant)) / (2 * a)))
    print("%.6f" % ((-b - my_sqrt(discriminant)) / (2 * a)))


def negativ_discriminant():
    print("Discriminant is strictly negative, the equation does not have solution in real number:")

def null_discriminant(discriminant, a, b):
    print("Discriminant is equal to zero, the only solution is:")
    print("%.6f" % (-b / (2 * a)))

def second_degree(dico):
    discriminant, a, b, c = get_discriminant(dico)
    print('dico:', dico)
    print('discriminant', discriminant)
    if type(discriminant) == type(float()):
        discriminant = round(discriminant, 5)
    if discriminant > 0:
        positiv_discriminant(discriminant, a, b)
    elif discriminant < 0:
        negativ_discriminant()
    elif discriminant == 0:
        null_discriminant(discriminant, a, b)



def solve(simple_form, expo):
    if expo == 2:
        second_degree(simple_form)
    if expo == 1:
        first_degree(simple_form)
    elif expo == 0:
        pass