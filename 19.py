# 19. Print multiplication table from 1-8
list = [1,2,3,4,5,6,7,8]
def q19(list):
    i = 0
    while i < len(list):
        j = 1
        while j < 11:
            print(f"{list[i]} x {j} = {list[i]*j}")
            j += 1
        i += 1
q19(list)
