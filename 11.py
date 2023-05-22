def fun():
    inputString = input("Enter String:")
    calculateSpace = 0
    calculateDigit = 0
    calculateLetter = 0

    for i in inputString:
        if i.isdigit():
            calculateDigit += 1
        elif i.isspace():
            calculateSpace += 1
        elif i.isalpha():
            calculateLetter += 1
    print(
        f'totoal letter={calculateLetter},total space-{calculateSpace},total digit={calculateDigit}')


fun()
