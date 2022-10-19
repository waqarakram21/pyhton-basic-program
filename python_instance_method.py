from curses import ALL_MOUSE_EVENTS
from http.client import PAYMENT_REQUIRED
from unicodedata import name


class payslip():
    def __init__(self,name,payment,amount) ->None:
        self.name = name
        self.payment=payment 
        self.amount=amount 
    def pay(self):
        self.payment="yes"
    def status(self):
        if self.payment=="yes":
            return (f"{self.name} is paid {self.payment}")
        else:
            return (f"{self.name} is not paid.")

nathon = payslip("nathon","no",1000)
roger = payslip("roger","no",2990)

print(nathon.status(),"\n",roger.status())