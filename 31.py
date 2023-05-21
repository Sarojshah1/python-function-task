# 31. Write a for loop using an if statement, that appends each number to the new list if it's positive. given lst1=[111, 32, -9, -45, -17, 9, 85, -10]
list1 = [111, 32, -9, -45, -17, 9, 85, -10]
def q31(list1):
    i = 0
    list2 = []
    while i < len(list1):
        if list1[i] > 0:
            list2.append(list1[i])
        i += 1
    print(list2)
q31(list1)
