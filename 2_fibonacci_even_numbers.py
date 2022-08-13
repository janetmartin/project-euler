# Question 2: Even Fibonacci Numbers https://projecteuler.net/problem=2

def fib(high):
    n1 = 0
    n2 = 1
    total = 0
      # formula for next item in fib sequence (add the previous 2 values)
    while total <= high:
        nth = n1 + n2
        if nth % 2 == 0:
            total = total + nth
        print(nth)
        n1 += 1
        n1 = n2
        n2 = nth
    print(total)
    return total

fib(4000000)

