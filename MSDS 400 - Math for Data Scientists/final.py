# from sympy import integrate, Symbol, lambdify, E
#
# x = Symbol('x')
# mean = 75
# m = 1 / mean
# f = m * E ** (-m * x)
#
# print(f)
#
# def int_solve(start, end, formula):
#     formula_int = integrate(formula, x)
#     solve_form = lambdify(x, formula_int)
#     sol_a = solve_form(start)
#     sol_b = solve_form(end)
#     solution = sol_b - sol_a
#     return solution
#
# print("the probability that the call is no more than 59 seconds",round(int_solve(0, 59, f),4))
# print("the probability that the call is more than 468 seconds",round(1-int_solve(0, 468, f),4))

# from sympy import symbols, nonlinsolve, nsimplify, expand, powsimp
#
# x, y, l = symbols('x, y, l', real=True)
#
# f_xy = -x**2 - y**2 + 2*x + 6*y
# g_xy = x + y - 4  # Constraint is equal to zero when subtracting right side
#
# # Implement lagrange function and solve system
# f_xyl = f_xy - l *g_xy
# f_xyl_x = f_xyl.diff(x)
# f_xyl_y = f_xyl.diff(y)
# f_xyl_l = f_xyl.diff(l)
#
# results = nonlinsolve([
#     f_xyl_x,
#     f_xyl_y,
#     f_xyl_l,
# ], [x, y, l])
#
# # Analyze each of the solutions
# for sol in list(results):
#     x_sol, y_sol, l_sol = sol
#
#     x_sol = x_sol.evalf()  # Evaluate the value so we're not getting sqrt equation
#     y_sol = y_sol.evalf()
#     print("Max profit is of x = {} and y ={} is {}".format(x_sol, y_sol, f_xy.subs({x: x_sol, y:y_sol})*100))

# import matplotlib.pyplot
# from matplotlib.pyplot import *
# import numpy
# from numpy import linspace
# x = linspace(0,12,100)
# y = (x**2+25)/(4*x)
# title('Plot of Linear Equation  ')  # Note how the title appears.
# plot(x,y)
# show()

import sympy
t = sympy.Symbol('t')
f = (t**2+25)/(4*t)

f_t = sympy.lambdify(t, f)
f_diff = f.diff(t)
print(f_diff)
roots = sympy.solveset(sympy.Eq(f_diff, 0), t)
print(f"The extrema for this equation are {roots}")

for root in roots:
    val_at_root = f_t(root)
    print(f"After {root} months the value is {val_at_root}")