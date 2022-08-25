# Question 6: Sum Square Differences https://projecteuler.net/problem=6
# solve for diff between sum of squares and square of sums

# function for square of sum with divisor
def square_of_sums(start, end, divisor):
    return sum(range(start, end + 1, divisor))**2


# function for sum of squares
def sum_of_squares(start, end, divisor):
    squares = []
    for i in range(start, end + 1, divisor):
        squares.append(i ** 2)
    return sum(squares)


print("Test Case:", square_of_sums(1, 10, 1) - sum_of_squares(1, 10, 1))
print("Solution:", square_of_sums(1, 100, 1) - sum_of_squares(1, 100, 1))
