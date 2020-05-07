# Problem 5: Smallest multiple
# Objective: Find the smallest positive number that is evenly divisible
# by all of the numbers from 1 to n.

from aux_funcs.time_decorator import timer

# Function definition
def reducer(lst, divisor):
    works = False
    new_lst = []
    for element in lst:
        if element % divisor == 0:
            works = True
            element //= divisor
        new_lst.append(element)
    return works, new_lst

@timer
def remainder(n):
    lst = list(range(1, n + 1))
    divisor = 2
    multiples = []
    result = 1
    while set(lst) != {1}:
        works, lst = reducer(lst, divisor)
        if works:
            multiples.append(divisor)
        else:
            divisor += 1
    for element in multiples:
        result *= element
    return result

# Tests
print(remainder(5)) # Should return 60
print(remainder(7)) # Should return 420
print(remainder(10)) # Should return 2520
print(remainder(13)) # Should return 360360
print(remainder(20)) # Should return 232792560
