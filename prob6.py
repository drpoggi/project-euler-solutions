def sum_of_square(num_range):
    return sum(x ** 2 for x in range(1, num_range + 1))


def square_of_sum(num_range):
    return sum(x for x in range(1, num_range + 1)) ** 2

print(abs(square_of_sum(100) - sum_of_square(100)))
