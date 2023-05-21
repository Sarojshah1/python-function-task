# 4. Write a program to display integer from a list. (Given List = [1,"a","c",2,3,4]).
def q4():
    List = [1,"a","c",2,3,4]
    integer = []
    b = len(List)
    i = 0
    while i < b:
        if type(List[i]) == int:
            integer.append(List[i])
        i = i + 1
    print(integer)
q4()
