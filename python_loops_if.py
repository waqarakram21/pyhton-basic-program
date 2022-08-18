favorites = ['Creme Brulee', 'Apple Pie', 'Churros', 'Tiramisú', 'Chocolate Cake']

for desserts in favorites:
    if desserts != "Apple Pie":
        pass    # this will only order the first iteration to the next because this will print "no desserts found as the first iteration is not Apple pie"...
    elif desserts == "Apple Pie":
        print("favorite from this list is: ", desserts)
        break
    else:
        print("no desserts found...")
        continue