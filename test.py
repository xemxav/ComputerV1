import subprocess

tests =[
    "5 + 4 * X^0 + 1* X^2= 0*X^2",
    "5 +  X^0 + 1* X^2= 0*X^2",
    "5 +  X^0 + 1* X^2= 0*X^2",
    "5 * X +  8X^0 + 1* X^2= 0*X^2",
    "0 = 0",
    "5 = 0",
    "5 = 5",
]

if __name__ == '__main__':
    for test in tests:
        print("testé:", test)
        ret = subprocess.run(["python", "computor.py", test])
        print("exit code =", ret.returncode, end="\n\n")


