import matplotlib.pyplot
from matplotlib.pyplot import *
import numpy
from numpy import linspace
x1 = 6.0
y1 = -4.0
x2 = 11.0
y2 = -5.0
slope = (y2-y1)/(x2-x1)
print(slope)

x= 0
y= y1 + slope*(x-x1)
print('\nValue of y if x is 0.0 equals {}'.format(y))

print(fraction(-2.8))

equation= str('y = y1 + slope*(x-x1)')
print('Equation of a line is', equation)
print('x1 equals {} and y1 equals {}'.format(x1, y1))

x = linspace(0,12,100)
y = (x**2+25)/(4*x)
title('Plot of Linear Equation  '+equation)  # Note how the title appears.
plot(x,y)
show()

# from scipy import stats
# x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
# y = [6.86, 5.04, 4.92, 6.6, 6.38, 3.56, 6.24, 3.12, 4.5, 1.68, 1.86, 2.04, 1.42, 3.4]
# slope, intercept, r_value, p_value, std_err = stats.linregress(x, y)
# predict_2020 = 120 * slope + intercept
# print("slope = ", round(slope, 3))
# print("intercept = ", round(intercept, 1))
# print("The death rate in 2020 will be approximately", round(predict_2020, 1), "per 100,000 population.")
# print("correlation coefficient = ", round(r_value, 3))
# print(stats.linregress(x,y))
