# Problem 9: Special Pythagorean triplet
# Objective: A Pythagorean triplet is a set of three natural numbers,
# a < b < c, for which, a2 + b2 = c2.
# Find the product abc such that a + b + c = n.

from aux_funcs.time_decorator import timer

# Function definition
@timer
def specialPythagoreanTriplet(number):
    # m must be greater than n always to comply with a < b < c < number
    products = []
    for n in range(1, number):
        for m in range(2, number):
            # Simplified sum from the below formulas (a + b + c)
            possible = (2*m)*(m+n)
            if possible == number:
                # The following formulas obtained from a2 + b2 = c2
                # to get possible pythagorean triplets.
                a = 2*m*n
                b = m**2 - n**2
                c = n**2 + m**2
                product = a * b * c
                return product

# Tests
print(specialPythagoreanTriplet(24)) # Should return 480
print(specialPythagoreanTriplet(120)) # Should return 49920, 55080 or 60000
print(specialPythagoreanTriplet(1000)) # Should return 31875000
