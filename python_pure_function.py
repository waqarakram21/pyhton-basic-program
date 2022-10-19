my_list = [1,2,3]

def add_to_list(lst,items):
    nl =  lst.copy()
    nl.append(items)
    return nl

new_list = add_to_list(my_list,4)

print(my_list)
print(new_list)