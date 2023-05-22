def fun():
    inputRange = int(input('Enter range:'))
    for i in range(2, inputRange + 1):
        if i > 1:
            for j in range(2, i):
                if (i % j) == 0:
                    break
            else:
                print(j)


fun()
