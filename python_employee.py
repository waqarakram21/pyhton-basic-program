from unicodedata import name


class employee():
    def __init__(self, name, last) -> None:
        self.name = name
        self.last = last

class supervisor(employee):
    def __init__(self, name, last,password) -> None:
        super().__init__(name, last)
        self.password = password

class chefs(employee):
    def leave_request(self,days):
        return (f"May i take the leave of {str(days)} days...")

waqar = supervisor("waqar","W","my123")

john = chefs("John", "J")
own = chefs("Own","O")

print(john.leave_request(3))
print(john.name)
print(waqar.password)
print(john.last)