status_code = int(input("what's the status code? "))

match status_code:
    case 200 | 201:
        print("success.")
    case 400:
        print("bad request.")
    case 500 | 501:
        print("sever error.")
    case _:
        print("the defult signal...")
        