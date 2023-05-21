# 5. Multiplication of a each element. given list = [4,5,3,2]
def q5():
    list = [4,5,3,2]
    i = 0
    while i < len(list):
        j = 1
        while j < 11:
            print(str(list[i]) + 'x' + str(j) + "=",list[i]*j)
            j += 1
        i += 1
q5()
