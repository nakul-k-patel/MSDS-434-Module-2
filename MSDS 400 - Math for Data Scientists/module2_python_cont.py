import numpy as np
from numpy.linalg import linalg, inv

rhs = [96, 87, 74]
rhs = np.matrix(rhs)
rhs = np.transpose(rhs)
print('\nRight Hand Side of Equation')
print(rhs)

A = [[1, 3, 4], [2, 1, 3], [4, 2, 1]]
A = np.matrix(A)
print('\nMatrix A')
print(A)

print('\nInverse of A')
IA = inv(A)
print(IA)


print('-'*80)
I = np.dot(IA, A)
I = np.rint(I)

print(I)
print(np.rint(np.dot(IA, rhs)))

