import matplotlib.pyplot as plt
import math

# An example function:

def f(x):
    return (math.pow(x, 2) + 100) * math.log(x + 2)  # Students can supply their functions at this point.

def integrate(a, b, n):
    total = 0.0
    delta = (b - a) / n
    i = 0
    while i < n:
        total = total + delta * (f(a + delta * (i + 1)) + f(a + delta * i)) / 2.0
        i = i + 1
    return total

# This shows list manipulations resulting in a plot
y = []
x = []
b = 4.0
a = 0.0
rng = [10, 20, 30, 40, 50, 100, 250]

for n in rng:
    area = integrate(a, b, n)
    x = x + [n]
    y = y + [area]

plt.xlim(0, max(x) + 60)
plt.ylim(min(y) - 0.5, max(y) + 0.5)

plt.plot(x, y)
plt.scatter(x, y, s=30, c='r')
plt.scatter(300, 64.0, c='y')  # This plots the limiting value for the area.

plt.xlabel('Number of Subintervals')
plt.ylabel('Estimated Area')
plt.title('Plot Showing Numerical Integration Convergence')
plt.show()

area = float(format(y[-1], '0.3f'))
print("Final Estimate of Area with %r subdivisions = {}".format(x[-1], area))