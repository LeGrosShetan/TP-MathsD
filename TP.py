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
    if(n%2 == 0):
        return False
    if(indice%2 == 0):
        indice -= 1
    while(indice > 0): #Marche, car dans le pire des cas, renvoie 1
        if(n%indice == 0):
            return (indice == 1)
        indice -= 2

def ratioPrime(i):
    val1=ExpMod(2,i,2147483649)
    val2=ExpMod(2,i+1,2147483649)
    count1=1
    count2=1
    for j in range (3,val1,2):
        if(TestPrimaliteNaif(j)):
            count1 += 1
    for k in range (3,val2,2):
        if (TestPrimaliteNaif(k)):
            count2 += 1

    ratio=(count2-count1)/(val2-val1)
    return ratio



print(ratioPrime(30))

