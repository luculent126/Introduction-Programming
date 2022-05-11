def makeMatrix(m, n, k):
    a = []
    for i in range(m):
        b = []
        for j in range(n):
                b.append(random.randint(0, k))
        a.append(b)
    return a

def printMatrix(a):
    m, n = len(a), len(a[0])
    for i in range(m):
        for j in range(n):
            print(a[i][j], end=' ')
        print()

def addMatrix(a, b):
    m, n = len(a), len(a[0])
    c = [[0]*n for i in range(m)]
    x = 0
    while x < m:
        y = 0
        sum = 0
        while y < m:
            sum = a[x][y] + b[x][y]
            c[x][y] = sum
            y = y + 1
        x = x + 1
    return c

import random
M = int(input('M = '))
N = int(input('N = '))
K = int(input('K = '))
print()
A = makeMatrix(M, N, K)
print('행렬 A')
printMatrix(A)
print()
B = makeMatrix(M, N, K)
print('행렬 B')
printMatrix(B)
print()
print('A + B')
C = addMatrix(A, B)
printMatrix(C)
