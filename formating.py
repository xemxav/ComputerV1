#!/Users/xmoreau/.brew/opt/python/bin/python3.7


def print_solution(solution, ending='\n'):
    if isinstance(solution, str):
        print(solution, end=ending)
    if isinstance(solution, float) and not solution.is_integer():
        print(("%.5f" % solution).rstrip('0').rstrip('.'), end=ending)
    else:
        print("%d" % solution, end=ending)
    return


def proper_formating(solution):
    if isinstance(solution, str):
        return solution
    if isinstance(solution, float) and not solution.is_integer():
        return ("%.5f" % solution).rstrip('0').rstrip('.')
    else:
        return "%d" % solution
