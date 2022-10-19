# from sympy import integrate, Symbol, lambdify, sqrt, E

# solve definite integrals
x = Symbol('x')
f = 2*E**(-2*x) # define formula
a = 0 # define start
b = 50/60 # define b
constant = 0 # define existing constant if known

def int_solve(start, end, formula):
    formula_int = integrate(formula, x)
    solve_form = lambdify(x, formula_int)
    sol_a = solve_form(start)
    sol_b = solve_form(end)
    solution = sol_b - sol_a
    return solution


f_int = integrate(f, x)
print(f_int)
print(round(int_solve(a, b, f)+constant, 3))

get indefinite integrals

x = Symbol('x')
f = x * E**(2 * x**2)
f_int = integrate(f, x)
print(f_int)

sandbox
x = Symbol('x')
m = 1/3.75
f = m*E**(-m*x) # define formula
a = 0 # define start
b = .5 # define b
c = 1
constant = 0 # define existing constant if known

def int_solve(start, end, formula):
    formula_int = integrate(formula, x)
    solve_form = lambdify(x, formula_int)
    sol_a = solve_form(start)
    sol_b = solve_form(end)
    solution = sol_b - sol_a
    return solution


f_int = integrate(f, x)
print(f_int)
print(round(int_solve(a, b, f)*320*100 + int_solve(b, c, f)*320*100/2, 2))

# normal distribution  and percentile

# import statistics as stat
# from sympy import erf
#
# mean = 253
# std_dev = 49
# critical_point = 222
# z_score = round(stat.NormalDist(mu=mean, sigma=std_dev).zscore(critical_point), 2)
# print('Z score = {}'.format(z_score))
#
#
# def percentage(z):
#     return .5 * (erf(z / 2 ** .5) + 1)
#
#
# print(round(percentage(z_score) * 100, 1), '% under {}'.format(critical_point))
# print(100 - round(percentage(z_score) * 100, 1), '% over {}'.format(critical_point))

