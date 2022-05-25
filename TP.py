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

def Square(n,i,j):
    mid=(i+j)/2
    mul=mid*mid
    if mul==n or abs(mul-n)<0.00001:
        return mid
    elif mul<n:
        return Square(n,mid,j)
    else:
        return Square(n,i,mid)

def sqrt(n):
    i=1
    found = False
    while not found:
        if i*i >n:
            found = True
            return i
        elif i*i>n:
            res = Square(n,i-1,i)
            found = True
            return res
        i=i+1

#def TestPrimaliteNaif(n):
    #transformer un entier en serie de bits, mettre à un les premiers, ce qui sera légèrement au dessus de la racine de ce dernier

print(sqrt(100))
