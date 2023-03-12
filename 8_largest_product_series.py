# Question 8: Find the largest product in a series, https://projecteuler.net/problem=8

# Track run time

import time
start_time = time.time()

# Data

value = 7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450

# Solution
i = 13 # number of digits in interval
product = 0  # define product variable, and set to zreo
b = str(value)  # convert value to a string so that string methods can be used to index value
while len(b) >= i:  # while i digits exist run the following loop
    calc = int(b[0]) * int(b[1]) * int(b[2]) * int(b[3]) * int(b[4]) * int(b[5]) * int(b[6]) * int(b[7]) * int(b[8]) * int(b[9]) * int(b[10]) * int(b[11]) * int(b[12])  # calculate the product by multipying the values returned by the index, note that after value is indeed it must be converted to an integer in order to find the product.
    if calc > product:  # compare to previous result
        product = calc  # save highest value
    b = (b[1:])  # slice off first item in value which shifts sliding window to the next 13 digits on the next run of this loop

# Result

print("The largest product is:", product)

# Runtime

print("This program took", time.time() - start_time, "seconds to run.")