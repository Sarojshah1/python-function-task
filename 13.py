# 13. Program to print the given number is odd or even.
num = int(input("Enter the number: "))
def q13(num):
    i = num
    while i <= num:
        if num % 2 == 0:
            print(f"{num} is an even number!")
            break
        else:
            print(f"{num} is odd number!")
            break
q13(num)

