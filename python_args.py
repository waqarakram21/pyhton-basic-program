def sum_of(*args):
    sum=0
    for j in args:
        sum += j
    return sum

print(sum_of(1,2,3,4,5,6))