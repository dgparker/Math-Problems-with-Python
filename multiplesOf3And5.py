"""Project Euler problem 1 - Multiples of 3 and 5."""

numberList = []


def sumMultiples():
    """Find sum of all multiples of 3 or 5 below 1000."""
    sum = 0
    for number in range(1000):
        if number % 3 == 0 or number % 5 == 0:
            numberList.append(number)
    for item in numberList:
        sum += item
    return sum


print(sumMultiples())
