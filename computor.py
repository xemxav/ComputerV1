
#todo : lire les arguments -> juste une string
#todo : verifier que l'equiation est bien dans une forme a*x^p
#todo : simplifier l'equation
#todo : donner le la plus haute puissance

import sys

def check_argv(argv):
    if '-h' in argv[1:] or '--help' in argv[1:] or len(argv) == 1:
        print("this is the help")
        exit()
    if len(argv) > 2 :
        return False
    return True

def main(argv):
    if not check_argv(argv):
        print("The arguments given are not formated properly. See -h or --help for help")

if __name__ == '__main__':
    main(sys.argv)
    exit()