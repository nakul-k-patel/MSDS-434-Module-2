import matplotlib.pyplot as plt
from numpy import poly1d, linspace

p = poly1d([5, -3, 2])
print(p)

q = poly1d([2, 1, 4, -2, 3])
print(q)

g = p + p*q

print(g)

h = p.deriv(m=1)  # First derivative with m=1.
print(h)
print(h.roots)

t = p.deriv(m=2)  # Second derivative with m=2.
print(t)
print(t.roots)

w = t.integ(m=2, k=[-3, 2])
print(w)
print(w.coeffs)

new = t.integ(m=2, k=[-2, 4])
print(new)
print(new.deriv(m=1))

print(w.roots) # roots solves polynomial for zero

p = poly1d([.3333, 0, -1, 5])

g = p.deriv(m=1)

print('\nRoots of First Derivative')
print(g.roots)

print('\nRoots of Second Derivative')
q = p.deriv(m=2)
print(q.roots)

x = linspace(-4, 4, 101)
y = p(x)
yg = g(x)  # These statements define points for plotting.
yq = q(x)
y0 = 0*x   # This statement defines the y axis for plotting.

plt.figure()
plt.plot(x, y, label='y=p(x)')
plt.plot(x, yg, label='First Derivative')
plt.plot(x, yq, label='Second Derivative')
plt.legend(loc='best')

plt.plot(x, y0)
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title('Plot Showing Function, First and Second Derivatives')
plt.show()

plt.figure()
p = poly1d([3, -4, -12, 0, 2])
print('\nFourth Degree Polynomial')
print(p)
print('\nFirst Derivative')
g = p.deriv(m=1)  # First derivative with m=1.
print(g)
print('\nSecond Derivative')
q = p.deriv(m=2)  # Second derivative with m=2.
print(q)
x = linspace(-2, 3, 101)
y = p(x)
yg = g(x)  # These statements define points for plotting.
yq = q(x)
y0 = 0*x  # This statement defines the y axis for plotting.
plt.plot(x, y, label='y=p(x)')
plt.plot(x, yg, label='First Derivative')
plt.plot(x, yq, label='Second Derivative')
plt.legend(loc='best')

plt.plot(x, y0)
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title('Plot Showing Function, First and Second Derivatives')
plt.show()