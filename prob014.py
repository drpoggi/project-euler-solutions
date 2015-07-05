"""

The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:
13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1

It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
"""
import time


def f_odd(x):
    return 3 * x + 1


def f_even(x):
    return x / 2


def longest_collatz(upper_bound):
    longest = {'digit': 0, 'chain_length': 0}  # [starting number, length of chain]
    target = 1
    for i in range(2, upper_bound):
        current = i
        chain = []
        while current != target:
            if current % 2 == 0:
                current = f_even(current)
                chain.append(current)
            else:
                current = f_odd(current)
                chain.append(current)
        if len(chain) > longest['chain_length']:
            longest['chain_length'] = len(chain)
            longest['digit'] = i

    return longest

if __name__ == '__main__':
    t0 = time.time()
    print(longest_collatz(1000000))
    t1 = time.time()
    print('Completed in {:.3f}s'.format(t1-t0))
