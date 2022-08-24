# Question 4: Largest Palindrome https://projecteuler.net/problem=4

# function to reverse a string
def reverse(x):
    x = str(x)
    return int(x[::-1])


# function to detect largest palindrome
def max_palindrome(val1, val2):
    product1 = 0
    for a in range(val1, val2 + 1):
        for b in range(val1, val2 + 1):
            product2 = a * b
            if product2 == reverse(product2):
                if product2 > product1:
                    product1 = product2
    return product1

# testcase
# print(max_palindrome(10, 99))
print(max_palindrome(100, 999))
