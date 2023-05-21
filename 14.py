# 14. Factorial of a given number
num = int(input("Enter the number: "))
def q14(num):
    i = 1
    fact = 1
    if num > 0:
        while i <= num:
            fact = fact * i
            i += 1
    print(f"The factorial of {num} is {fact}.")
q14(num)
