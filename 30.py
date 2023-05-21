# 30. Write a while loop which appends the square of each number to the new list.
list = eval(input("Enter the elements: "))
def q30(list):
    i = 0
    new_list = []
    while i < len(list):
        if type(list[i]) == int:
            new_list.append(list[i]**2)
        i += 1
    print(new_list)
q30(list)