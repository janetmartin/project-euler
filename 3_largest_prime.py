# Question 3: Largest Prime https://projecteuler.net/problem=3

import math

# checking for primality


def isprime(num):
    for n in range(2, int(math.sqrt(num))+1):
        if num % n == 0:
            return False
    return True

# checking for largest prime factors


def largest_factor(value):
    for i in range(2, value):
        if isprime(i):
            if value % i == 0:
                print(i)


largest_factor(600851475143)
