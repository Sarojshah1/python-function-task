# 26. Place a break statement in the for loop so that it prints from 0 to 7 only (including 7). Given range(50)
def q26():
    i = 0
    while i<=50:
        if i > 7:
            break
        else:
            print(i)
            i += 1
q26()
