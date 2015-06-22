from functools import reduce
from math import sqrt


def eratosthenes2(n):
    multiples = set()
    for i in range(2, n + 1):
        if i not in multiples:
            yield i
            multiples.update(range(i * i, n + 1, i))


def factors(n):
    return set(reduce(list.__add__,
                      ([i, n // i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))


def prime_factor(n):
    factor_results = factors(n)
    primes = set((eratosthenes2(int(sqrt(n)) + 1)))
    return factor_results.intersection(primes)


print(max(prime_factor(600851475143)))
