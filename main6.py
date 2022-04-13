import numpy as np

#1

# A = np.array([1, 3, 2])
# B = np.array([7, 5, 7])
# C=A*2
# D=B*2
# print(C)
# print(D)

#2

# A=np.array([[1, 2, 3],[4, 5, 6],[1, 2, 6]])
# B=np.array([[6, 2, 3,44],[3, 5, 3,4],[4, 2, 3,6],[8, 2, 21,5]])
#
# c=np.min(A)
# d=np.min(B)

#3

# A = np.array([1, 3, 2])
# B = np.array([7, 5, 7])
#
# C=np.dot(A,B)
# print(C)

#4

# A = np.array([1, 3, 2])
# B = np.array([1, 3, -72])
#
# c=A*2
# d=B*5
# print(c)
# print(d)

#5

X1=np.array([[1, 2, 3],[4, 5, 6]])
#
a=np.sin(X1)
# print(a)

#6
#
X2=np.array([[1, 2, 3],[4, 5, 6]])
#
b=np.cos(X2)
# print(a)

#7

# a = np.array([[1, 2, 3], [4, 5, 6]])
# b = np.sin(a)
# v = np.array([[5, 6, 7], [8, 9, 10]])
# d = np.cos(v)
# e = b + d
# print(e)

#8

# a = np.array([[3, 3, 3], [4, 4, 4], [5, 5, 5]])
# for x in a:
#     print(x)

#9

# a = np.array([[3, 3, 3], [4, 4, 4], [5, 5, 5]])
# for x in a.flat:
#     print(x)

#10

x = np.arange(81).reshape(9, 9)
print(x)
a = x.reshape(81, 1)
print(a)
b = x.reshape(1, 81)
print(b)
c = x.reshape(3, 27)
print(c)
d = x.reshape(27, 3)
print(d)
