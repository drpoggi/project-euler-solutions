"""

A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

print(max(filter(lambda num: str(num) == str(num)[::-1], [i * j for i in range(100, 1000) for j in range(100, 1000)])))
