# Problem 2: Even Fibonacci Numbers
# Objective: By considering the terms in the Fibonacci sequence whose values
# do not exceed n, find the sum of the even-valued terms.

from aux_funcs.time_decorator import timer

# Function definition
@timer
def fiboEvenSum(number):
    fibo_seq = [1, 2]
    result = 0
    if number <= 1:
        print('No even number to sum, please try again!')
    else:
        for i in range(1, number):
            fibo_seq.append(fibo_seq[i] + fibo_seq[i-1])
            if fibo_seq[-1] >= number:
                break
        for x in fibo_seq:
            if x % 2 == 0:
                result += x
        return result

# Tests
print(fiboEvenSum(10)) # Should return 10
print(fiboEvenSum(60)) # Should return 44
print(fiboEvenSum(1000)) # Should return 798
print(fiboEvenSum(100000)) # Should return 60696
print(fiboEvenSum(4000000)) # Should return 4613732
print(fiboEvenSum(0)) # Should print 'No even number to sum, please try again!'
print(fiboEvenSum(1)) # Should print 'No even number to sum, please try again!'
print(fiboEvenSum(2)) # Should return 2
