# input current budget in thousands
current_b1 = 0
current_b2 = 0
current_b3 = 0
current_b4 = 0

# input incremental in thousands
available_cash = 2000
# step is what increment to allocate dollars
step = 1

from sympy import Symbol, log as ln, diff

# assign symbols
b1 = Symbol('b1')
b2 = Symbol('b2')
b3 = Symbol('b3')
b4 = Symbol('b4')

# define production function
f = 15*ln(b1+1) + 11*ln(b2+1) + 12*ln(b3+1) + 10*ln(b4+1)

# calculate derivatives

fdb1 = diff(f, b1)
fdb2 = diff(f, b2)
fdb3 = diff(f, b3)
fdb4 = diff(f, b4)

# calculate current rates and value
value = f.doit().subs({b1: current_b1, b2: current_b2, b3: current_b3, b4: current_b4})
instant_b1 = fdb1.doit().subs({b1: current_b1, b2: current_b2, b3: current_b3, b4: current_b4})
instant_b2 = fdb2.doit().subs({b1: current_b1, b2: current_b2, b3: current_b3, b4: current_b4})
instant_b3 = fdb3.doit().subs({b1: current_b1, b2: current_b2, b3: current_b3, b4: current_b4})
instant_b4 = fdb4.doit().subs({b1: current_b1, b2: current_b2, b3: current_b3, b4: current_b4})


# create indexes for values and instant roi
current_values = [current_b1, current_b2, current_b3, current_b4]
instant_roi = [instant_b1, instant_b2, instant_b3, instant_b4]

# allocate incremental in step wise increments as instantaneous roi decreases with additional budget

for i in range(0, available_cash, step):
    max_value = max(instant_roi)
    index_of_max = instant_roi.index(max_value)
    current_values[index_of_max] += step
    instant_b1 = fdb1.doit().subs(
        {b1: current_values[0], b2: current_values[1], b3: current_values[2], b4: current_values[3]})
    instant_b2 = fdb2.doit().subs(
        {b1: current_values[0], b2: current_values[1], b3: current_values[2], b4: current_values[3]})
    instant_b3 = fdb3.doit().subs(
        {b1: current_values[0], b2: current_values[1], b3: current_values[2], b4: current_values[3]})
    instant_b4 = fdb4.doit().subs(
        {b1: current_values[0], b2: current_values[1], b3: current_values[2], b4: current_values[3]})
    instant_roi = [instant_b1, instant_b2, instant_b3, instant_b4]


# calculate new production1
value = f.doit().subs({b1: current_values[0], b2: current_values[1], b3: current_values[2], b4: current_values[3]})

# get output of algorithm
print(current_values)
print("Your budget across investments should be:")
print("b1 = ${}, b2 = ${}, b3 = ${}, b4 = ${}".format(current_values[0],
                                                      current_values[1],
                                                      current_values[2],
                                                      current_values[3], ))
print('Based on returns, you will see an aggregate return of {}% '.format(round(value / available_cash, 2)))
