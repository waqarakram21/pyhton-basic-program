status = int(input("enter the signal status: "))

if status>100 and status<199:
    print("informational error..")
elif status>200 and status <299:
    print("conditional error..")
else:
    print("the error is occured..")