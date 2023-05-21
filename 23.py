# 23. Python program to count the space of a given string.
string = input("Enter the string: ")
def q23(string):
    i = 0
    space = 0
    while i < len(string):
        if string[i].isspace():
            space += 1
        i += 1
    print(f"Number of Spaces: {space}")
q23(string)
