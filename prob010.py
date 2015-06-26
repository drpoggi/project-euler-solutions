"""The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million."""


def eratosthenes2(n):
    multiples = set()
    for i in range(2, n + 1):
        if i not in multiples:
            yield i
            multiples.update(range(i * i, n + 1, i))


print(sum(i for i in eratosthenes2(2 * 10**6)))
