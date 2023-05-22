# write a program to display integer from of a list. given list=[1,"a","c",2,3,4]
def fun():
    listElements = [1, 'a', 'c', 2, 3, 4]

    for i in listElements:
        if type(i) == int:
            print(i)


fun()
