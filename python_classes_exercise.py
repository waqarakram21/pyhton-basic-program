class A:
    def __init__(self,c) -> None:
        print("---------inside class A----------")
        self.c = c
    print("print inside A")

    def alpha(self):
        c = self.c+1
        return c

print(dir(A))
print("instantiating A...")
a=A(1)
print(a.alpha)

class B:
    def __init__(self,a) -> None:
        print("-------------inside class B------------")
        self.a = a

    print(a.alpha())
    d=5
    print(d)
    print(a)

    
print("instantiating B...")
b = B(a)
print(a)

