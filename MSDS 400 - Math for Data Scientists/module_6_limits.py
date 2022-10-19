import numpy
from numpy import sin, arange
import matplotlib.pyplot
from matplotlib.pyplot import *

def g(x):
    g = (x**3 - 7*x**2 + 6*x+8)/(x-2)  # define function here
    return g

n=5  # This determines the number of values calculated on each side of x=0.
powers=arange(2,n+1) # first number is limit at
denominator=2.0**powers  # denominator contains exponentiated values of 2.0.
delta=2.0  #This is the interval used on either side of the origin.

x_r=delta/denominator
y_r=g(x_r)
x_l=-x_r   # The negative sign generates a symmetric point on the left.
y_l=g(x_l)

ymax=max(abs(y_r))+0.5
ymin=-ymax
figure()
xlim(-delta-0.5,delta+0.5)
ylim(ymin,ymax)
plot(x_r,y_r, color='b')
plot(x_l,y_l,color='r')

# The black points were computed.  The yellow point marks the limit.
scatter(x_r,y_r,color='k',s=30)
scatter(x_l,y_l,color='k',s=30)
scatter(0.0,g(0.0),c='y',s=40)
title ('Example of Convergence to a Functional Value')
xlabel('x-axis')
ylabel('y-axis')
show()

def f(x):
    f = (8.0*x)/(3*x-1)
    return f


number = 210  # This is the number of points calculated (minus the increment).
increment = 10  # This is the increment between the points.

y = []
x = []

for k in range(increment, number, increment):
    w = float(k)
    x = x + [k]
    y = y + [f(w)]

print('Final value equals', y[-1])  # Floating point with 4 decimals.

figure()
xlim(0,number+increment)
ylim(min(y)-0.1, max(y)+0.1)
plot(x,y, color='r')
scatter(x,y,color='k',s=30)
scatter(number,y[-1],c='y',s=40)
title ('Example of Convergence to a Limit at Infinity')
xlabel('x-axis')
ylabel('y-axis')
show()  # Plot shows convergence to limit at infinity