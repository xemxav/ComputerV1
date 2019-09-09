#!/Users/xmoreau/.brew/opt/python/bin/python3.7

def my_abs(x):
    if x < 0:
        return -1 * x
    return x


def my_sqrt(x, tolerance=0.000001):
    y = 1.0
    while (my_abs(x / y - y) > tolerance):
        y = (y + x / y) / 2.0
    return y
