# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
#
# Find the sum of all the primes below two million.

# Method:
# 1. This is slow but will do it without using any modules (optimized solution would use numpy)
# 2. 1 to 2 million
# 3. On each loop test the value using the Use the Sieve of Eratosthenes algorithm to see
# 4. If true add that value to the sum of primes.

# # Solution 1: Seive
def sieve(n):

    # Define variabes
    # - the first list to hold calculated multiples
    # - the second to hold the sieved out prime numbers.

    multiples = []
    primes = []

    for i in range(2, n+1):
        if i not in multiples:  # the prime sieve
            primes.append(i)
            for j in range(i*i, n+1, i):
                multiples.append(j)
    print(sum(primes))


# Solution 2: A faster sieve
# optimized solution from https://algodaily.com/challenges/sum-all-primes/python

def sumofprimes(n):
    if n <= 1:
        return 1  # not considered a prime

    prime = [True] * (n + 1)  # list to store if number is prime number

    p = 2  # start at 2
    while p * p <= n:  # continue loop until upper bound
        # if p is not changed in prime, then it is prime number
        if prime[p] is True:
            i = p * 2  # update all multiples of p

            while i <= n:
                prime[i] = False
                i += p
        p += 1

    totalsum = 0
    for i in range(2, n + 1):  # find the sum by looking into prime list
        if prime[i]:
            totalsum += i
    return totalsum


print(sumofprimes(2000000))
