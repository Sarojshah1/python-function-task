# 22. Python program to calculate the sum of all the even numbers within the given range.
start = int(input("Enter the starting point: "))
end = int(input("Enter the ending point: "))
def q22(start,end):
    i = start
    sum = 0
    while i <= end:
        if i % 2 == 0:
            sum += i
        i += 1
    print(f"The sum of even numbers within the given range is: {sum}")
q22(start, end)