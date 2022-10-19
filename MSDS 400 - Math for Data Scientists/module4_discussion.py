def factorial(n):
    if n == 0:
        return 1
    else:
        recurse = factorial(n - 1)
        result = n * recurse
        return result

probC = 0
for i in range (1, 10):
    prob = ((factorial(i)*factorial(37))/(factorial(47))) * (factorial((47-i))/factorial(37))
    # probB += prob*((10-i)/38)
    probC += prob
    print(probC)

probD = 1 - probC
print(probD)
print("*"*10)
print(probD + probC)
print("*"*10)

A = 38*37*36*35*34*33*32*31*30*29
B = 47*46*45*44*43*42*41*40*39*38
print(A/B)


# for i in range (1,10):
#     print(i)
#     A = (factorial((47-i))/factorial(37))
#     print(A)
#     B = (factorial(i)*factorial(37))/(factorial(47))
#     print(B)
#     print(A*B)
#     print('-'*10)


