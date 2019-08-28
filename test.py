import subprocess

#todo : ajouter coef negatifs, ou decimaux

tests =[
    "13 * X^0 + 1 * X^2 = 0 * X^1",
    "8 * X^0 - 6 * X^1 + 0 * X^2 - 5.6 * X^3 = 3 * X^0",
    "5 * X^0 + 4 * X^1 - 9.3 * X^2 = 1 * X^0",
    "5 * X^0 + 4 * X^1 = 4 * X^0",
    "5*X^0=5*X^0",
    "5*X^-1 + 5*X^2 = 8 * X^2",
    "5*X^-2 + 5*X^2 = 5*X^-2",
    "5*X^2.5 + 5*X^2 = 9*X^2.5",
    "5*X^-2 + 5*X^2 = - 8 *X^1",
]

if __name__ == '__main__':
    for test in tests:
        print("testé:", test)
        ret = subprocess.run(["python", "computor.py", test])
        print("exit code =", ret.returncode, end="\n\n")


