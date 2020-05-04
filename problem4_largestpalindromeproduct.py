# Problem 4: Largest palindrome product
# Objective: Find the largest palindrome made from the product of two n-digit
# numbers.

from aux_funcs.time_decorator import timer

# Function definition
# Option1 
@timer
def largestPalindromeProducta(n):
    product = 0
    palindromes = []
    start = 10 **(n-1)
    end = 10**n
    for x in range(start, end):
        for y in range(start, end):
            product = x * y
            if str(product) == str(product)[::-1]:
                palindromes.append(product)
    palindromes.sort()
    return palindromes[-1]

# Option 2
@timer
def largestPalindromeProductb(n):
    product = 0
    palindromes = []
    start = 10 **(n-1)
    end = 10**n
    for x in range(start, end):
        for y in range(start, end):
            product = x * y
            if str(product) == str(product)[::-1]:
                palindromes.append(product)
    return max(palindromes)

# Tests
print(largestPalindromeProducta(2)) # Should return 9009
print(largestPalindromeProductb(2)) # Should return 9009
print(largestPalindromeProducta(3)) # Should return 906609
print(largestPalindromeProductb(3)) # Should return 906609
