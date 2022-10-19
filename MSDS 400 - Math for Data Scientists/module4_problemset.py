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


# define tuple for probability storage
probs = []

# populates tuples with every possible outcome and their relevant
# probability to pull needed suit from remaining cards
for i in range(0, 6):
    probA = comb(9, i) * comb(38, 5 - i) / comb(47, 5)
    probBA = (9 - i) / 33
    probs.append((i, probA, probBA))

# defines list of all products of probability compliments and probability of pulling card
# given probability of opponent hand
probComplements = []

# populates list created of products
for suit_cards, probA, probBA in probs:
    print("""The probability of the opponent drawing {} cards of the same suit is {} 
    and the probability of you drawing the suit after discarding is {}"""
          .format(suit_cards,probA,probBA))
    probComplements.append(probA * probBA)

# defines denominator of bayes theorem
denominator = 0
for i in range (0, 6):
    denominator += probComplements[i]
# bayes theorem
probAB = probComplements[5]/denominator
print("The probability of your opponent having a flush of the same suit is {}".format(probAB))


