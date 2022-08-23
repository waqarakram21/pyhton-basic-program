from tkinter import OFF
from typing import MutableMapping


def calculate_tax(bill, tax):
    return round((bill*tax)/100,1)

print(calculate_tax(175,15))


