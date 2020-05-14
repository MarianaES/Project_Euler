# Problem 10: Summation of primes
# Objective: Find the sum of all the primes below n.
# 2 + 3 + 5 + 7 = 17.

from aux_funcs.time_decorator import timer

# Function definition
@timer
def primeSummation(number):
    primes = [2]
    for possible_prime in range(3, number, 2):
        for digit in primes:
            if possible_prime % digit == 0:
                break
        else:
            primes.append(possible_prime)
    return sum(primes)


# Tests
print(primeSummation(17)) # Should return 41
print(primeSummation(2001)) # Should return 277050
print(primeSummation(140759)) # Should return 873608362
print(primeSummation(2000000)) # Should return 142913828922
