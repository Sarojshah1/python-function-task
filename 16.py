def fun():
    num = int(input("Enter a number: "))
    sum = 0
    temp = num

    num_digits = len(str(num))

    while temp > 0:
        digit = temp % 10
        sum += digit ** num_digits
        temp //= 10

    if num == sum:
        print(num, "is an Armstrong number")
    else:
        print(num, "is not an Armstrong number")


fun()
