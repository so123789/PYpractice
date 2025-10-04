#Brute force approach to count the number of digits in a number
#TC: O(log n)
#SC: O(1)
def CountDigits(n):
    count = 0
    while n > 0:
        n = n // 10
        count += 1
    return count

print(CountDigits(234))

import math
#Optimal approiach
#TC: O(1)
#SC: O(1)
def CountDigitsOptimal(n):
    if n == 0:
        return 1
    count = int(math.log10(n) + 1)
    return count

print(CountDigitsOptimal(2345))
    