# Solution to Question 1: Sum of Multiples https://projecteuler.net/problem=1

def sum_of_multiples(low, high):
    y = 0
    for i in range(low, high, 1):
        if i % 3 == 0 or i % 5 == 0:
            y= y + i
    print(y)
    return y

sum_of_multiples(1, 1000)

