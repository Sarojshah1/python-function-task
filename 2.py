# 2. Sum of a list

list = [0,1,2,3]
def q2():
    sum = 0
    i = 0
    while i < 4:
        sum = sum + list[i]
        i = i + 1
    print(f"The sum is: {sum}")
q2()
