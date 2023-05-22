def fun():
    num = int(input("Enter a number: "))
    isPerfectSquare = False

    for i in range(num+1):
        if i*i == num:
            isPerfectSquare = True
            break

    if isPerfectSquare:
        print(num, "is a perfect square")
    else:
        print(num, "is not a perfect square")


fun()
