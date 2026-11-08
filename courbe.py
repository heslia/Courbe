import sys
from math import *

eq = " ".join(sys.argv[1:]).replace("^", "**")
g, d = eq.split("=")                          


def F(x, y): # utilisation d'une fonction
    return eval(g) - eval(d)


for j in range(20, -21, -1):
    ligne = ""
    for i in range(-40, 41):
        x, y = i / 2, j
        v = F(x, y)
        if v * F(x + 0.5, y) <= 0 or v * F(x, y - 1) <= 0:
            ligne += "#"
        else:
            ligne += " "
    print(ligne)
