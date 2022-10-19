# print('Question 1")
#
# import matplotlib.pyplot as plot
# from numpy import linspace
#
# x = linspace(0, 1000, 1000)
# y1 = 50000+18*x
# y2 = 130*x
#
# plot.xlabel('Pairs of Shoes')
# plot.ylabel('Dollars')
# plot.plot(x, y1, 'g')
# plot.plot(x, y2, 'b')
# plot.legend(['Cost = 50000+18x', 'Revenue = 130x'])
# plot.title('Cost and Revenue for Crossfit Nano XXXII')
# plot.show()

print("-"*80)
print("Question 2")

import numpy as np
from numpy.linalg import linalg, inv

rhs = [17500, 0, 1495]
rhs = np.matrix(rhs)
rhs = np.transpose(rhs)

A = [[1, 1, 1],
     [-1, 0, 2],
     [.11, .07, .05]]

A = np.matrix(A)
IA = inv(A)

print(np.rint(np.dot(IA, rhs)))

print("-"*80)
print("Question 3")

print("-"*80)
print("Question 4")

import numpy as np
from numpy.linalg import linalg, inv

A = [[6, 8, 1],
     [6, 4, 1],
     [5, 7, 1]]
B = [[4, 3],
     [4, 5],
     [2, 2]]

cost_per_batch = np.dot(A, B)

total_cost = 0
for i in range(0, 3):
    add_cost = cost_per_batch[i][1] * 100
    total_cost += add_cost

print(total_cost)

print("-"*80)
print("Question 5")

import numpy as np
from numpy.linalg import linalg, inv

rhs = [28000, 750000, 400000]
rhs = np.matrix(rhs)
rhs = np.transpose(rhs)

A = [[1, 1, 1],
     [48, 36, 24],
     [24, 36, 12]]

A = np.matrix(A)
IA = inv(A)

print(np.rint(np.dot(IA, rhs)))

print("-"*80)
print("Question 6")

from pulp import LpVariable, LpProblem, LpMaximize, LpStatus, value, LpMinimize

# declare your variables
o = LpVariable("o", 0, None)
n = LpVariable("n", 0, None)

# defines the problem
prob = LpProblem("problem", LpMaximize)

# defines the constraints
prob += 6*o + 2*n <= 18000
prob += 3*o + 4*n <= 12000

# defines the objective function to solve
prob += .25*o + .16*n

# solve the problem
status = prob.solve()
LpStatus[status]

# print the results
print("Solution")
o = round(value(o), 0)
n = round(value(n), 0)
print("old process = {} liters, new process = {}".format(o,n))
print("Profit = ", round(.25*o + .16*n, 2))

print("-"*80)
print("Question 7")

from pulp import LpVariable, LpProblem, LpMaximize, LpStatus, value, LpMinimize

# declare your variables
t = LpVariable("t", 10, None)
p = LpVariable("p", 1, None)

# defines the problem
prob = LpProblem("problem", LpMinimize)

# defines the constraints
prob += 30 <= p+t
prob += p+t <= 45
prob += t <= 3/2 * p

# defines the objective function to solve
prob += 2400*p + 1100*t

# solve the problem
status = prob.solve()
LpStatus[status]

# print the results
print("Solution")
t = round(value(t), 0)
p = round(value(p), 0)
print("TAs = {}, Teachers = {}".format(t, p))
print("Cost = ", round(2400*p + 1100*t, 2))

print("-"*80)
print("Question 8")

from pulp import LpVariable, LpProblem, LpMaximize, LpStatus, value, LpMinimize

# declare your variables
x = LpVariable("x", 0, None)
y = LpVariable("y", 0, None)
z = LpVariable("z", 0, None)

# defines the problem
prob = LpProblem("problem", LpMinimize)

# defines the constraints
prob += 4*x + y + 10*z >= 10
prob += 3*x + 2*y + z >= 12
prob += 4*y + 5*z >= 20

# defines the objective function to solve
prob += .06*x + .08*y + .01*z

# solve the problem
status = prob.solve()
LpStatus[status]

# print the results
print("Solution")
x = round(value(x), 0)
y = round(value(y), 0)
z = round(value(z), 0)
print("# of Pill 1 = {}, # of Pill 2 = {}, # of Pill 3 = {}".format(x, y, z))
print("Cost = ", round(.06*x + .08*y + .01*z, 2))

print("-"*80)
print("Question 9")

from pulp import LpVariable, LpProblem, LpMaximize, LpStatus, value, LpMinimize

# declare your variables
b = LpVariable("b", 0, None)
t = LpVariable("t", 0, None)
s = LpVariable("s", 0, None)

# defines the problem
prob = LpProblem("problem", LpMaximize)

# defines the constraints
prob += b + t + s <= 210
prob += b >= 2*t
prob += s >= 30

# defines the objective function to solve
prob += 200*b + 1000*t + 300*s

# solve the problem
status = prob.solve()
LpStatus[status]

# print the results
print("Solution")
b = round(value(b), 0)
t = round(value(t), 0)
s = round(value(s), 0)
print("DVD Players = {}, Speakers  = {}, TVs = {}".format(b, t, s))
print("Revenue = ", round( 200*b + 1000*t + 300*s, 2))

print("-"*80)
print("Question 10")

print((.25*.02)/(.25*.02+.75*.05))
