# using slice function.
# str[start:stop:step] this is called the extended slice sytax.
# we can also reverse the same string but for the ease we did so.
name = "waqarakrambhutta"
new_name= name[::-1]
print(new_name)

# using recursion.
def string_reverse(str):
    if len(str) == 0:
        return str
    else:
        return string_reverse(str[1:]) + str[0]

name = "waqarakrambhutta"
reverse_name= string_reverse(name)
print(reverse_name)
