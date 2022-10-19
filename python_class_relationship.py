class A():
    a =5
class B(A):
    b=132
class C(B):
    pass

c = C()
print((c.a),(c.b))

# print(issubclass(A,B))``
# print(issubclass(B,A))

print(isinstance(c,C))

