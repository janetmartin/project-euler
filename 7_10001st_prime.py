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

# This 2nd solution iterates over the candidate but does not slow down by appending a list.

def faster_primes(limit):
    count = 1 # we know that 2 is prime
    candidate = 2
    while count < limit:
        candidate = candidate + 1
        if isprime(candidate):
            count=count+1
        if count == limit:
            return(candidate)

print("My Solution")
print("Test case: ", find_prime(6))
print("Solution: ", find_prime(10001))

print("Faster test case:", faster_primes(6))
print("Faster solution:", faster_primes(10001))
