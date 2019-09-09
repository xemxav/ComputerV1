import subprocess

tests =[
    "13 * X^0 + 1 * X^2 = 0 * X^1",
        "5*X^0 = 4*X^0 + 7*X^1",
        "5*X + 13*X^1+3*X^2 = 1*X^0 + 1*X^1",
        "6*X^0 + 11*x^1 + 5*X^2 = 1*X^0 + 1*X^1",
        "5*X^0 + 3*X^1 + 3 * X^2 = 0",
        "5*X^0 + 3*X^1 + 3*X^3 = 0",
        "wefjowe",
        "424",
        "X^2",
        "13 * X^0 + 1 * X^2 = -6 * X^2  fr",
    "5*X^0.0 +3*X^1 + 3*X^2.00000 = 0",
    "4*X^2 + 3 = 0"
]

if __name__ == '__main__':
    for test in tests:
        print("testé:", test)
        ret = subprocess.run(["python", "computor.py", test])
        print("exit code =", ret.returncode, end="\n\n")


