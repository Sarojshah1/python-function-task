# 8. Given list is [1,2,3,4] but expected output in new list [2,3,4,5]
list = [1,2,3,4]
def q8(list):
    new_list = []
    i = 0
    while i < len(list):
        new_list = new_list + [list[i] + 1]
        i = i + 1
    print(new_list)
q8(list)
