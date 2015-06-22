print(max(filter(lambda num: str(num) == str(num)[::-1], [i * j for i in range(100, 1000) for j in range(100, 1000)])))
