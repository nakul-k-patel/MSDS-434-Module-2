from sympy import integrate, Symbol, lambdify, E

x = Symbol('x')
y = Symbol('y')
mean = 6
m = 1 / mean
f = m * E ** (-m * x)  # define formula
months = [1, 2, 3, 6, 12]


def int_solve(start, end, formula):
    formula_int = integrate(formula, x)
    solve_form = lambdify(x, formula_int)
    sol_a = solve_form(start)
    sol_b = solve_form(end)
    solution = sol_b - sol_a
    return solution


for i in months:
    right_set_kpi = round(int_solve(0, i, f) * 25, 2)
    print("For {} month completion rate, the KPI should be {}%".format(i,
                                                                       right_set_kpi))
