from scipy import stats
x = [0, 1, 2, 3, 4, 5]
y = [174, 193, 201, 228, 233, 279]
slope, intercept, r_value, p_value, std_err = stats.linregress(x, y)
print('slope = ', round(slope,2))
print('intercept = ', round(intercept,2))

for year in [2022, 2046]:
    x = year - 2009
    print(round(slope, 2)*x+round(intercept, 2))
