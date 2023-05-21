# 17. Python program to check a number is perfect square.
def q17():
    num = int(input("Enter the number: "))
    i = 0
    while i*i < num:
        i += 1
    if i * i == num:
        print(f"The given number {num} is a perfect square..")
    else:
        print(f"The given number {num} is not a perfect square..")
q17()
