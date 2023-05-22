def fun():
    inputList = eval(input("Enter List of Digit:"))
    sum = 0
    if type(inputList) == list:

        for i in inputList:
            sum = sum+i
            print(f"The sum of a enterd list is {sum}")
    else:
        print("Please enter the list of no")


fun()
