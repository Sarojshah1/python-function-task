def fun():
    range_value = input('Enter: ')
    ary = []
    sum = 0

    for i in range(1, int(range_value)):
        if (i % 2 != 0):
            ary.append(i)

    for j in range(0, len(ary)):
        sum += ary[j]

    print(sum)


fun()
