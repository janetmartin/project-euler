# Question 6: Sum Square Differences https://projecteuler.net/problem=6

# function for diff betwen square of sums and sum of squares
def sum_of_squares(end):
    squares = 0
    for i in range(0, end + 1):
        squares += i**2
    return sum(range(end + 1))**2 - squares


print("Test Case:", sum_of_squares(10))
print("Solution:", sum_of_squares(100))
