from numpy import array, absolute
t = [1, 2, 3]

print('Comparison of a concatenated list with an array ')
r = [4, 5, 6]
print('r= {} and t= {} \n'.format(r, t))
result1 = t + r
print('Concatenation example using t and r lists. {}'.format(result1))
result2 = array([t, r])
print('\n Comparison of concatenation with array([t,r]).')
print(result2)
print('\n The second element of the preceding list and array')
print(result1[1]) # becomes index of original array
print(result2[1]) # becomes row basically of arrayed arrays aka a matrix
print('\n Slicing to produce an element, a column and a row of the array')
print(result2[0, 1])
print(result2[:, 1])  # Note the horizontal output of a column.
print(result2[1, :])  # Gives horizontal output of a row
