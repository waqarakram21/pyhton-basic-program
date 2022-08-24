from pkgutil import extend_path


list = [1,2,3,4,5]

# print(list[2]) # simple way to print the list.
#to extend the list or to add another item in the list.
#using the following function we do so.
# list.insert(len(list), 6)
#this will add 6 to the list.
# list.append(6)
# append keyword will automatically add 6 to list
list.extend([6,7,8])
#by extend keyword we can add multiple items.
# we can also delet any item from the list.
# list.pop(5)
del list[3]
print(list)



 

