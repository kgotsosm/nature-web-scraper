import math

# your code here


def cheat(*args):
    print("Don't cheat!")


math.factorial = cheat
# don't delete this line, please
math.factorial(23)
