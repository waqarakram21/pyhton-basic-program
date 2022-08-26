from logging import exception
from re import S


def divide_by(a,b):
    return a/b

# print("the answer is: ", divide_by(40,0))
#this is an excepition because it this is zero error.
#so we'll use the try except statment.

try:
    ans = divide_by(40,0)
except Exception as e:
    print("something wents wrong, ",e)
    
    

