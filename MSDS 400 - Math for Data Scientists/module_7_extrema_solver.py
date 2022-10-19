from sympy import Symbol, diff, solve, lambdify

#assign symbols
x = Symbol('x')

# define function
f = (x**2+25)/(4*x)

# define end points
min_end_point = 1
max_end_point = 12

# find derivative
f_prime = diff(f, x)
print(f_prime)
# identifies all relevant extrema
extrema = solve(f_prime, x)

for i in extrema:
    if min_end_point is not None:
        if i < min_end_point:
            extrema.remove(i)
    if max_end_point is not None:
        if i > max_end_point:
            extrema.remove(i)

if min_end_point is not None:
    extrema.append(min_end_point)

if max_end_point is not None:
    extrema.append(max_end_point)

extrema.sort()

print(extrema)

sol_f = lambdify(x, f)

# creates list of all solutions

extrema_value = []
for i in extrema:
    if i != 0:
        value = sol_f(i)
        extrema_value.append(value)

# gets maximum
abs_max_value = max(extrema_value)
index_of_abs_max = extrema_value.index(abs_max_value)
abs_max_extrema = extrema[index_of_abs_max]

# gets minimum
abs_min_value = min(extrema_value)
index_of_abs_min = extrema_value.index(abs_min_value)
abs_min_extrema = extrema[index_of_abs_min]

print("""Max extrema is {} with value {}
Min extrema is {} with value {}""". format(float(abs_max_extrema),
                                           float(abs_max_value),
                                           float(abs_min_extrema),
                                           float(abs_min_value)))

