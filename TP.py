#made by Schwaederle Gaetan and Poiret Maxime

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


def TestFermat(n):
    return ExpMod(2, n - 1, n) == 1


def sqrt(n):
    if n <= 1:
        return 1
    i = 1
    while (i * i < n):
        i += 1
    return i


def PrimaliteNaif(n):
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


def primesInRange(x,y):
    prime_list = []
    for n in range(x, y):
        isPrime = PrimaliteNaif(n)
        if isPrime:
            prime_list.append(n)
    return prime_list

def FermatInRange(x,y):
    prime_list = []
    for n in range(x, y):
        isPrime = TestFermat(n)
        if isPrime:
            prime_list.append(n)
    return prime_list

def ratioPrime(i):
    val1 = 2 ** i
    val2 = 2 ** (i + 1)
    liste=primesInRange(val1,val2)
    ratio = len(liste) / val1
    return ratio

def ratioFermat(i):
    val1 = 2**i
    val2 = 2**(i + 1)
    liste = FermatInRange(val1, val2)
    ratio = len(liste) / val1
    return ratio

def tauxErreurFermat(i):
    val1 = 2 ** i
    val2 = 2 ** (i + 1)
    list1=primesInRange(val1,val2)
    list2=FermatInRange(val1,val2)
    len1=len(list1)
    len2=len(list2)
    taux=abs((len2-len1))/len1
    return taux

def GenPremiers(k):
    i=2**k
    liste = primesInRange(2,i)
    return random.choice(liste)

def PhiToFact(n,phin):
    p=1
    q=n+1-phin-p
    while p*q != n:
        p+=1
        q = n + 1 - phin - p
    return p,q
#faire la deduction de l'exo8

#faire exo 11, 12, 13, 14, 15


print(tauxErreurFermat(20))


