#!python


def sievePrimes(maxTry):
    isPrime= [True for i in range(maxTry)]
    isPrime[:2] = [False, False]
    i = 2
    step = 2

    while step < maxTry:
        while step < maxTry and not isPrime[step]:
            step += 1
        i = step * 2 
        while i < maxTry:
            isPrime[i] = False
            i += step
        step += 1
    return isPrime

isPrime = sievePrimes(1000000)

def genPrimes():
    for i, p in enumerate(isPrime):
        if p: yield i

def cycles(num):
    L = list(str(num))
    return [int(''.join(L[i:] + L[:i])) for i in range(len(L))]

def circular(num):
    return all(isPrime[n] for n in cycles(num))

def count(iterable):
    c = 0
    for i in iterable:
        c += 1
    return c

print(count(n for n in genPrimes() if circular(n)))
