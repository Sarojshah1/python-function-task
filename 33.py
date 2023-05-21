# 33. Write a for loop which appends the type of each element in the first list to the second list.
list = eval(input("Enter the elements: "))
def q33(list):
    typeList = []
    i = 0
    while i < len(list):
        typeList.append(type(list[i]))
        i += 1
    print(typeList)
q33(list)
