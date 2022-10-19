# Question 1

# from sympy import symbols, lambdify
#
# x, y = symbols('x, y')
#
# f = 6*x - 3*y + 4
#
# print("a) f(1,1) =",f.subs({x:1, y:1}))
# print("b) f(3, -1) =",f.subs({x:3,y:-1}))
# print("c) f(4,0) =",f.subs({x:4,y:0}))
# print("d) f(-4,4) =",f.subs({x:-4,y:4}))

# Question 4

# from sympy import diff, symbols, log as ln
#
# x, y = symbols('x, y')
# f = y*ln(4*x+y)
# f_x = diff(f, x)
# f_y = diff(f, y)
#
# print(f_x)
# print(f_y)4

# Question 5

# from sympy import diff, symbols, log as ln
#
# x, y = symbols('x, y')
# f = 3*x**4 -6*x**2*y**2 - y**3
# f_x = diff(f, x)
# f_y = diff(f, y)
# f_x_x = diff(f_x, x)
# f_x_y = diff(f_x, y)
#
# print("f_x:", f_x)
# print("f_y:", f_y)
# print("f_x_x:", f_x_x)
# print("f_x_y:", f_x_y)

# Question 6 - Tangent Plan
#
# from sympy import diff, symbols, E
#
# x, y = symbols('x, y')
# f = 3 * E ** (x ** 2 - 6 * y)
# x0 = 12
# y0 = 24
#
# f_x = diff(f, x)
# f_y = diff(f, y)
#
# # tangent plane formula
#
# z = f.subs({x: x0, y: y0}) + f_x.subs({x: x0, y: y0})*(x-x0) + f_y.subs({x: x0, y: y0})*(y-y0)
#
# print(z)

# Question 7
#
# from sympy import symbols, sqrt
#
# x, y = symbols('x, y')
#
# f = 4*sqrt((x*y)/2)
#
# print(float(f.subs({x: 2.19, y: 4.12})))

# Question 8

# from sympy import symbols, diff, E
#
# x, y, t = symbols('x, y, t')
# fz = x*E**(4*y)
# fx = t**4
# fy = -1 +4*t
# d_z_x = diff(fz, x)
# d_x_t = diff(fx, t)
# d_z_y = diff(fz, y)
# d_y_t = diff(fy, t)
#
# d_z_t = d_z_x*d_x_t + d_z_y*d_y_t
# print(d_z_t.subs({x: fx, y: fy}))
#
# x = t**4
# y = -1 +4*t
# z = x*E**(4*y)
#
# print(diff(z, t))

# Question 9
#
# from sympy import symbols
#
# p, t = symbols('p, t')
#
# v = 8.31*t/p
# current_t = 280
# current_p = 20
# dt = .05
# dp = .06
#
# dv = v.subs({t: current_t+dt, p: current_p+dp}) - v.subs({t: current_t, p: current_p})
# print(dv)

# Question 10

# from sympy import symbols, S, nonlinsolve, lambdify, Abs
#
# x, y = symbols('x, y', real=True)
#
# f_x_y = 3*x**4 + 3*y**4 - 2*x*y
# partial_x = f_x_y.diff(x)
# partial_y = f_x_y.diff(y)
#
# # Get nonlinear solution and remove imaginary numbers
# results = nonlinsolve([partial_x, partial_y], [x, y])
#
# print(f"The x and y value for critical points are {results}")
# for result in list(results):
#     if result[0].is_real and result[1].is_real:  # Ignore any solutions that are not real numbers
#         print(float(f_x_y.subs({x: result[0], y: result[1]})))
#         print("-"*10)

# Question 11
#
# from sympy import symbols, S, nonlinsolve
#
# x, y = symbols('x, y')
#
# f_x_y = x**3 + y**3 + 21*x**2 - 24*y**2 - 1
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
#
# minimum = f_x_y.subs({x: 0, y: 16})
# maximum = f_x_y.subs({x: -14, y: 0})
#
# print(minimum)
# print(maximum)

# Question 12

# from sympy import symbols, S, nonlinsolve
#
# x, y = symbols('x, y')
#
# f_x_y = 2*x + 7*y - 9*x**2 - 8*y**2 - 6*x*y
# partial_x = f_x_y.diff(x)
# partial_y = f_x_y.diff(y)
#
# results = nonlinsolve([partial_x, partial_y], x, y)
# print(partial_x)
# print(partial_y)
# print(f"The x and y value for critical points are {results}")

# Question 13
#
# from sympy import symbols, nonlinsolve
#
# w, l, h = symbols('w, l, h')
#
# c = 8 * w * l + 10 * w * h + 4 * w * h + 8 * l * h
#
# partial_w = c.diff(w)
# partial_h = c.diff(h)
# partial_l = c.diff(l)
#
# results = nonlinsolve([partial_w, partial_h, partial_l], w, h, l)
# print(f"The w, h, and l values for critical points are {results}")
#
# from sympy import symbols, nonlinsolve, nsimplify, expand, powsimp
#
# w, h, d, l = symbols('w, h, d, l', real=True)
#
# c = 8 * w * d + 11 * w * h + 3 * w * h + 6 * d * h
# g = w*d*h - 350 # Constraint is equal to zero when subtracting right side
#
# # Implement lagrange function and solve system
# cl = c - l * g
# cl_w = cl.diff(w)
# cl_d = cl.diff(d)
# cl_h = cl.diff(h)
# cl_l = cl.diff(l)
#
# results = nonlinsolve([
#     cl_w,
#     cl_h,
#     cl_d,
#     cl_l
# ], [w, h, d, l])
#
# # Analyze each of the solutions
# for sol in list(results):
#     w_sol, h_sol, d_sol , l_sol = sol
#
#     w_sol = w_sol.evalf()  # Evaluate the value so we're not getting sqrt equation
#     h_sol = h_sol.evalf()
#     d_sol = d_sol.evalf()
#     print(f"Max value of w is {w_sol}")
#     print(f"Max value of h is {h_sol}")
#     print(f"Max value of d is {d_sol}")
#
#     print(f"Max volume is of ({w_sol}, {h_sol}, {d_sol}) is {w_sol * d_sol * h_sol}")

# Question 14
# from sympy import symbols, nonlinsolve, nsimplify, expand, powsimp
#
# x, y, l = symbols('x, y, l', real=True)
#
# f_xy = 2*x**2 + x*y + 8*y**2 + 2400
# g_xy = x + y - 1800  # Constraint is equal to zero when subtracting right side
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

# Question 15

from sympy import symbols, Derivative
from sympy.solvers import solve
from mpmath import pi

p, r = symbols('p r')
p = 1080 - 9*r

# Plug in the equation of p in the z equation
z = 100*(1080 - 9*r)**0.75*r**0.25
dz = Derivative(z, r).doit()

# To calculate the maximum we have to find where dz = 0
# We will use the equation of dz above and the sympy solve function to
# solve for r
r_value = solve(dz, r)
print("r =", round(r_value[0]))

# Calculate p by substituting the value for r
p_value = p.subs({r:r_value[0]})
print("p =",round(p_value))

# Calculate z by substituting the value for r
z_value = z.subs({r:r_value[0]})
print("z = ",round(z_value))