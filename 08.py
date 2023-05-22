# given list is [1,2,3,4] but expected output in new list [2,3,4,5]
def fun():
    givenList = [1, 2, 3, 4]
    for i in givenList:
        if i == 1:
            givenList.remove(i)
            givenList.append(5)
    print(givenList)


fun()
