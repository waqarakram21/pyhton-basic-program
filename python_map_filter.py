ciggrates = ["morven","classic","dunhill","capstan","cobera","goldleaf"]

def c_cig(brand):
    if brand[0] == "c":
        return brand

# map_cig= map(c_cig, ciggrates)
# print(map_cig) 

# for _ in map_cig:
#     print(_)

map_cig = filter(c_cig,ciggrates)
print(map_cig)

for _ in map_cig:
    print(_)