# 39. Given list is lst=[1,2,3,4] but print 1 and 4 only.
list = [1,2,3,4]
def q39(list):
    i = 0
    while i < len(list):
        if list[i] != 2 and list[i] != 3:
            print(list[i])
        i += 1

q39(list)