# creates the functions for the counting principle
def factorial(n):
    if n == 0:
        return 1
    else:
        recurse = factorial(n - 1)
        result = n * recurse
        return result


def perm(n, k):
    if n == 0:
        return 1
    if k > n:
        return -1
    else:
        return (factorial(n)) / factorial(n - k)


def comb(n, k):
    result = perm(n, k)
    result = result / factorial(k)
    result = int(result)
    return result



