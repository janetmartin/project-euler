# Question 7: 10001st prime https://projecteuler.net/problem=7
import math


# function to test for primality
def isprime(num):
    for n in range(2, int(math.sqrt(num))+1):
        if num % n == 0:
            return False
    return True


def find_prime(nth):
    primes = []
    counter = 0
    num = 2
    while counter < nth:
        if isprime(num):
            primes.append(num)
            counter += 1
        num += 1
    return primes[-1]


print("Test case: ", find_prime(6))
print("Solution: ", find_prime(10001))
