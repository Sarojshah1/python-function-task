# 21. Python program to calculate the sum of all the odd numbers within the given range.
start = int(input("Enter the starting point: "))
end = int(input("Enter the ending point: "))
def q21(start,end):
    sum = 0
    i = start
    while i <= end:
        if i % 2 != 0:
            sum += i
        i += 1
    print(f"The sum of odd numbers within the given range is: {sum}")
q21(start, end)