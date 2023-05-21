# 32. Write a Python program that prints all the numbers from 0 to 6 except 3 and 6. given list=[0,1,2,3,4,5,6].
list = [0,1,2,3,4,5,6]
def q32(list):
    i = 0
    list1 = []
    while i < len(list):
        if list[i] != 3 and list[i] != 6:
            list1.append(list[i])
        i += 1
    print(list1)
q32(list)

