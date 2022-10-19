from statistics import mode

# Way 1 for file handling in python.
# file = open("test.txt", mode ="r")

# data = file.readlines()
# print(data)

# Way 2 for file handling in Python using With open Function.

with open("test.txt",mode="r") as file:
    data = file.readlines()
    print(data) 