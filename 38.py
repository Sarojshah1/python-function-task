# 38. Given list is lst=[1,2,3,4] but print 1 2 and 4 only
list = [1,2,3,4]
def q38(list):
    i = 0
    while i < len(list):
        if list[i] != 3:
            print(list[i])
        i += 1
q38(list)

