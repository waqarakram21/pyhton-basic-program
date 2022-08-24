def sum_of(**kwargs):
    sum = 0
    for i,j in kwargs.items():
        sum += j
    return sum

print(sum_of(coffee=12,salad=5))