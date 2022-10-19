with open('test.txt','r') as file:
    # data = file.readline() #    this will read only first line in the test.txt file.
    # data = file.readlines() #   this will read the whole content in the test.txt file.
    data =file.read() #     this is similar to readlines function.will print the whole content.

    print(data)