class parent():

    def __init__(self) -> None:
        self.id = None
        self.name = None
        self.father_name = None
        self.email = None

    def speak(self,language = 'urdu'):
        return f"{self.name} is speaking {language} language! "
    
    def eat(self,food):
        return f"{self.name} is eating {food}"
    
class child(parent):
    pass


c1 = child()
c1.id = 2
c1.name = 'faizan'
c1.father_name = 'yousaf'
c1.email = 'faizan@gmail.com'

print(c1.id)
print(c1.name)
print(c1.father_name)
print(c1.email)

p1 = parent()
p1.name = 'faizan'

print(p1.eat('biriyani'))


