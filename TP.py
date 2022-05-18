import random
import time

def EuclideEtendu(a, b):
    if (b==0):
        return(a,1,0)

    res = EuclideEtendu(b, a%b)

    dp = res[0]
    xp = res[1]
    yp = res[2]

    return (dp,yp,xp - a/byp)

def ExpMod(a,k,n):
    p = 1
    while k > 0:
        if k%2 != 0:
            p = (p a)%n
        a = (a*a)%n
        k = k//2
    return p

def TestFernat(n):
    return ExpMod(2, n - 1, n) == 1

def bin(n):
    q = -1
    res = ''
    while q != 0:
        q = n // 2
        r = n % 2
        res = r + res
        n = q
    return res

def TestPrimaliteNaif(n):
    #transformer un entier en serie de bits, mettre à un les premiers, ce qui sera légèrement au dessus de la racine de ce dernier

print(ExpMod(2,6,7))
