# from scipy.optimize import linprog
# z = [-9, -3]
# lhs = [[6, 3], [12, 19]]
# rhs = [34, 28]
# x1_bounds = (0, None)
# x2_bounds = (0, None)
#
# method='simplex'
#
# res = linprog(c=z, A_ub=lhs, b_ub=rhs,  bounds=(x1_bounds,x2_bounds))
#
# print('Scipy Optimize Optimal value:', res.fun, '\n x1, x2 :', res.x)
# print('\n')

from pulp import LpVariable, LpProblem, LpMaximize, LpStatus, value, LpMinimize

# declare your variables
x = LpVariable("x", 0, None)
y = LpVariable("y", 0, None)
z = LpVariable("z", 0, None)


# defines the problem
prob = LpProblem("problem", LpMaximize)

# defines the constraints
prob += x + y + z <= 100000
prob += y <= .15*x + .03*z

# defines the objective function to solve
prob += .15*x + .5*y + .16*z

# solve the problem
status = prob.solve()
LpStatus[status]

# print the results
print("Solution")
x = round(value(x),2)
y = round(value(y),2)
z = round(value(z),2)
print("x={}, y={}, z={}".format(x,y,z))
print("P=", 0.15*x + 0.5*y + 0.16*z)

