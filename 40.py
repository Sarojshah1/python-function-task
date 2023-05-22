def fun():
    lst = [1, 2, 3, 4]
    new_list = []

    for i in range(len(lst)):
        if i == 0:
            new_list.append(lst[i])
        elif i == 1:
            new_list.append("a")
        elif i == 2:
            new_list.append(lst[i])
        elif i == 3:
            new_list.append(lst[i])

    print(new_list)


fun()
