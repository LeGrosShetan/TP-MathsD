import random
import time

def EuclideEtendu(a, b):
    if b == 0:
        return a, 1, 0

    res = EuclideEtendu(b, a % b)

    dp = res[0]
    xp = res[1]
    yp = res[2]

    return dp, yp, xp - a / b * yp


def ExpMod(a, k, n):
    p = 1
    while k > 0:
        if k % 2 != 0:
            p = (p * a) % n
        a = (a * a) % n
        k = k // 2
    return p

def bin(n):
    if n >= 1:
        bin(n // 2)
    print(n % 2, end='')

#def TestPrimaliteNaif(n):
    #transformer un entier en serie de bits, mettre à un les premiers, ce qui sera légèrement au dessus de la racine de ce dernier

print(bin(10))
