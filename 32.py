#!python

# unsolved

def digits(num):
    return [ord(n) - ord('0') for n in str(num)]

def multiplicand(a, b):
    L = digits(a) + digits(b) + digits(a * b)
    return len(L) == 9 and len(set(L)) == 9

s = {(i, j) for i in range(10, 100) for j in range(100, 1000) if multiplicand(i, j)}
t = {(i, j) for i in range(0, 10) for j in range(1000, 10000) if multiplicand(i, j)}
L = sorted(s.union(t))
print(sum(i * j for i, j in L))
print(L)
