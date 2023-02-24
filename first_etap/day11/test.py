def sum_range(start, end):
    total = 0
    if start < end:
        for i in range(start, end):
            total += i
    else:
        for i in range(end, start):
            total += i
    return total


print(sum_range(100, 10))