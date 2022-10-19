from sympy import diff, Symbol, sqrt, lambdify


# def f(x):
#     function = x**3 - 4*x
#     return function
#
#
# slope = (f(5) - f(2)) / (5 - 2)
# print(slope)

x = Symbol('x')
f = 4*(x-3)**(2/3)
f_prime = diff(f, x)
print(f_prime)
f_double_prime = diff(f_prime, x)
print(f_double_prime)

sol_f_prime = lambdify(x, f_prime)


for i in [-1, 10]:
    print(i)
    print(sol_f_prime(i))()