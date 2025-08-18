limit = 10

odd_itter = iter(range(1, limit, 2))

for num in odd_itter:
    print(num)

odd_itter = iter(range(0, limit, 2))

for num in odd_itter:
    print(num)