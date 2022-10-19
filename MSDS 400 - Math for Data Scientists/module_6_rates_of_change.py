import numpy
from numpy import arange, cos
import matplotlib.pyplot
from matplotlib.pyplot import *

def der(x, delta):
    delta = float(delta)
    if delta < 0.0000001:
        print('Value chosen for delta is too small.')
        return 1 / delta
    else:
        slope = (f(x + delta) - f(x)) / delta
        return slope

def f(x):
    f = cos(x)
    return f

# The following statements initialize variables for computation.
point = 1.0  #This is a point at which a derivative will be calculated.
number = 510
increment =10
y = []
x = []

for k in range(increment, number, increment):
    delta = 1.0/(k+1)
    d = der(point,delta)
    x = x + [k]
    y = y + [d]
    max_x = k + increment

limit=der(point,0.000001)
print ('Final value equals')
print(limit)

figure()
xlim(0, max_x+50 )
ylim(min(y)-0.05, max(y)+0.05)

scatter(540,limit,color='g',s=40,label='limiting slope')
legend(('limiting slope'),loc='best')
scatter(x,y,c='k',s=20)

title ('Example of Convergence to Instanteous Rate of Change')
xlabel('x-axis')
ylabel('y-axis')
ylabel('y-axis')
plot(x,y)
show()

# Calculate values for the tangent.
w=arange(point-1.0,point+1.1,0.1)
t=f(point)+limit*(w-point)

# Now we are going to plot the original function over a wider range.
# Define a domain for the function.
domain=3.14

# Calculate values for the function on both sides of x=1.0.
u=arange(point-domain,point+domain+0.1,0.1)
z=f(u)

figure()
xlim(point-domain-.1,point+domain+0.1)
ylim(max(z)+.5,min(z)-.5)

plot(w,t,c='r')  # This plots the tangent line.
plot(u,z,c='b')  # This plots the curve itself.
scatter(point,f(point),c='g',s=40)  # This is the point of contact.
xlabel('x-axis')
ylabel('y-axis')
title('Plot showing function and tangent at a point')
show()