"""

2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""

from itertools import count

divisors = [i for i in range(1, 21)]

for num in count(20):
    for i in divisors:
        if num % i != 0:
            break
    else:
        print(num)
        break
