def fun():
    inputNumber = int(input("Enter Prime"))
    prime = False
    if inputNumber == 1:
        print("not prime")
    elif inputNumber > 1:
        for i in range(2, inputNumber):
            if inputNumber % i == 0:
                prime = True
                break

        if prime:
            print('not prime')
        else:
            print('prime')


fun()
