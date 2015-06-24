"""By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
What is the 10 001st prime number?"""


def eratosthenes2(n):
    multiples = set()
    for i in range(2, n + 1):
        if i not in multiples:
            yield i
            multiples.update(range(i * i, n + 1, i))


def find_prime(goal_prime):
    primes = set()
    for num in eratosthenes2(goal_prime ** 2):
        primes.add(num)
        if len(primes) == goal_prime:
            return num
            break

print(find_prime(10001))
