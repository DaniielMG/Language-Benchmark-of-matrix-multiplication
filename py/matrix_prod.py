import random

def random_matrix(n, seed=None):
    if seed is not None:
        random.seed(seed)
    return [[random.random() for _ in range(n)] for _ in range(n)]

def zero_matrix(n):
    return [[0.0 for _ in range(n)] for _ in range(n)]

def matmul_naive(A, B):
    n = len(A)
    C = zero_matrix(n)
    for i in range(n):
        for j in range(n):
            s = 0.0
            for k in range(n):
                s += A[i][k] * B[k][j] 
            C[i][j] = s
    return C
