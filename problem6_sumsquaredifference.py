# Problem 6: Sum square difference
# Objective: Find the difference between the sum of the squares of the first
# n natural numbers and the square of the sum.

from aux_funcs.time_decorator import timer

# Function definition
def sum_squares(lst):
    addition = 0
    for element in lst:
        addition += element ** 2
    return addition

def square_sum(lst):
    addition = 0
    for element in lst:
        addition += element
    return addition ** 2

@timer
def sumSquareDifference(number):
    lst = list(range(1, number + 1))
    difference = square_sum(lst) - sum_squares(lst)
    return difference

# Tests
print(sumSquareDifference(10)) # Should return 2640
print(sumSquareDifference(20)) # Should return 41230
print(sumSquareDifference(100)) # Should return 25164150
