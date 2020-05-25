# Problem 12: Highly divisible triangular number
# Objective: The sequence of triangle numbers is generated by adding the natural numbers.
# So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28.
# The first ten terms would be:
# 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...
# Let us list the factors of the first seven triangle numbers:
# 1: 1
# 3: 1, 3
# 6: 1, 2, 3, 6
# 10: 1, 2, 5, 10
# 15: 1, 3, 5, 15
# 21: 1, 3, 7, 21
# 28: 1, 2, 4, 7, 14, 28
# We can see that 28 is the first triangle number to have over five divisors.
# What is the value of the first triangle number to have over n divisors?

from aux_funcs.time_decorator import timer

# Function definition
@timer
def divisibleTriangleNumber(number):
    count_divisors = 2
    addition = 1
    while count_divisors < number:
        triangle_number = sum(list(range(1, number + addition)))
        divisor_lst = list(range(1, int(triangle_number**0.5)))
        for divisor in divisor_lst:
            if count_divisors >= number:
                return triangle_number
            if triangle_number % divisor == 0:
                count_divisors += 2
        else:
            addition += 1
            count_divisors = 1

# Tests

print(divisibleTriangleNumber(5)) # Should return 28
print(divisibleTriangleNumber(23)) # Should return 630
print(divisibleTriangleNumber(167)) # Should return 1_385_280
print(divisibleTriangleNumber(374)) # Should return 17_907_120
print(divisibleTriangleNumber(500)) # Should return 76_576_500
