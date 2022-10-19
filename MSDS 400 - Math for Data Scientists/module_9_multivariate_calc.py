# partial derivatives

from sympy import symbols

x, y = symbols('x, y')
f_x_y = 4 * x**2 - 9 * x * y + 6 * y**3

partial_f_x = f_x_y.diff(x)  # Differentiate our equation with respect to x
print(f"Partial Derivitive of our equation with respect to x: {partial_f_x}")

partial_f_y = f_x_y.diff(y)  # Differentiate our equation with respect to y
print(f"Partial Derivitive of our equation with respect to y: {partial_f_y}")

partial_y_y = partial_f_y.diff(y)
partial_y_x = partial_f_y.diff(x)

print(f"Second derivitive fyy(x,y): {partial_y_y}")
print(f"Second derivitive fyx(x,y): {partial_y_x}")


# solve for critical points

from sympy import symbols, S, linsolve

x, y = symbols('x, y')

f_x_y = 6*x**2 + 6*y**2 + 6*x*y + 36*x - 5
partial_x = f_x_y.diff(x)
partial_y = f_x_y.diff(y)

results = linsolve([partial_x, partial_y], x, y)

print(f"The x and y value for critical points are {results}")

# evaluate discriminant

from sympy import lambdify, Abs


def D(func, x_sym, y_sym, x_crit, y_crit):
    # Calculate the discriminant for a given function
    f_x_x = func.diff(x_sym, x_sym)
    f_y_y = func.diff(y_sym, y_sym)
    f_x_y = func.diff(x_sym, y_sym)

    # Create callable functions for each of the derivitives we created
    lambd_x_x = lambdify([x_sym, y_sym], f_x_x)
    lambd_y_y = lambdify([x_sym, y_sym], f_y_y)
    lambd_x_y = lambdify([x_sym, y_sym], f_x_y)

    fxx_ab = lambd_x_x(x_crit, y_crit)
    fyy_ab = lambd_y_y(x_crit, y_crit)
    fxy_ab = lambd_x_y(x_crit, y_crit)

    d = fxx_ab * fyy_ab - Abs(fxy_ab) ** 2

    print(f"The discriminant of our critical value is {d}")

    if d < 0:
        print("This is a saddle point")
    elif d > 0:
        if fxx_ab < 0:
            print("This is relative maxima")
        else:
            print("This is a relative minima")


# Call our new function and pass in the values
D(f_x_y, x, y, -4, 2)

# multiple critical points

from sympy import symbols, S, nonlinsolve

x, y = symbols('x, y', real=True)

f_x_y = 9*x*y - x**3 - y**3 - 6
partial_x = f_x_y.diff(x)
partial_y = f_x_y.diff(y)

# Get nonlinear solution and remove imaginary numbers
results = nonlinsolve([partial_x, partial_y], [x, y])

print(f"The x and y value for critical points are {results}")

for result in list(results):
    if result[0].is_real and result[1].is_real:  # Ignore any solutions that are not real numbers
        print(f"Analyzing critical point {result}")
        D(f_x_y, x, y, result[0], result[1])

# lagrange multiplies

from sympy import symbols, nonlinsolve, nsimplify, expand, powsimp

x, y, l = symbols('x, y, l', real=True)

f_xy = x * y
g_xy = x * y + 20 * y + 20 * x + 474000 - 500000  # Constraint is equal to zero when subtracting right side

# Implement lagrange function and solve system
f_xyl = f_xy - l *g_xy
f_xyl_x = f_xyl.diff(x)
f_xyl_y = f_xyl.diff(y)
f_xyl_l = f_xyl.diff(l)

results = nonlinsolve([
    f_xyl_x,
    f_xyl_y,
    f_xyl_l,
], [x, y, l])

# Analyze each of the solutions
for sol in list(results):
    x_sol, y_sol, l_sol = sol

    x_sol = x_sol.evalf()  # Evaluate the value so we're not getting sqrt equation
    y_sol = y_sol.evalf()
    print(f"Max value of x is {x_sol}")
    print(f"Max value of y is {y_sol}")

    print(f"Max area is of ({x_sol}, {y_sol}) is {x_sol * y_sol}")