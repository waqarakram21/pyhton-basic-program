coffee_types = ["Espresso","Arabica","Decaf","Robusta","Black coffee"]

def reverse(str):
    return str[::-1]

reversed_coffee = map(reverse,coffee_types)

for _ in reversed_coffee:
    print(_)