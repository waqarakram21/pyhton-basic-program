with open("newfile.txt","r") as file:
    file.writelines(["this is the first line written","\nthis is the ssecond line written","\nthis is the last line.","\nyou can write more than these lines"])