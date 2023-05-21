# 40. Given list is [1,2,3,4] but expected output is [1,"a",2,4].
list = [1,2,3,4]
def q40(list):
    new_list = []
    i = 0
    while i < len(list):
        if i == 1:
            new_list.append("a")
        elif i == 2:
            new_list.append(2)
        else:
            new_list.append(list[i])
        i += 1
    print(new_list)
q40(list)
