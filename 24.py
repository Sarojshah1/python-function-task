def fun():
    list = [1, 2, 3, 4]
    list2 = []

    for i in range(0, len(list)):
        list2.append(list[i]*list[i]*list[i])

    list = list2
    print(list)


fun()
