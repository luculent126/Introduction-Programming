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

def multiplyMatrix(a, b):
    m, n, p = len(a), len(a[0]), len(b[0])
    c = [[0]*p for i in range(m)]
    for x in range(m):
        for y in range(m):
            sum = 0
            for z in range(m):
                sum = sum + a[x][z] * b[z][y]
            c[x][y] = sum
    return c

import random
M = int(input('M = '))
N = int(input('N = '))
P = int(input('P = '))
K = int(input('K = '))
print()
A = makeMatrix(M, N, K)
print('행렬 A')
printMatrix(A)
print()
B = makeMatrix(N, P, K)
print('행렬 B')
printMatrix(B)
print()
print('A * B')
C = multiplyMatrix(A, B)
printMatrix(C)
