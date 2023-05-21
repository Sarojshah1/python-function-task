# 7. Reverse a list
def q7():
    list = eval(input("Enter the elements: "))
    i = 0
    reverse = []
    while i < len(list):
        reverse = [list[i]] + reverse
        i += 1
    print(reverse)
q7()

