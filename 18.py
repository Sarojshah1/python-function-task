# 18. Python program to check a number is perfect number
num = int(input("Enter the number: "))
def q18(NUMBER):
    sum = 0
    i = 1
    while i < num:
        i += 1
        if num % i == 0:
            sum += i
    if sum == num:
        print(f"The entered number {num} is a perfect number..")
    else:
        print(f"The entered number {num} is not a perfect number..")
q18(num)
