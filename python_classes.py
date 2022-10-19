class myClass():# this is the method for initializing the class.
    a=5
    print("hello")
    def call(self):
        print("hello! world.")

myc = myClass() # here myc is the instance class.
print(myc.a)
print(myc.call())# we can also print the "hello! world." using the instance function but it need to write the key word "self in the function parentheses"

