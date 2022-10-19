import numpy as np
import matplotlib.pyplot as plt

def extrema(a, b, c):
    x = max(a, b, c)
    z = min(a, b, c)
    epsilon = 0.0000001  # This is a safeguard against minor differences.
    result = False
    if abs(b - x) < epsilon:
        result = True
    if abs(b - z) < epsilon:
        result = True
    return result

def f(x):
    y = x**4 - 98*x**2 +3
    return y

xa = -6.0
xb = +15.0

n = 1000
delta = (xb - xa) / n
x = np.arange(xa, xb + delta, delta)
y = f(x)

value = [False]  # This defines the list value which will contain Boolean values.
value = value * len(x)  # This expands the list to the length of x.

L = len(x)
value[0] = True  # This will correspond to one endpoint.
value[L - 1] = True  # This corresponds to the other.

for x_index in range(L - 2):
    first_x = x[x_index]
    second_x = x[x_index + 1]
    third_x = x[x_index + 2]
    a = f(first_x)
    b = f(second_x)
    c = f(third_x)
    is_second_x_extrema = extrema(a, b, c)
    value[x_index + 1] = is_second_x_extrema

for k in range(L - 2):
    value[k + 1] = extrema(f(x[k]), f(x[k + 1]), f(x[k + 2]))

max_value = max(y)  # We check the list to find the global maxima.
min_value = min(y)  # We check the list to find the global minima.

error = 0.0000001  # The error parameter guards against roundoff error.
# The code which follows assigns colors to maxima and minima and plots them.

plt.figure()
for k in range(L):
    if value[k] is True:
        plt.scatter(x[k], y[k], s=60, c='y')
        if abs(max_value - y[k]) < error:
            plt.scatter(x[k], y[k], s=60, c='r')
        if abs(min_value - y[k]) < error:
            plt.scatter(x[k], y[k], s=60, c='b')

plt.plot(x, y, c='k')  # This plots the line on the chart.
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title('Plot Showing Absolute and Relative Extrema')
plt.show()