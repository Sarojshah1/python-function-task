# 20. Given list is list=[1,2,3,4] but print 1 and 2 only.
list = [1,2,3,4]
def q20(list):
    index = []
    i = 0
    while i < 2:
        index.append(list[i])
        i += 1
    print(index)
q20(list)
