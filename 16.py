# 16. Python program to check whether a number is armstrong or not.
def q16():
    num = input("Enter the number: ")
    sum = 0
    a = len(num)
    i = 0
    while i < a:
        sum += int(num[i])**a
        i += 1
    if sum == num:
        print(f"The entered number {num}, is an armstrong number!")
    else:
        print(f"The entered number {num}, is not an armstrong number!")
q16()
