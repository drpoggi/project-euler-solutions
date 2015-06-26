"""

A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
a2 + b2 = c2

For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc."""

for a in range(1, 1000):
    for b in range(1, 1000):
        if b > a:
            for c in range(1, 1000):
                if c > b:
                    if a + b + c == 1000 and a**2 + b**2 == c**2:
                        A = a
                        B = b
                        C = c

print(A*B*C)
