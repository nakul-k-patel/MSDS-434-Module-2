import numpy as np
from numpy.linalg import linalg, inv
import timeit
import sympy as sym

start = timeit.default_timer()

rhs = [100000, 19000, 0]
rhs = np.matrix(rhs)
rhs = np.transpose(rhs)

A = [[1, 1, 1],
     [.15, .5, .16],
     [-.15, 1, -.03]]
IA = inv(A)

solution = np.dot(IA, rhs)
solution = np.rint(solution)
print("Solution is : {}".format(solution))


stop = timeit.default_timer()

print('Time: ', stop - start)

start = timeit.default_timer()


sym.init_printing()
x,y,z = sym.symbols('x,y,z')
solns = sym.solve([
     x + y + z - 100000,
    .15 * x + .5 * y + .16 * z - 19000,
    -0.15* x + .5 * y - .03*z],
    [x, y, z])

print(f"x: {solns[x]}, y: {solns[y]}, z: {solns[z]}")

stop = timeit.default_timer()

print('Time: ', stop - start)