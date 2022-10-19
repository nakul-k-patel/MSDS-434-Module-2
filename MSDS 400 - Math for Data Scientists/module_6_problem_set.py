# # f(x) from left (negative)
# def fl(x):
#     fl = (-7/(x+8))
#     return fl
#
# # f(x) from right (positive)
# def fr(x):
#     fr = (112/(x-9))
#     return fr
#
# x = -7
#
# left_limit = fl(x)
# right_limit = fr(x)
#
# print("Left limit is:", left_limit)
# print("Right limit is:", right_limit)

# def velocity(s, t):
#     h1 = -3*s**2 + 6*s + 63
#     h2 = -3*(s+t)**2 + 6*(s+t) + 63
#     velocity = (h2-h1)/t
#     return velocity
#
# s = 1
# t = .001
# print('Average velocity is {}'.format(velocity(s, t)))

# getting y_prime

# from sympy import Symbol, Derivative, log as ln, E, diff, sin, pi
#
# x = Symbol('x')
#
#
# f = 3*sin((pi/3)*x + ((4*pi)/3))+2
# point = 5
#
# f_prime = diff(f, x)
# value = f.doit().subs({x: point})
# rate_of_change = f_prime.doit().subs({x: point})
#
# print("f' is {}".format(f_prime))
# print('The value of f(x) at x={} is {}'.format(point, value))
# print('The rate of change of f(x) at x={} is {}'.format(point, rate_of_change))




