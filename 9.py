# 9. Given number is prime or not.
num = int(input("Enter the number: "))
def q9(num):
    i = 2
    while i < num:
        i += 1
    if num % i == 0:
        print(">> PRIME NUMBER <<")
    else:
        print(">> COMPOSITE NUMBER <<")
q9(num)
