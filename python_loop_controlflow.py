num_list = [33,42,5,66,77,22,16,79,36,62,78,43,88,39,53,67,89,11]

count=0
for x,num in enumerate(num_list):  
    count+=1 
    if num==88: # emumerate function counts the number of items in the list before the given item in the list...
        print("the number is found ", x)
        break

print(count) # Count will counts the number till the item in the condition.



# example for enumerate function...

x=("ammar","waqar","qasim","yousaf","abubaker") # names of persons in list.
y=enumerate(x)

print(list(y))