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
    d=2
    r=n%d
    racine = sqrt(n)
    if n==2:
        return True
    if r==0:
        return False
    d=3
    while d<= racine:
        r=n%d
        if r==0:
            return False
        d+=2
    return True


def ratioPrime(i):
    val1 = ExpMod(2, i, 2147483649)
    val2 = ExpMod(2, i + 1, 2147483649)
    count = 0
    for j in range(val1, val2, 1):
        if (TestPrimaliteNaif(j)):
            count += 1

    ratio = count / val1
    return ratio

def ratioFernat(i):
    val1 = ExpMod(2, i, 2147483649)
    val2 = ExpMod(2, i + 1, 2147483649)
    count = 0
    for j in range(val1, val2, 1):
        if (TestFernat(j)):
            count += 1

    ratio = count / val1
    return ratio

def tauxErreurFernat(i):
    val1=ratioPrime(i)
    val2=ratioFernat(i)
    taux=(val2-val1)/val1
    return taux


print(tauxErreurFernat(16))

