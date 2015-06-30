"""Work out the first ten digits of the sum of the following one-hundred 50-digit numbers."""

total = 0
with open('prob013_numbers.txt', 'r') as f:
    for line in f.readlines():
        total += int(line)

print(str(total)[:10])
