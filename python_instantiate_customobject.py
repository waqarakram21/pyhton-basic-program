# the process of creating a class and instantiating objcts in it.
from copyreg import dispatch_table
from operator import itemgetter


class recipie():
    def __init__(self,dish,items,time) -> None:
        self.dish = dish 
        self.items = items 
        self.time = time 
    def contents(self):
        print("this dish "+ self.dish +" han the items "+str(self.items)+ \
            " will prepare in "+ str(self.time)+"seconds")

Pizza= recipie("pizza",["cheeze","bread","chicken"],45)
Pasta= recipie("pasta",["item1","item2","item3"],55)

print(Pizza.dish)
print(Pizza.items)
print(Pizza.time)
