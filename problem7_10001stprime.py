# Problem 7: 10001st prime
# Objective: By listing the prime numbers, find the nth prime number.

from aux_funcs.time_decorator import timer

# Function definition
# Option1
@timer
def nthPrimea(number):
    prime_numbers = []
    possible_prime = 2
    while len(prime_numbers) < number:
        if possible_prime == 2:
            prime_numbers.append(possible_prime)
        elif possible_prime % 2 != 0:
            is_prime = True
            for prime_number in prime_numbers:
                if possible_prime % prime_number == 0:
                    is_prime = False
                    break
            if is_prime:
                prime_numbers.append(possible_prime)
        possible_prime += 1
    return prime_numbers[-1]
    
# Option2 (Fastest)
@timer
def nthPrimeb(number):
    prime_numbers = [2]
    possible_prime = 3
    while len(prime_numbers) < number:
        is_prime = True
        for prime_number in prime_numbers:
            if possible_prime % prime_number == 0:
                is_prime = False
                break
        if is_prime:
            prime_numbers.append(possible_prime)
        possible_prime += 2
    return prime_numbers[-1]

if __name__ == "__main__":

    # Tests
    print(nthPrimea(6)) # Should return 13
    print(nthPrimeb(6)) # Should return 13

    print(nthPrimea(10)) # Should return 29
    print(nthPrimeb(10)) # Should return 29

    print(nthPrimea(100)) # Should return 541
    print(nthPrimeb(100)) # Should return 541

    print(nthPrimea(1000)) # Should return 7919
    print(nthPrimeb(1000)) # Should return 7919

    print(nthPrimea(10001)) # Should return 104743
    print(nthPrimeb(10001)) # Should return 104743
