# input current budget in thousands
current_b1 = 400
current_b2 = 400
current_b3 = 300
current_b4 = 600

# input incremental in thousands
incremental = 200
# step is what increment to allocate dollars
step = 1

from sympy import Symbol, log as ln, diff

# assign symbols
b1 = Symbol('b1')
b2 = Symbol('b2')
b3 = Symbol('b3')
b4 = Symbol('b4')

# define production function
f = 400 * ln(b1) + 8400 * ln(b2 * b1 * b3 + 100) + 1600 * ln(b3 + 800) + 8800 * (b4 / 775) ** 3 + 50000

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

# ouput current values
print("At current budget allocation:")
print('Based on MMM you can drive {} conversions '.format(int(value)))
print("fdb1 is {} and will drive {} more conversions with an additional $1000".format(fdb1, (round(instant_b1, 2))))
print("fdb2 is {} and will drive {} more conversions with an additional $1000".format(fdb2, (round(instant_b2, 2))))
print("fdb3 is {} and will drive {} more conversions with an additional $1000".format(fdb3, (round(instant_b3, 2))))
print("fdb4 is {} and will drive {} more conversions with an additional $1000".format(fdb4, (round(instant_b4, 2))))

# create indexes for values and instant roi
current_values = [current_b1, current_b2, current_b3, current_b4]
instant_roi = [instant_b1, instant_b2, instant_b3, instant_b4]

# allocate incremental in step wise increments as instantaneous roi decreases with additional budget

for i in range(0, incremental, step):
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
    print(current_values)

# calculate new production1
value = f.doit().subs({b1: current_values[0], b2: current_values[1], b3: current_values[2], b4: current_values[3]})

# get output of algorithm
print(current_values)
print("Your budget with incremental should be:")
print("b1 = ${}, b2 = ${}, b3 = ${}, b4 = ${}".format(current_values[0] * 1000,
                                                      current_values[1] * 1000,
                                                      current_values[2] * 1000,
                                                      current_values[3] * 1000, ))
print('Based on MMM and incremental budget you can drive {} conversions '.format(int(value)))
