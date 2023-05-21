# 37. Python program to count the number of even and odd numbers from a series of numbers.
List = [1,2,3,4,5,6,7,8,9]
def q37(list):
    totalOdds = 0
    totalEven = 0
    i = 0
    while i < len(List):
        if List[i] % 2 == 0:
            totalEven += 1
        else:
            totalOdds += 1
        i += 1
    print(f"Total Even Numbers: {totalEven}")
    print(f"Total Odd Numbers: {totalOdds}")
q37(list)