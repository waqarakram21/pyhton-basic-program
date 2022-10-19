def d():
    animal="elephant"
    def e():
        nonlocal animal
        animal="giraffe"
        print("inside nested function: ",animal)
    print("before calling function: ",animal)
    e()
    print("after nested function: ", animal)

