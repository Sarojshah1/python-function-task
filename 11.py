# 11. Python program that accepts a string and calculate the number of digits and letters and space.
string = input("Enter the string: ")
def q11(string):
    digits = 0
    letters = 0
    space = 0
    i = 0
    while i < len(string):
        if string[i].isdigit():
            digits += 1
        elif string[i].isalpha():
            letters += 1
        elif string[i].isspace():
            space += 1
        i += 1

    print(f"NUMBER OF DIGITS: {digits}")
    print(f"NUMBER OF LETTERS: {letters}")
    print(f"NUMBER OF SPACES: {space}")
q11(string)

