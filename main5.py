import numpy as np

# 1

a = np.arange(4, 81, 4)
print(a)

# 2

a = np.arange(1.0, 2.0, 0.12, dtype='float')
b = a.astype('int32')
print(b)
print(b.shape)
print(b.dtype)
print(b.ndim)

# 3

def fun(n: int):
    m = np.identity(n, int)
    for i in range(n):
        for j in range(n):
            m[i, j] = 2 ** (i + j)
    return m

print(fun(5))

# 4

def fun(n, m):
    a = np.arange(m)
    for i in range(m):
        a[i] = n ** (i + 1)
    return a

print(fun(3, 5))

# 5

def fun(n: int):
    a = [n - i for i in range(n)]
    return np.diag([i for i in a],2)


print(fun(5))









