def fun():
    inputNumber = int(input("Enter a no:"))
    rangeOfMultiply = int(input("Enter a range"))
    for i in range(1, rangeOfMultiply+1):
        print(f'{inputNumber}*{i}={inputNumber*i}')


fun()
