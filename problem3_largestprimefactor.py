# Problem 3: Largest prime factor
# Objective: Find the largest prime factor of a given number.

from aux_funcs.time_decorator import timer

# Function definition
@timer
def largestPrimeFactor(number):
    if type(number) != int:
        return 'Number must be a natural number!'
    if number == 1:
        return 'There is no largest prime factor, one is a unit!'
    divisor = 2
    while divisor * divisor <= number:
        if number % divisor != 0:
            divisor += 1
        else:
            number //= divisor
    return number


# Tests
print(largestPrimeFactor(2)) # Should return 2
print(largestPrimeFactor(3)) # Should return 3
print(largestPrimeFactor(5)) # Should return 5
print(largestPrimeFactor(7)) # Should return 7
print(largestPrimeFactor(13195)) # Should return 29
print(largestPrimeFactor(600851475143)) # Should return 6857
print(largestPrimeFactor(0.6)) # Should return 'Number must be a natural number!'
print(largestPrimeFactor("Hola")) # Should return 'Number must be a natural number!'
print(largestPrimeFactor(1)) # Should return 'There is no largest prime factor, one is a unit!
