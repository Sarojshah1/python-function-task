def fun():
    lst1 = [111, 32, -9, -45, -17, 9, 85, -10]
    lst2 = []
    for i in range(0, len(lst1)):
        if (lst1[i] >= 0):
            lst2.append(lst1[i])

    print(lst2)


fun()
