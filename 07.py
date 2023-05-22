def fun():
    inputList = eval(input("Enter the list:"))
    b = []
    if type(inputList) == list:
        for i in inputList:
            b = [i]+b
            print(b)
    else:
        print("Please enter the list")


fun()
