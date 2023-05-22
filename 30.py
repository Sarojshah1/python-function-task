def fun():
    lst = [1, 2, 3, 4, 5, 6]
    lst2 = []

    for i in range(1, len(lst)):
        lst2.append(lst[i]*lst[i])

    print(lst2)


fun()
