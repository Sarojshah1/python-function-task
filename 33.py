def fun():
    lst1 = [1, True, 4.78, "Ram"]
    lst2 = [False, True, 0]
    lst3 = []
    for i in range(0, len(lst1)):
        lst3.append(type(lst1[i]))
    for i in range(0, len(lst2)):
        lst3.append(type(lst2[i]))

    print(lst3)


fun()
