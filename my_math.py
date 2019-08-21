def my_abs(x):
    if x < 0:
        return -x
    return x


def my_sqrt(x, TOLERANCE=0.000001):
    y = 1.0
    while (my_abs(x / y - y) > TOLERANCE):
        y = (y + x / y) / 2.0
    return y