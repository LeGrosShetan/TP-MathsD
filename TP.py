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


def TestFernat(n):
    return ExpMod(2, n - 1, n) == 1


def sqrt(n):
    if n <= 1:
        return 1
    i = 1
    while (i * i < n):
        i += 1
    return i


def TestPrimaliteNaif(n):
    indice = sqrt(n)
    step = 1
    if (n % 2 == 1):
        step = 2
        if (indice % 2 == 0):
            indice -= 1
    while (indice > 0):  # Marche, car dans le pire des cas, renvoie 1
        if (n % indice == 0):
            return indice
        indice -= step


print(sqrt(100))
# print(Square(100, 9, 10))