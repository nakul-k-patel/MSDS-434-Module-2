from numpy import random, arange, array, swapaxes
import matplotlib.pyplot as plt

nsamples = 100
sample = random.random(nsamples)  # This draws a random sample.

nbins = 10  # This defines the number of subintervals for the histogram.
bns = float(nbins)
print(bns)

expected = 1.0 / bns  # This defines the expected subinterval proportion.

ind = arange(nbins)  # This sets ind to serve as a range of indices.
h = [0] * nbins  # This prepares h to serve as a list of the proper length.
histogram = {}  # This defines histogram as a void dictionary.

for k in ind:
    histogram[k] = 0  # This initializes the dictionary with zero counts.
print(histogram)

for v in sample:
    for k in ind:
        xk = float(k)
        if xk / bns <= v < (xk + 1) / bns:
            histogram[k] += 1
print(histogram)

for k in ind:
    x = histogram[k]
    x = x / float(nsamples)
    h[k] = [x]
    histogram[k] = x
print(histogram)

total = 0.0
for k in ind:
    total = total + abs(expected - histogram[k])
total = format(total, '0.4e')
print('Sum of Absolute Differences= {}'.format(total))

h = swapaxes(h, 0, 1)[0]  # Swapping x/y axes for pyplot
cell = ind + 0.5  # This will center the bar in the middle of the subinterval.
plt.figure()
plt.bar(cell, h, width=0.5, align='center', color='r')
plt.plot(cell, h)

# The following statements are used to form the title for the plot.
# Note how computational information is being included in the title.

string = str(nsamples) + '   Absolute Difference= ' + str(sum)
plt.title('Histogram   n=' + string)

plt.ylabel('Proportions')
plt.xlabel('Subintervals')
plt.show()