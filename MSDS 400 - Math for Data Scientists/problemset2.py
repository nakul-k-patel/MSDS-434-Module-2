import numpy as np
from numpy.linalg import linalg, inv

# below for solving equations with inverses

rhs = [100000, 19000, 0]
rhs = np.matrix(rhs)
rhs = np.transpose(rhs)

A = [[1, 1, 1],
     [.15, .5, .16],
     [-.15, 1, -.03]]
IA = inv(A)

I = np.dot(A, IA)
I = np.rint(I)

print("""Identity Martrix Check
{}""".format(I))

solution = np.dot(IA, rhs)
solution = np.rint(solution)
print("Solution is : {}".format(solution))

# below for determinent and solutions 3 variables
# a1 = 5
# b1 = -3
# c1 = -4
# d1 = 3
#
# a2 = 1
# b2 = -5
# c2 = 3
# d2 = -24
#
# a3 = -1
# b3 = 4
# c3 = -2
# d3 = 18
#
#
# D = a1*b2*c3 + b1*c2*a3 + c1*a2*b3 - a3*b2*c1 - b3*c2*a1 - c3*a2*b1
# print('D is {}'.format(D))
#
# Dx = d1*b2*c3 + b1*c2*d3 + c1*d2*b3 - d3*b2*c1 - b3*c2*d1 - c3*d2*b1
# print('Dx is {}'.format(Dx))
#
# Dy = a1*d2*c3 + d1*c2*a3 + c1*a2*d3 - a3*d2*c1 - d3*c2*a1 - c3*a2*d1
# print('Dy is {}'.format(Dy))
#
# Dz = a1*b2*d3 + b1*d2*a3 + d1*a2*b3 - a3*b2*d1 - b3*d2*a1 - d3*a2*b1
# print('Dz is {}'.format(Dz))
#
# x = Dx/D
# y = Dy/D
# z = Dz/D
#
# print('x = {}, y = {} , z = {}'.format(x,y,z))
