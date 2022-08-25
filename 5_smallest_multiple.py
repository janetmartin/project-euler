# Question 5: Smallest Multiple https://projecteuler.net/problem=5

import math

# Method Using Libraries
print(math.lcm(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20))

# Method Without Using Libraries
i = 1
for k in (range(1, 21)):
    if i % k > 0:
        for j in range(1, 21):
            if (i*j) % k == 0:
                i *= j
                break
print(i)
