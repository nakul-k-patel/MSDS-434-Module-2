import matplotlib.pyplot as plt
import numpy as np

# Sample function

def f(x):
    f = x * x - 4.0  # Students can supply a function at this point.
    return f

def integrate(a, b, n):
    total = 0.0
    delta = (b - a) / n
    for i in range(n):
        total = total + delta * (f(a + delta * (i + 1)) + f(a + delta * i)) / 2
    return total

# This defines the parameters for integration.

c = 4.0
b = 2.0
a = 0.0
n = 100

area1 = integrate(a, b, n)
area2 = integrate(b, c, n)
area = abs(area1) + np.abs(area2)

print("Final Estimate of Area= {}".format(area))

x = np.arange(0.0, 2.1, 0.1)  # This defines the interval for the color red.
y = f(x)

x1 = np.arange(2.0, 4.1, 0.1)  # This defines the interval for the color blue.
y1 = f(x1)

plt.figure()
plt.fill_between(x, 0, y, color='r', alpha=0.8)
plt.fill_between(x1, 0.0, y1, color='b', alpha=0.8)

ymin = min(min(y), min(y1))
ymax = max(max(y), max(y1))
plt.xlim(-0.5, 4.5)
plt.ylim(ymin - 1.0, ymax + 1.0)

plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title('Plot Showing Color Coded Integration Areas')
plt.show()

plt.figure()  # This separates the two plots from each other.
x = np.arange(0.0, 4.1, 0.1)  # This defines the interval for color filling.
y = f(x)
plt.plot(x, y, c='k')

# This shows how to fill between the lines using an inequality.

plt.fill_between(x, 0.0, y, where=y < 0.0, facecolor='y', interpolate=True)
plt.fill_between(x, 0.0, y, where=y > 0.0, facecolor='g', interpolate=True)

plt.xlim(-0.5, 4.5)
plt.ylim(ymin - 1.0, ymax + 1.0)
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title('Plot Showing Color Coded Integration Areas')
plt.show()