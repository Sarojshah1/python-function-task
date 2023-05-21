# 10. Write a python program to display all the prime numbers within a given range, take input from user for range
lower = int(input("Enter the lower range: "))
upper = int(input("Enter the upper range: "))

iterate through the range and print prime numbers
def q10(lower, upper):
    print("Prime numbers between", lower, "and", upper, "are:")
    num = lower
    while num <= upper:
        # check if the number is greater than 1
        if num > 1:
            # check if the number is divisible by any number except 1 and itself
            i = 2
            while i < num:
                if (num % i) == 0:
                    break
                i += 1
            else:
                print(num)
        num += 1
q10(lower, upper)
