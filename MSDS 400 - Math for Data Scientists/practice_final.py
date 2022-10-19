# regression
# from scipy import stats
# x = [158, 251, 340, 350, 391, 190, 221]
# y = [32.8, 27.7, 14.8, 17.7, 10.3, 35.9, 42.4]
# slope, intercept, r_value, p_value, std_err = stats.linregress(x, y)
# print("slope = ", round(slope, 4))
# print("intercept = ", round(intercept, 4))
# print("correlation coefficient = ", round(r_value, 4))
# print(stats.linregress(x,y))
#
# solution = (25-round(intercept, 4))/round(slope, 4)
# print(solution)

# solve system of 3 variables
# import numpy as np
# from numpy.linalg import linalg, inv
#
# rhs = [64000, 1500, 3190]
# rhs = np.matrix(rhs)
# rhs = np.transpose(rhs)
# print('\nRight Hand Side of Equation')
# print(rhs)
#
# A = [[1, 1, 1],
#      [0, 1, -1],
#      [.04, .05, .06]]
# A = np.matrix(A)
# print('\nMatrix A')
# print(A)
#
# print('\nInverse of A')
# IA = inv(A)
# print(IA)
#
#
# print('-'*80)
# I = np.dot(IA, A)
# I = np.rint(I)
#
# print(I)
# print(np.rint(np.dot(IA, rhs)))

# linear programming
# from pulp import LpVariable, LpProblem, LpMaximize, LpStatus, value, LpMinimize
#
# # declare your variables
# x = LpVariable("x", 0, None)
# y = LpVariable("y", 0, None)
#
#
# # defines the problem
# prob = LpProblem("problem", LpMaximize)
#
# # defines the constraints
# prob += 2.40*x + .80*y <= 141
# prob += x <= 50
# prob += y <= 86
# prob += x + y <= 100
#
# # defines the objective function to solve
# prob += .039*x + .031*y
#
# # solve the problem
# status = prob.solve()
# LpStatus[status]
#
# # print the results
# print("Solution")
# x = value(x)
# y = value(y)
# print("x={}, y={}".format(round(x),round(y)))
# print("P=", round(.039*x + .031*y,2))

# bayes thereom

# PA = .9
# PDgA = .15
# PDgB = .25
# PB = .1
#
# PAgD = (PA*PDgA)/(PA*PDgA + PB*PDgB)
#
# print(round(PAgD,4))
#
# PA = .9
# PUgA = .85
# PUgB = .75
# PB = .1
#
# PBgD = (PB*PUgB)/(PB*PUgB + PA*PUgA)
#
# print(round(PBgD,4))

# marginal cost at a point
#
# from sympy import Symbol, diff
#
# x = Symbol('x')
#
# f = (7*x-8)/(4*x**2 + x)
# df = diff(f, x)
# print(float(df.subs({x:5})*100))

# instanteous rate of change

# from sympy import Symbol, diff, E
#
# t = Symbol('t')
#
# f = 500*E**(t*-.38)
# df = diff(f, t)
# print("After 3 years",round(float(df.subs({t:3})),2))
# print("After 6 years",round(float(df.subs({t:6})),2))
# print("After 10 years",round(float(df.subs({t:10})),2))

#
# from sympy import Symbol, diff, log as ln
#
# x = Symbol('x')
# f = 30.64 - 5.67*ln(x)
# df = diff(f, x)
#
# for i in [1971-1965, 1992-1965, 2009-1965]:
#     print(round(f.subs({x:i}),4))
#     print(round(df.subs({x: i}),4))

# extrema solver

# import sympy
# t = sympy.Symbol('t')
# f = (t**2+25)/4*t
#
# f_t = sympy.lambdify(t, f)
# f_diff = f.diff(t)
# print(f_diff)
# roots = sympy.solveset(sympy.Eq(f_diff, 0), t)
# print(f"The extrema for this equation are {roots}")
#
# for root in roots:
#     val_at_root = f_t(root)
#     print(f"After {root} years the value is {val_at_root}")

# solve area under curve with integral
# import sympy
# x = sympy.Symbol('x')
# function = 40.8 + 3.5*x - 0.891*x**2
#
# solution = round(sympy.integrate(function, (x,0,9)),0)
#
# print ("solution of intergral [0,9] =",solution)


# integral solving

# import sympy
# t = sympy.Symbol('t')
# function = (3*t+3)*(t**2+2*t+2)**(1/3)
#
# profit = round(sympy.integrate(function, (t,0,3))*1000,0)
# print(profit)

# exponentially distributed
# import sympy
#
# x = sympy.Symbol('x')
# l = 2
#
# expected_value = 1 / l  # Expected value formula for exponential distribution
# print(f"The expected proportion of an exponential distribution, in this case the bee dispersal, is {expected_value}")
#
# cdf_exp = 1 - sympy.exp(-l * x)  # CDF for exponential distribution
# cdf_exp_func = sympy.lambdify(x, cdf_exp)
# print(f"The probability that fewer than 35% are located within 2 meters is {cdf_exp_func(.30):.04}")

# # solve for extrema multivariate
#
# from sympy import symbols, S, nonlinsolve
#
# x, y = symbols('x, y')
#
# f_x_y = 2*x**2 + 6*y**2 + 4*x*y + 10
# partial_x = f_x_y.diff(x)
# partial_y = f_x_y.diff(y)
#
# results = nonlinsolve([partial_x, partial_y], x, y)
#
# print(f"The x and y value for critical points are {results}")
#
# # evaluate discriminant
#
# from sympy import lambdify, Abs
#
#
# def D(func, x_sym, y_sym, x_crit, y_crit):
#     # Calculate the discriminant for a given function
#     f_x_x = func.diff(x_sym, x_sym)
#     f_y_y = func.diff(y_sym, y_sym)
#     f_x_y = func.diff(x_sym, y_sym)
#
#     # Create callable functions for each of the derivitives we created
#     lambd_x_x = lambdify([x_sym, y_sym], f_x_x)
#     lambd_y_y = lambdify([x_sym, y_sym], f_y_y)
#     lambd_x_y = lambdify([x_sym, y_sym], f_x_y)
#
#     fxx_ab = lambd_x_x(x_crit, y_crit)
#     fyy_ab = lambd_y_y(x_crit, y_crit)
#     fxy_ab = lambd_x_y(x_crit, y_crit)
#
#     d = fxx_ab * fyy_ab - Abs(fxy_ab) ** 2
#
#     print(f"The discriminant of our critical value is {d}")
#
#     if d < 0:
#         print("This is a saddle point")
#     elif d > 0:
#         if fxx_ab < 0:
#             print("This is relative maxima")
#         else:
#             print("This is a relative minima")
#
# for result in list(results):
#     if result[0].is_real and result[1].is_real:  # Ignore any solutions that are not real numbers
#         print(f"Analyzing critical point {result}")
#         D(f_x_y, x, y, result[0], result[1])
#         print("With a result of:")
#         print(f_x_y.subs({x: result[0], y: result[1]}))

# solve multivariate with constraint (la grange)

# from sympy import symbols, nonlinsolve, nsimplify, expand, powsimp
#
# x, y, l = symbols('x, y, l', real=True)
#
# f_xy = 2*x**2 + 6*y**2 + 4*x*y + 10
# g_xy = x + y - 10  # Constraint is equal to zero when subtracting right side
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
#     print("Min cost is of x = {} and y ={} is {}".format(x_sol, y_sol, f_xy.subs({x: x_sol, y:y_sol})))