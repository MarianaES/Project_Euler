# Problem 1: Multiples of 3 and 5
# Objective: Find the sum of all the multiples of 3 or 5 below the provided parameter value number.

from aux_funcs.time_decorator import timer

# Function definition
# Option1
@timer
def multiplesOf3and5a(number):
    multiples_lst = []
    for x in range(1, number):
        if x % 3 == 0 or x % 5 == 0:
            multiples_lst.append(x)
    return sum(multiples_lst)
    
# Option2 (Fastest)
@timer
def multiplesOf3and5b(number):
    multiples_lst = 0
    for x in range(1, number):
        if x % 3 == 0 or x % 5 == 0:
            multiples_lst += x
    return multiples_lst

# Tests

# print(multiplesOf3and5(10)) #Should return 23
# print(multiplesOf3and5(49)) #Should return 543
# print(multiplesOf3and5(1000)) #Should return 233168
# print(multiplesOf3and5(8456)) #Should return 16687353
print(multiplesOf3and5a(19564)) #Should return 89301183
print(multiplesOf3and5b(19564)) #Should return 89301183
