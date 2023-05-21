# 24. Given list is [1,2,3,4] but expected output is [1,8,27,64].
list = [1,2,3,4]
def q24(list):
    new_list = []
    i = 0
    while i < len(list):
        new_list.append(list[i]**3)
        i += 1
    print(new_list)
q24(list)
